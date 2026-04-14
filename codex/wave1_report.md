# Wave 1 Verification Report

## w1-01 Determinism check (`--voice pirate`, two runs per section)
- Could not complete: Ollama unavailable while testing section `s00_opening`.

## w1-02 Verbatim fidelity check (model output vs source bytes)
- Not runnable here because Ollama is unavailable.

## w1-03 Schema/calibration/coordinates consistency
- No key or section-ID mismatches found.

## w1-04 Word budget deviation vs `calibration/density.json`
- s00_opening: actual=304, budget=320, deviation=-5.0% [OK]
- s01_brains_rgb: actual=318, budget=520, deviation=-38.8% [⚠️]
- s02_dogs_computation: actual=388, budget=580, deviation=-33.1% [⚠️]
- s03_color_you_cant_see: actual=356, budget=480, deviation=-25.8% [⚠️]
- s04_what_engineers_found: actual=303, budget=500, deviation=-39.4% [⚠️]
- s05_mantis_shrimp_problem: actual=444, budget=620, deviation=-28.4% [⚠️]
- s06_what_im_building: actual=430, budget=560, deviation=-23.2% [⚠️]
- s07_coda: actual=296, budget=320, deviation=-7.5% [OK]

## w1-05 Dead code scan in `build.py` (static)
- Unused imports (static): ['hashlib', 'CALIBRATION']
- Potentially unused functions (never called by name in file): ['get_backend']

## w1-06 Security audit of `build.py`
- **Medium**: `--voice` is interpolated into `voices/{voice}.json` without sanitizing path segments. A crafted value like `../calibration/density` resolves outside `voices/` and can read arbitrary JSON files in-repo.
- **Low**: `sys.path.insert(0, REPO_DIR)` + `from steer_coordinates import ...` trusts repository-local Python import resolution, which is risky if repo contents are untrusted.
- **No findings**: no shell command execution, no eval/exec, no unsafe deserialization (JSON only), and HTTP payloads are serialized with `json.dumps`.

## w1-07 Behavior without Ollama
- `python3 build.py --voice pirate` failed gracefully with a clear message (`Ollama not reachable... Start Ollama first`) and no Python stack trace.
- `python3 build.py --no-model --out /tmp/w1_nomodel.md` succeeded without Ollama.

## w1-08 `--verify` reliability after single-word source edit
- Changed one word in `sections/s00_opening.md`, ran `python3 build.py --verify`, and it still printed PASS.
- Conclusion: `--verify` only checks build output against the *current* source files, so it cannot detect source tampering/regressions against a historical baseline.

## w1-09 README factual claims check
- File-path claims checked: `sections/`, `schema.json`, `steer_coordinates.py`, `calibration/`, `sources.json`, `build.py` all exist.
- Command claim verified: `python3 steer_coordinates.py` works and prints coordinate map.
- Command claim verified with caveat: `python3 build.py --verify` runs, but it is weaker than implied (cannot catch source-file changes; see w1-08).
- Command claim environment-dependent: model-backed build commands requiring Ollama are accurate but were not executable here because Ollama is not running.

## w1-10 Missing test edge cases added
Added 3 edge-case tests in `tests/test_determinism.py`:
- `test_coord_key_normalizes_hyphenated_slug`
- `test_build_substack_appends_repo_footer`
- `test_verify_reports_line_mismatch`
