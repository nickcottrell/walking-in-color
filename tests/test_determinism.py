#!/usr/bin/env python3
"""
Adversarial test suite for Walking Through Color pipeline.

Philosophy: every test here tries to PROVE the pipeline is broken.
If all tests pass, the skeptic just proved the thesis.

Requires: Ollama running locally with qwen2.5:7b-instruct-q4_K_M
Run: python3 -m pytest tests/ -v
"""

import hashlib
import json
import os
import re
import sys

import pytest

# Add repo root to path
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_DIR)

import build
from steer_coordinates import COORDINATES, CALIBRATION


# ---------------------------------------------------------------------------
# DETERMINISM: prove it is NOT reproducible (it is)
# ---------------------------------------------------------------------------

class TestDeterminism:
    """Try to prove the pipeline produces different output on repeated runs."""

    def _generate_section(self, section_idx, voice=None):
        schema = build.load_json(build.SCHEMA_PATH)
        section = schema["sections"][section_idx]
        key = build.coord_key(section)
        coord = COORDINATES[key]
        source = build.load_section(
            section["id"], section["slug"].replace("-", "_")
        )
        speculation = build.load_json(build.SPECULATION_PATH)
        tone = build.load_json(build.TONE_PATH)
        density = build.load_json(build.DENSITY_PATH)
        sys_prompt = build.build_system_prompt(
            section, coord, speculation, tone, density, voice=voice
        )
        if voice:
            prompt = "Rewrite this section in the voice described:\n\n" + source
        else:
            prompt = "Reproduce this section verbatim:\n\n" + source
        return build.ollama_generate(prompt, system_prompt=sys_prompt)

    def test_verbatim_determinism(self):
        """Two verbatim runs of the same section must produce identical bytes."""
        run1 = self._generate_section(0)
        run2 = self._generate_section(0)
        assert hashlib.sha256(run1.encode()).hexdigest() == \
               hashlib.sha256(run2.encode()).hexdigest(), \
               "Verbatim mode is not deterministic"

    def test_voice_determinism(self):
        """Two pirate runs of the same section must produce identical bytes."""
        voice = build.load_voice("pirate")
        run1 = self._generate_section(7, voice=voice)
        run2 = self._generate_section(7, voice=voice)
        assert hashlib.sha256(run1.encode()).hexdigest() == \
               hashlib.sha256(run2.encode()).hexdigest(), \
               "Voice filter is not deterministic"

    def test_cross_section_determinism(self):
        """Every section must be deterministic, not just the easy ones."""
        voice = build.load_voice("pirate")
        for idx in range(8):
            run1 = self._generate_section(idx, voice=voice)
            run2 = self._generate_section(idx, voice=voice)
            h1 = hashlib.sha256(run1.encode()).hexdigest()
            h2 = hashlib.sha256(run2.encode()).hexdigest()
            assert h1 == h2, "Section {} is not deterministic".format(idx)


# ---------------------------------------------------------------------------
# VERBATIM FIDELITY: prove the model corrupts the source text (it doesnt)
# ---------------------------------------------------------------------------

class TestVerbatimFidelity:
    """Try to prove the model alters the essay when told to reproduce it."""

    def test_verbatim_matches_source(self):
        """Model output must match source sections byte-for-byte."""
        schema = build.load_json(build.SCHEMA_PATH)
        speculation = build.load_json(build.SPECULATION_PATH)
        tone = build.load_json(build.TONE_PATH)
        density = build.load_json(build.DENSITY_PATH)

        for section in schema["sections"]:
            key = build.coord_key(section)
            coord = COORDINATES[key]
            source = build.load_section(
                section["id"], section["slug"].replace("-", "_")
            )
            sys_prompt = build.build_system_prompt(
                section, coord, speculation, tone, density
            )
            prompt = "Reproduce this section verbatim:\n\n" + source
            output = build.ollama_generate(prompt, system_prompt=sys_prompt)
            assert output.strip() == source.strip(), \
                "Model altered section: {}".format(section["title"])

    def test_full_build_matches_concat(self):
        """Full model build must match direct section concatenation."""
        direct = build.build_essay(use_model=False)
        steered = build.build_essay(use_model=True)
        clean = re.sub(r"\x1b\[[0-9;]*[a-zA-Z]", "", steered)
        assert clean.strip() == direct.strip(), \
            "Full build diverges from source concatenation"


