# Walking In Color

An essay about orthogonal channel architectures -- in a dog's nose, a bird's eye, a shrimp's parallel lookup table, an optical fiber, and a hex color coordinate system called VRGB.

Written on a walk with a Standard Poodle named Jack Jack, through Ladera Ranch, California.

**Read the essay:** [nicholascottrell.substack.com/p/walking-in-color](https://nicholascottrell.substack.com/p/walking-in-color)

## What You're Looking At

An essay. And the rig that built it.

The essay is human-written prose. The rig is the scaffolding around it -- a coordinate system, a set of calibration knobs, a model backend, and a voice layer -- that shapes how the prose gets assembled into a final draft. You can read the essay on Substack (link above). You can also pop the hood, pull it apart, and run it yourself.

This is what VRGB looks like in the wild. The same three-orthogonal-channel idea the essay argues for is what's steering the essay's own assembly. The system is the argument.

## Tour

**sections/** -- Eight markdown files, one per part of the essay (s00 opening → s07 coda). The actual words. Edit here and the next build picks them up.

**schema.json** -- The map. Section IDs, word budgets, structural roles (anchor / evidence / expansion / convergence / complication / synthesis), and arc metadata (where tension peaks, where emotion peaks, where convergence happens).

**steer_coordinates.py** -- The VRGB coordinates. Every section gets a hex color plus two scalars: tension (0-1) and speculation (0-1). Red for the brain-RGB section because red is the first channel to fire. UV-leaning violet for the hummingbird section because that is literally the color you cannot see. Amber for the mantis shrimp because it is the tradeoff point. The coordinates are meaningful, not decorative.

**calibration/** -- Three knobs per section, stored as JSON:
- *speculation.json* -- ceiling on how far each section is allowed to reach beyond cited sources (0.10 in the opening, 0.85 at the mantis shrimp peak)
- *tone.json* -- grounded-to-lyrical axis (0.30 for engineering precision, 0.85 for the coda)
- *density.json* -- per-section word budgets that sum to the global target

**voices/** -- Thirty-plus voice filter JSONs. Primer, academic, pirate, noir, zen, southern gothic, sagan, haiku, Shakespeare, stoner. Swap one in with --voice and the assembler rewrites every section in that register while preserving the argument. Most of them are jokes. Some of them surface things the default voice buries.

**sources.json** -- The citation registry. Full author lists, DOIs, journal names, and the specific finding cited in each section. Every claim in the essay that takes a number from a paper is traceable from here.

**build.py** -- The assembler. Reads sections, pulls their coordinates and calibration, pipes everything to a local Ollama model (Qwen 2.5 7B quantized, runs on a laptop) or to an OpenAI endpoint (for CI), and writes a draft. --verify mode confirms the output matches the source sections verbatim when no model is steering.

**codex/** -- The adversarial audit trail. Three waves of reports where a separate agent tried to break the argument: pipeline determinism, voice-filter argument preservation, and thesis defensibility. The repo has survived all three.

**generations/** -- Output drafts. Substack-ready, plain markdown, or voice-filtered.

## Build

Requires [Ollama](https://ollama.ai) with qwen2.5:7b-instruct-q4_K_M pulled locally.

```
# Full steered build (runs each section through Qwen with VRGB coordinates)
python3 build.py --substack --out generations/substack-draft.md

# Direct concatenation (no model, just assemble sections)
python3 build.py --no-model --out generations/draft.md

# Verify output matches source sections verbatim
python3 build.py --verify

# Print the steering coordinate map
python3 steer_coordinates.py

# Run the essay through a voice filter
python3 build.py --voice pirate --out generations/pirate-draft.md
python3 build.py --voice sagan --out generations/sagan-draft.md
python3 build.py --voice primer --out generations/primer-draft.md
```

## Fork It

Swap the prose, keep the rig. Drop your own sections into sections/, update schema.json with your word budgets, paint the arc in steer_coordinates.py, and rebuild. The rig does not care what you're writing about. It cares where the argument tightens, where it reaches, where it lands.

If you ship something built on this, credit the coordinate system and tag the repo. If you take issue with a claim, the "Disagree?" section at the bottom is live.

## The Argument

Four independent systems -- human trichromatic vision, canine olfactory computation, hummingbird tetrachromacy, and engineered wavelength division multiplexing -- all converge on the same architecture: orthogonal channels generating high-dimensional information space from a limited substrate.

VRGB (Virtual RGB) uses the 16.7 million positions in hex color space as semantic coordinates. The essay argues this isn't arbitrary -- it's building in the native dimensionality of human perception, using a principle that evolution and engineering discovered independently.

The full VRGB spec lives in its own repo: [github.com/nickcottrell/vrgb-spec](https://github.com/nickcottrell/vrgb-spec).

## Sources

| Section | Paper | Finding |
|---|---|---|
| Brain's RGB | Wu et al. (2023), *PeerJ Computer Science* 9:e1376. [DOI: 10.7717/peerj-cs.1376](https://doi.org/10.7717/peerj-cs.1376) | 93.7% EEG decoding of R/G/B, sequential peak latencies (R:190ms, G:215ms, B:238.5ms) |
| Dog's Computation | Komatsu, Yonezawa & Yamamoto (2025), *Next Research* 2(4). [DOI: 10.1016/j.nexres.2025.100847](https://doi.org/10.1016/j.nexres.2025.100847) | 3D X-ray CT + CFD analysis of canine olfactory airflow |
| Color You Can't See | Stoddard et al. (2020), *PNAS* 117(26):15112-15122. [DOI: 10.1073/pnas.1919377117](https://doi.org/10.1073/pnas.1919377117) | Wild hummingbirds discriminate nonspectral UV+visible colors |
| What Engineers Found | Cai (2021), *Frontiers in Physics* 9:731405. [DOI: 10.3389/fphy.2021.731405](https://doi.org/10.3389/fphy.2021.731405) | 60 Gbps via RGB wavelength + polarization multiplexing over 500m fiber |
| What I'm Building | Cottrell (2025), [VRGB Spec](https://github.com/nickcottrell/vrgb-spec) | Hex colorspace as semantic coordinate system |

## Steering Coordinate Arc

```
s00_opening              #C4956A  T:0.2 S:0.1  anchor
s01_brains_rgb           #E04040  T:0.5 S:0.2  evidence
s02_dogs_computation     #6B8E6B  T:0.6 S:0.4  evidence
s03_color_you_cant_see   #7B3FA0  T:0.7 S:0.5  expansion
s04_what_engineers_found  #3070C0  T:0.8 S:0.3  convergence
s05_mantis_shrimp_problem #D4A830  T:0.9 S:0.8  complication
s06_what_im_building     #2E2E5E  T:0.7 S:0.7  synthesis
s07_coda                 #B8865A  T:0.1 S:0.1  anchor
```

The arc traces a loop: warm/grounded at the edges, through the biological spectrum (red, green, violet, blue), into the engineering/tradeoff midpoint (amber), down into synthesis (indigo), and back to sodium orange.

## Author

Nick Cottrell
3DMATH

## License

Copyright 2026 Nick Cottrell / 3DMATH.

The essay, steering coordinates, VRGB whitepaper, and generative
architecture are original authored works. Voice filter definitions,
generated drafts, and verification reports were produced with the
assistance of open and commercially available language models
(Qwen 2.5, GPT-4o-mini, Claude) running locally and via API.
The use of these models for creative and analytical work is
protected expression under applicable law. Model outputs in this
repository are published artifacts of that process.

All rights reserved except where noted. Fork, study, and build on
the architecture. Credit the source.

## Disagree?

Open a PR. If you take issue with a claim, a citation, a coordinate,
or the thesis itself -- submit it. This repo has already survived
three waves of adversarial review. Make it stronger.
