#!/usr/bin/env python3
"""
Walking Through Color -- Build Script

Assembles the essay from per-section source files, steered by VRGB
coordinates via a local or cloud LLM backend.

Backends:
    ollama   -- Qwen 2.5 7B Instruct Q4 (local, default)
    openai   -- gpt-4o-mini via OpenAI API (cloud, for Codex/CI)

Set backend via env var or --backend flag:
    export WALKING_BACKEND=openai
    export OPENAI_API_KEY=sk-...

Usage:
    python3 build.py                          # build to stdout (verbatim)
    python3 build.py --out draft.md           # build to file
    python3 build.py --verify                 # verify output matches source
    python3 build.py --substack               # Substack-ready with repo link
    python3 build.py --voice pirate           # apply a voice filter
    python3 build.py --backend openai         # use OpenAI instead of Ollama
"""

import argparse
import hashlib
import json
import os
import sys
import urllib.request
import urllib.error

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SECTIONS_DIR = os.path.join(REPO_DIR, "sections")
SCHEMA_PATH = os.path.join(REPO_DIR, "schema.json")
SPECULATION_PATH = os.path.join(REPO_DIR, "calibration", "speculation.json")
TONE_PATH = os.path.join(REPO_DIR, "calibration", "tone.json")
DENSITY_PATH = os.path.join(REPO_DIR, "calibration", "density.json")
VOICES_DIR = os.path.join(REPO_DIR, "voices")
REPO_URL = "https://github.com/nickcottrell/walking-in-color"

# ---------------------------------------------------------------------------
# Backend configuration
# ---------------------------------------------------------------------------

BACKENDS = {
    # --- Local (Ollama) ---
    "ollama": {
        "model": "qwen2.5:7b-instruct-q4_K_M",
        "url": "http://localhost:11434/api/generate",
        "seed": 42,
        "temperature": 0.0,
        "api": "ollama",
        "tier": "baseline",
        "description": "Qwen 2.5 7B Instruct, 4-bit quantized, local CPU",
    },
    # --- OpenAI: baseline (Codex default) ---
    "openai": {
        "model": "gpt-4o-mini",
        "url": "https://api.openai.com/v1/chat/completions",
        "seed": 42,
        "temperature": 0.0,
        "api": "openai",
        "tier": "baseline",
        "description": "GPT-4o-mini via OpenAI API",
    },
    # --- OpenAI: stretch ---
    "openai-4o": {
        "model": "gpt-4o",
        "url": "https://api.openai.com/v1/chat/completions",
        "seed": 42,
        "temperature": 0.0,
        "api": "openai",
        "tier": "stretch",
        "description": "GPT-4o via OpenAI API (stretch benchmark)",
    },
    # --- Anthropic: stretch ---
    "anthropic": {
        "model": "claude-sonnet-4-6",
        "url": "https://api.anthropic.com/v1/messages",
        "seed": 42,
        "temperature": 0.0,
        "api": "anthropic",
        "tier": "stretch",
        "description": "Claude Sonnet 4.6 via Anthropic API (stretch benchmark)",
    },
}


def get_backend():
    """Resolve which backend to use from env or default."""
    name = os.environ.get("WALKING_BACKEND", "ollama")
    if name not in BACKENDS:
        print("Unknown backend: {}".format(name), file=sys.stderr)
        print("Available: {}".format(", ".join(BACKENDS.keys())), file=sys.stderr)
        sys.exit(1)
    return name, BACKENDS[name]


# ---------------------------------------------------------------------------
# Import steering coordinates
# ---------------------------------------------------------------------------

sys.path.insert(0, REPO_DIR)
from steer_coordinates import COORDINATES, CALIBRATION


# ---------------------------------------------------------------------------
# File loaders
# ---------------------------------------------------------------------------

def load_voice(voice_name):
    """Load a voice filter definition."""
    path = os.path.join(VOICES_DIR, "{}.json".format(voice_name))
    if not os.path.exists(path):
        print("Voice not found: {}".format(voice_name), file=sys.stderr)
        print("Available voices:", file=sys.stderr)
        for f in sorted(os.listdir(VOICES_DIR)):
            if f.endswith(".json"):
                print("  {}".format(f.replace(".json", "")), file=sys.stderr)
        sys.exit(1)
    return load_json(path)


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_section(section_id, slug):
    """Load a section source file."""
    filename = "{}_{}.md".format(section_id, slug)
    path = os.path.join(SECTIONS_DIR, filename)
    with open(path, "r") as f:
        return f.read().strip()


# ---------------------------------------------------------------------------
# Generation backends
# ---------------------------------------------------------------------------