# ---------------------------------------------------------------------------
# FACTUAL PRESERVATION: prove the voice filter destroys data (it doesnt)
# ---------------------------------------------------------------------------

class TestFactualPreservation:
    """Try to prove the pirate voice filter corrupts factual claims."""

    # Each entry is a list of acceptable variants. At least one must appear.
    REQUIRED_FACTS = [
        ["93.7%", "93.7 percent"],
        ["190 milliseconds", "190ms", "190 ms"],
        ["215"],
        ["238"],
        ["811"],
        ["398"],
        ["16.7 million"],
        ["650nm", "650 nm"],
        ["530nm", "530 nm"],
        ["450nm", "450 nm"],
        ["60 gigabits", "sixty gigabits", "60 gbps", "60gbps", "60 Gbps"],
        ["500-meter", "500 meter", "500m", "500 metres"],
        ["30%", "30 percent"],
        ["35%", "35 percent"],
        ["Hofstadter unit", "Hofstadter"],
        ["Fudan"],
        ["Nagaoka"],
        ["Princeton"],
        ["Quanzhou"],
        ["VRGB"],
        ["A Bridge in the Sky", "Bridge in the Sky"],
    ]

    def test_pirate_preserves_facts(self):
        """Every factual claim must survive the pirate voice filter."""
        voice = build.load_voice("pirate")
        essay = build.build_essay(use_model=True, voice=voice)
        essay_lower = essay.lower()
        missing = []
        for variants in self.REQUIRED_FACTS:
            found = any(v.lower() in essay_lower for v in variants)
            if not found:
                missing.append(variants[0])
        assert not missing, \
            "Pirate filter destroyed facts: {}".format(missing)


# ---------------------------------------------------------------------------
# STRUCTURAL INTEGRITY: prove the voice filter breaks the sections (it doesnt)
# ---------------------------------------------------------------------------

class TestStructuralIntegrity:
    """Try to prove the voice filter collapses the section structure."""

    SECTION_MARKERS = [
        "Part One",
        "Part Two",
        "Part Three",
        "Part Four",
        "Part Five",
        "Part Six",
        "Coda",
    ]

    def test_pirate_preserves_sections(self):
        """All section titles must appear in voice-filtered output."""
        voice = build.load_voice("pirate")
        essay = build.build_essay(use_model=True, voice=voice)
        missing = []
        for marker in self.SECTION_MARKERS:
            if marker not in essay:
                missing.append(marker)
        assert not missing, \
            "Pirate filter collapsed sections: {}".format(missing)

    def test_section_order_preserved(self):
        """Sections must appear in the correct order."""
        voice = build.load_voice("pirate")
        essay = build.build_essay(use_model=True, voice=voice)
        positions = []
        for marker in self.SECTION_MARKERS:
            pos = essay.find(marker)
            if pos >= 0:
                positions.append(pos)
        assert positions == sorted(positions), \
            "Pirate filter reordered sections"


# ---------------------------------------------------------------------------
# STEERING COORDINATE INTEGRITY: prove the coordinates are arbitrary (not)
# ---------------------------------------------------------------------------

