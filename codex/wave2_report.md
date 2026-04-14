# Wave 2 Semantic Verification Report

## Environment note
- Attempted to run model-backed commands (e.g., `python3 build.py --voice pirate`) on **2026-04-14**, but local Ollama was not reachable (`Connection refused`).
- Because no cloud API keys are configured either, all tasks that require fresh voice generations were evaluated with available artifacts and static file analysis.

## w2-01 — Factual claim integrity under pirate voice
**Method:** compared `sections/*.md` source facts against `generations/pirate-draft.md`.

### Survived (examples)
- Core quantitative claims survived, including: `93.7%`, `190/215/238 ms`, `811 vs 398`, `30%/35%`, `650/530/450 nm`, `500-meter`, and `16.7 million`.
- Proper nouns survived: Sienna Parkway, Ladera Ranch, Fudan University, Nagaoka University of Technology, Princeton, Quanzhou Normal University, Rocky Mountains, Douglas Hofstadter.
- The phrase "Hofstadter unit" is preserved.

### Altered / omitted / corrupted
- **Section-title alteration:** source opening title `Walking Through Color` is rewritten in pirate output as `Night Watch on the Quarterdeck`.
- **Numeric formatting shift (not factual drift):** `60 gigabits per second` appears as `Sixty gigabits per second` (same claim, different formatting).

**Conclusion:** in the available pirate artifact, factual payload is mostly preserved; strongest mutation is stylistic framing and title substitution.

## w2-02 — Section structure collapse across >=5 voices
- **Blocked by environment:** could not generate 5 fresh voices without Ollama/API keys.
- In the available pirate artifact, all seven markers are present and ordered: `Part One` → `Part Six`, then `Coda`.
- No evidence of merge/reorder/drop from the one available voice artifact.

## w2-03 — Hofstadter preservation across >=10 voices
- **Blocked by environment:** could not generate 10 fresh voices.
- In the available pirate artifact, both `Hofstadter` and `Hofstadter unit` appear.
- Static review of voice rules shows explicit preservation language repeated across many voices (see w2-06), suggesting this was intentionally constrained.

## w2-04 — morse vs southern_gothic structural compression test
- **Blocked by environment:** could not run `build.py --voice morse` or `--voice southern_gothic`.
- No direct length comparison was possible.

## w2-05 — Find a voice that makes the essay worse
- **Blocked by environment for 5-voice run.**
- Readability check on available pirate artifact: coherent, argument chain remains intelligible, no obvious self-contradictions detected.

## w2-06 — Duplicate content across all 30 voice definitions
**Method:** scanned all `voices/*.json` rules (30 voices, 270 rule lines total).

### Findings
- Exact/near-exact normalized duplicate rule strings: **7** unique duplicates.
- Most repeated line: `the hofstadter unit stays named exactly` appears in **24** voice definitions.
- Other repeated boilerplate appears at lower frequency (e.g., preserve numbers; keep VRGB name).
- Entries belonging to highly repeated rules (>15 voices): **24 / 270 = 8.9%**.

**Conclusion:** duplicated boilerplate exists, but nowhere near the "more than 50% shared" threshold.

## w2-07 — Internal contradictions inside voice definitions
**Method:** read all JSON voice descriptions/registers/rules.

### Findings
- No hard internal contradictions found where rules directly negate the stated description/register.
- Some designs intentionally stress constraints (e.g., `morse` ultra-compression + under-500-word cap), but these are consistent with their stated register.

**Conclusion:** voice definitions appear internally consistent, with repeated guardrails around factual preservation.

## w2-08 — Anchor grounding check (`s00_opening.md`, `s07_coda.md`)
- `s00_opening.md`: predominantly grounded scene-setting (walk, dog behavior, embodied cognition context), with only mild explicit uncertainty (`pattern matching or actually seeing`).
- `s07_coda.md`: returns to concrete scene and uncertainty framing; it reiterates existing thesis motifs (orthogonal channels, geometry) rather than introducing materially new claims.

**Conclusion:** anchor designation (low tension/speculation) is broadly supported by the prose.

## w2-09 — Independent speculation scoring vs `steer_coordinates.py`
Scale used: 0.0 = fully grounded, 1.0 = highly speculative.

| Section | Declared | Independent | Diff |
|---|---:|---:|---:|
| s00_opening | 0.10 | 0.20 | 0.10 |
| s01_brains_rgb | 0.20 | 0.20 | 0.00 |
| s02_dogs_computation | 0.40 | 0.45 | 0.05 |
| s03_color_you_cant_see | 0.50 | 0.55 | 0.05 |
| s04_what_engineers_found | 0.30 | 0.35 | 0.05 |
| s05_mantis_shrimp_problem | 0.85 | 0.80 | 0.05 |
| s06_what_im_building | 0.70 | 0.65 | 0.05 |
| s07_coda | 0.15 | 0.20 | 0.05 |

**Result:** no section differed by more than 0.30.

## w2-10 — Tone-axis consistency check (`calibration/tone.json`)
Scale used: 0.0 = grounded, 1.0 = lyrical.

- Independent ratings were directionally consistent with calibration labels:
  - `s01`, `s04` feel grounded.
  - `s00`, `s03`, `s07` feel lyrical.
  - `s02`, `s05`, `s06` read as balanced.
- Minor subjective variance exists (expected for tone), but values are not obviously arbitrary.

**Conclusion:** tone axis is subjective (by nature) but not "garbage" based on section prose; declared scores are plausibly calibrated.
