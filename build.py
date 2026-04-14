#!/usr/bin/env python3
"""
Walking Through Color -- Build Script

Assembles the essay from per-section source files, steered by VRGB
coordinates via Qwen 2.5 7B Instruct (quantized, local Ollama).

Usage:
    python3 build.py                  # build to stdout
    python3 build.py --out draft.md   # build to file
    python3 build.py --verify         # verify output matches source sections
    python3 build.py --substack       # build Substack-ready version with repo link
"""

import argparse
import json
import os
import subprocess
import sys

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SECTIONS_DIR = os.path.join(REPO_DIR, "sections")
SCHEMA_PATH = os.path.join(REPO_DIR, "schema.json")
SPECULATION_PATH = os.path.join(REPO_DIR, "calibration", "speculation.json")
TONE_PATH = os.path.join(REPO_DIR, "calibration", "tone.json")
DENSITY_PATH = os.path.join(REPO_DIR, "calibration", "density.json")

MODEL = "qwen2.5:7b-instruct-q4_K_M"

REPO_URL = "https://github.com/nickcottrell/walking-in-color"

# Import steering coordinates
sys.path.insert(0, REPO_DIR)
from steer_coordinates import COORDINATES, CALIBRATION


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def load_section(section_id, slug):
    """Load a section source file."""
    filename = "{}_{}.md".format(section_id, slug)
    path = os.path.join(SECTIONS_DIR, filename)
    with open(path, "r") as f:
        return f.read().strip()


def ollama_generate(prompt, system_prompt=None):
    """Call Qwen via Ollama API."""
    cmd = ["ollama", "run", MODEL]
    full_prompt = ""
    if system_prompt:
        full_prompt = system_prompt + "\n\n"
    full_prompt += prompt

    result = subprocess.run(
        cmd,
        input=full_prompt,
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode != 0:
        print("Ollama error: {}".format(result.stderr), file=sys.stderr)
        sys.exit(1)
    return result.stdout.strip()


def build_system_prompt(section, coord, speculation, tone, density):
    """Build the steering prompt for a section."""
    lines = [
        "You are a precise editorial assistant.",
        "Your task: reproduce the following essay section VERBATIM.",
        "Do not alter, summarize, expand, or rephrase any text.",
        "Output the section exactly as provided, word for word.",
        "",
        "Section steering context (for your awareness, not for modification):",
        "  Title: {}".format(section["title"]),
        "  Role: {}".format(section["role"]),
        "  VRGB coordinate: {}".format(coord["hex"]),
        "  Tension: {:.1f}".format(coord["tension"]),
        "  Speculation: {:.1f}".format(coord["speculation"]),
        "  Speculation ceiling: {:.2f}".format(
            speculation["per_section"][coord_key(section)]["ceiling"]
        ),
        "  Tone: {} ({:.2f})".format(
            tone["per_section"][coord_key(section)]["label"],
            tone["per_section"][coord_key(section)]["tone"],
        ),
        "  Word budget: {}".format(density["per_section"][coord_key(section)]["words"]),
        "",
        "Reproduce the text below exactly. No additions. No omissions.",
    ]
    return "\n".join(lines)


def coord_key(section):
    """Map schema section to coordinate/calibration key."""
    return "{}_{}".format(section["id"], section["slug"].replace("-", "_"))


def build_essay(use_model=True):
    """Assemble the full essay from sections, optionally through Qwen."""
    schema = load_json(SCHEMA_PATH)
    speculation = load_json(SPECULATION_PATH)
    tone = load_json(TONE_PATH)
    density = load_json(DENSITY_PATH)

    parts = []

    for section in schema["sections"]:
        key = coord_key(section)
        coord = COORDINATES.get(key)
        source_text = load_section(section["id"], section["slug"].replace("-", "_"))

        if use_model:
            sys_prompt = build_system_prompt(
                section, coord, speculation, tone, density
            )
            prompt = "Reproduce this section verbatim:\n\n{}".format(source_text)
            output = ollama_generate(prompt, system_prompt=sys_prompt)
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
        # Find first divergence
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
        help="Skip Ollama/Qwen, concatenate sections directly",
    )
    args = parser.parse_args()

    use_model = not args.no_model

    if args.verify:
        # Verify always uses direct concatenation (the source of truth)
        essay = build_essay(use_model=False)
        verify(essay)
        return

    essay = build_essay(use_model=use_model)

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