def ollama_generate(prompt, system_prompt=None, backend=None):
    """Call Qwen via Ollama HTTP API. Deterministic: seed pinned, temperature zero."""
    payload = {
        "model": backend["model"],
        "prompt": prompt,
        "stream": False,
        "options": {
            "seed": backend["seed"],
            "temperature": backend["temperature"],
            "top_k": 1,
            "top_p": 0.0,
            "repeat_penalty": 1.0,
            "num_predict": 2048,
            "num_thread": 1,
            "num_gpu": 0,
        },
    }
    if system_prompt:
        payload["system"] = system_prompt

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        backend["url"],
        data=data,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body["response"].strip()
    except urllib.error.URLError as e:
        print("Ollama not reachable: {}".format(e), file=sys.stderr)
        print("Start Ollama first: ollama serve", file=sys.stderr)
        sys.exit(1)
    except KeyError:
        print("Unexpected Ollama response: {}".format(body), file=sys.stderr)
        sys.exit(1)


def openai_generate(prompt, system_prompt=None, backend=None):
    """Call OpenAI chat completions API. Deterministic: seed pinned, temperature zero."""
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        print("OPENAI_API_KEY not set.", file=sys.stderr)
        print("export OPENAI_API_KEY=sk-...", file=sys.stderr)
        sys.exit(1)

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": backend["model"],
        "messages": messages,
        "temperature": backend["temperature"],
        "seed": backend["seed"],
        "top_p": 1.0,
        "max_tokens": 2048,
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        backend["url"],
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(api_key),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body["choices"][0]["message"]["content"].strip()
    except urllib.error.URLError as e:
        print("OpenAI API error: {}".format(e), file=sys.stderr)
        sys.exit(1)
    except (KeyError, IndexError):
        print("Unexpected OpenAI response: {}".format(
            json.dumps(body, indent=2)[:500]
        ), file=sys.stderr)
        sys.exit(1)