class TestSteeringCoordinates:
    """Try to prove the VRGB coordinates are arbitrary noise."""

    def test_all_sections_have_coordinates(self):
        """Every section in the schema must map to a coordinate."""
        schema = build.load_json(build.SCHEMA_PATH)
        for section in schema["sections"]:
            key = build.coord_key(section)
            assert key in COORDINATES, \
                "Section {} has no steering coordinate".format(key)

    def test_hex_values_are_valid(self):
        """Every hex value must be a valid 6-digit RGB hex."""
        for key, coord in COORDINATES.items():
            h = coord["hex"]
            assert re.match(r"^#[0-9A-Fa-f]{6}$", h), \
                "Invalid hex for {}: {}".format(key, h)

    def test_rgb_matches_hex(self):
        """R, G, B values must match the hex string."""
        for key, coord in COORDINATES.items():
            h = coord["hex"].lstrip("#")
            r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
            assert coord["r"] == r, "{} R mismatch".format(key)
            assert coord["g"] == g, "{} G mismatch".format(key)
            assert coord["b"] == b, "{} B mismatch".format(key)

    def test_anchor_sections_are_low_tension(self):
        """Anchor sections (opening, coda) must have low tension/speculation."""
        for key, coord in COORDINATES.items():
            if coord["role"] == "anchor":
                assert coord["tension"] <= 0.3, \
                    "Anchor {} has tension {}".format(key, coord["tension"])
                assert coord["speculation"] <= 0.2, \
                    "Anchor {} has speculation {}".format(key, coord["speculation"])

    def test_arc_returns_to_warmth(self):
        """The coordinate arc must start and end in warm tones (high R)."""
        keys = list(COORDINATES.keys())
        first = COORDINATES[keys[0]]
        last = COORDINATES[keys[-1]]
        assert first["r"] > first["b"], "Opening is not warm-toned"
        assert last["r"] > last["b"], "Coda is not warm-toned"

    def test_speculation_peak_matches_schema(self):
        """The highest speculation value must be on the section the schema
        declares as the speculation peak."""
        schema = build.load_json(build.SCHEMA_PATH)
        declared_peak = schema["arc"]["speculation_peak"]
        max_spec = max(COORDINATES.items(), key=lambda x: x[1]["speculation"])
        peak_id = max_spec[0].split("_", 1)[0]
        assert peak_id == declared_peak, \
            "Speculation peak is {} but schema declares {}".format(
                peak_id, declared_peak
            )


# ---------------------------------------------------------------------------
# SCHEMA CONSISTENCY: prove the metadata is self-contradictory (it isnt)
# ---------------------------------------------------------------------------

class TestSchemaConsistency:
    """Try to prove the schema, calibration, and coordinates contradict."""

    def test_word_budgets_sum_to_total(self):
        """Per-section word budgets must sum to declared total (within 10%)."""
        schema = build.load_json(build.SCHEMA_PATH)
        density = build.load_json(build.DENSITY_PATH)
        total = density["total_words"]
        section_sum = sum(
            v["words"] for v in density["per_section"].values()
        )
        assert abs(section_sum - total) / total < 0.10, \
            "Word budgets sum to {} but total declared as {}".format(
                section_sum, total
            )

    def test_all_calibration_keys_match_schema(self):
        """Every key in calibration files must correspond to a schema section."""
        schema = build.load_json(build.SCHEMA_PATH)
        valid_keys = set()
        for section in schema["sections"]:
            valid_keys.add(build.coord_key(section))

        for cal_file in ["speculation.json", "tone.json", "density.json"]:
            path = os.path.join(REPO_DIR, "calibration", cal_file)
            cal = build.load_json(path)
            for key in cal["per_section"]:
                assert key in valid_keys, \
                    "Calibration key {} in {} not in schema".format(
                        key, cal_file
                    )

    def test_source_files_exist_for_all_sections(self):
        """Every section in the schema must have a source .md file."""
        schema = build.load_json(build.SCHEMA_PATH)
        for section in schema["sections"]:
            slug = section["slug"].replace("-", "_")
            filename = "{}_{}.md".format(section["id"], slug)
            path = os.path.join(build.SECTIONS_DIR, filename)
            assert os.path.exists(path), \
                "Missing source file: {}".format(filename)