def anthropic_generate(prompt, system_prompt=None, backend=None):
    """Call Anthropic messages API. Deterministic: temperature zero."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ANTHROPIC_API_KEY not set.", file=sys.stderr)
        print("export ANTHROPIC_API_KEY=sk-ant-...", file=sys.stderr)
        sys.exit(1)

    messages = [{"role": "user", "content": prompt}]

    payload = {
        "model": backend["model"],
        "messages": messages,
        "temperature": backend["temperature"],
        "max_tokens": 2048,
    }
    if system_prompt:
        payload["system"] = system_prompt

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        backend["url"],
        data=data,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body["content"][0]["text"].strip()
    except urllib.error.URLError as e:
        print("Anthropic API error: {}".format(e), file=sys.stderr)
        sys.exit(1)
    except (KeyError, IndexError):
        print("Unexpected Anthropic response: {}".format(
            json.dumps(body, indent=2)[:500]
        ), file=sys.stderr)
        sys.exit(1)


def generate(prompt, system_prompt=None, backend_name=None, backend=None):
    """Route to the correct backend."""
    api = backend.get("api", backend_name)
    if api == "openai":
        return openai_generate(prompt, system_prompt=system_prompt, backend=backend)
    elif api == "anthropic":
        return anthropic_generate(prompt, system_prompt=system_prompt, backend=backend)
    else:
        return ollama_generate(prompt, system_prompt=system_prompt, backend=backend)


# ---------------------------------------------------------------------------
# Steering prompt builder
# ---------------------------------------------------------------------------

def build_system_prompt(section, coord, speculation, tone, density, voice=None):
    """Build the steering prompt for a section."""
    key = coord_key(section)

    steering_block = "\n".join([
        "Section steering context:",
        "  Title: {}".format(section["title"]),
        "  Role: {}".format(section["role"]),
        "  VRGB coordinate: {}".format(coord["hex"]),
        "  Tension: {:.1f}".format(coord["tension"]),
        "  Speculation: {:.1f}".format(coord["speculation"]),
        "  Speculation ceiling: {:.2f}".format(
            speculation["per_section"][key]["ceiling"]
        ),
        "  Tone: {} ({:.2f})".format(
            tone["per_section"][key]["label"],
            tone["per_section"][key]["tone"],
        ),
        "  Word budget: {}".format(density["per_section"][key]["words"]),
    ])

    if voice is None:
        lines = [
            "You are a precise editorial assistant.",
            "Your task: reproduce the following essay section VERBATIM.",
            "Do not alter, summarize, expand, or rephrase any text.",
            "Output the section exactly as provided, word for word.",
            "",
            steering_block,
            "",
            "Reproduce the text below exactly. No additions. No omissions.",
        ]
    else:
        lines = [
            "You are a skilled literary voice actor.",
            "",
            "VOICE FILTER: {}".format(voice["name"]),
            "Description: {}".format(voice["description"]),
            "Register: {}".format(voice["register"]),
            "",
            "RULES:",
        ]
        for rule in voice["rules"]:
            lines.append("- {}".format(rule))
        lines.append("")
        lines.append(steering_block)
        lines.append("")
        lines.append(
            "Rewrite the section below in the voice described above."
        )
        lines.append(
            "Preserve the ARGUMENT and all FACTUAL CLAIMS exactly."
        )
        lines.append(
            "Preserve the STRUCTURE (section title, paragraph breaks)."
        )
        lines.append(
            "Transform the VOICE, REGISTER, and DICTION only."
        )
        lines.append(
            "Respect the word budget: approximately {} words.".format(
                density["per_section"][key]["words"]
            )
        )
        lines.append(
            "Respect the tension ({:.1f}) and speculation ({:.1f}) levels -- "
            "grounded sections stay grounded, speculative sections can reach.".format(
                coord["tension"], coord["speculation"]
            )
        )

    return "\n".join(lines)


def coord_key(section):
    """Map schema section to coordinate/calibration key."""
    return "{}_{}".format(section["id"], section["slug"].replace("-", "_"))


# ---------------------------------------------------------------------------
# Build pipeline
# ---------------------------------------------------------------------------

def build_essay(use_model=True, voice=None, backend_name="ollama", backend=None):
    """Assemble the full essay from sections, optionally through a model."""
    schema = load_json(SCHEMA_PATH)
    speculation = load_json(SPECULATION_PATH)
    tone = load_json(TONE_PATH)
    density = load_json(DENSITY_PATH)

    parts = []
    total = len(schema["sections"])

    for i, section in enumerate(schema["sections"]):
        key = coord_key(section)
        coord = COORDINATES.get(key)
        source_text = load_section(section["id"], section["slug"].replace("-", "_"))

        if use_model:
            label = voice["name"] if voice else "verbatim"
            print(
                "[{}/{}] {} ({}) [{}]".format(
                    i + 1, total, section["title"], label, backend_name
                ),
                file=sys.stderr,
            )
            sys_prompt = build_system_prompt(
                section, coord, speculation, tone, density, voice=voice
            )
            if voice:
                prompt = "Rewrite this section in the voice described:\n\n{}".format(
                    source_text
                )
            else:
                prompt = "Reproduce this section verbatim:\n\n{}".format(source_text)
            output = generate(
                prompt,
                system_prompt=sys_prompt,
                backend_name=backend_name,
                backend=backend,
            )
        else:
            output = source_text

        parts.append(output)

    return "\n\n".join(parts)


def build_substack(essay_text):
    """Wrap the essay with Substack footer linking back to the repo."""
    footer = "\n\n---\n\n"
    footer += "This essay was built with a VRGB generative architecture -- "
    footer += "per-section steering coordinates encoding the argument's "
    footer += "emotional and conceptual arc in hex color space.\n\n"
    footer += "Source, schema, and steering coordinates: [{}]({})\n".format(
        REPO_URL, REPO_URL
    )
    return essay_text + footer


def verify(essay_text):
    """Verify the built essay matches the source sections."""
    schema = load_json(SCHEMA_PATH)
    all_source = []
    for section in schema["sections"]:
        source = load_section(section["id"], section["slug"].replace("-", "_"))
        all_source.append(source)

    expected = "\n\n".join(all_source)

    if essay_text.strip() == expected.strip():
        print("PASS: built output matches source sections verbatim.")
        return True
    else:
        built_lines = essay_text.strip().splitlines()
        expected_lines = expected.strip().splitlines()
        for i, (b, e) in enumerate(zip(built_lines, expected_lines)):
            if b != e:
                print("FAIL at line {}:".format(i + 1))
                print("  expected: {}".format(e[:80]))
                print("  got:      {}".format(b[:80]))
                return False
        if len(built_lines) != len(expected_lines):
            print("FAIL: line count mismatch ({} vs {})".format(
                len(built_lines), len(expected_lines)
            ))
            return False
        return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Build Walking Through Color essay")
    parser.add_argument("--out", help="Output file path")
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify output matches source sections",
    )
    parser.add_argument(
        "--substack",
        action="store_true",
        help="Build Substack-ready version with repo link",
    )
    parser.add_argument(
        "--no-model",
        action="store_true",
        help="Skip model, concatenate sections directly",
    )
    parser.add_argument(
        "--voice",
        help="Apply a voice filter (e.g. pirate, noir, academic)",
    )
    parser.add_argument(
        "--backend",
        choices=list(BACKENDS.keys()),
        help="Model backend (default: WALKING_BACKEND env or ollama)",
    )
    args = parser.parse_args()

    backend_name = args.backend or os.environ.get("WALKING_BACKEND", "ollama")
    if backend_name not in BACKENDS:
        print("Unknown backend: {}".format(backend_name), file=sys.stderr)
        sys.exit(1)
    backend = BACKENDS[backend_name]

    use_model = not args.no_model
    voice = None
    if args.voice:
        voice = load_voice(args.voice)
        use_model = True

    if args.verify:
        essay = build_essay(use_model=False)
        verify(essay)
        return

    print(
        "Backend: {} ({})".format(backend_name, backend["description"]),
        file=sys.stderr,
    )

    essay = build_essay(
        use_model=use_model,
        voice=voice,
        backend_name=backend_name,
        backend=backend,
    )

    if args.substack:
        essay = build_substack(essay)

    if args.out:
        with open(args.out, "w") as f:
            f.write(essay)
        print("Written to {}".format(args.out), file=sys.stderr)
    else:
        print(essay)


if __name__ == "__main__":
    main()
