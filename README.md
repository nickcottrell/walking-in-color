# Walking In Color

An essay about orthogonal channel architectures -- in a dog's nose, a bird's eye, a shrimp's parallel lookup table, an optical fiber, and a hex color coordinate system called VRGB.

Written on a walk with a Standard Poodle named Jack Jack, through Ladera Ranch, California.

## What This Is

This is an essay with a generative architecture. The source text lives in `sections/` as individual files, one per section. The steering system that shapes assembly lives alongside it:

- **schema.json** -- section map, word budgets, structural roles
- **steer_coordinates.py** -- per-section VRGB hex coordinates encoding the essay's emotional and conceptual arc
- **calibration/** -- speculation ceiling, tone axis, density distribution per section
- **sources.json** -- citation registry for the four research papers and one whitepaper
- **build.py** -- assembles sections through Qwen 2.5 7B Instruct (quantized, local) with steering coordinates as system context

The steering coordinates encode the argument's shape: warm and grounded at the edges, speculative at the peak, with a loop that returns you to the sidewalk where you started.

## Build

Requires [Ollama](https://ollama.ai) with `qwen2.5:7b-instruct-q4_K_M` pulled locally.

```
# Full steered build (runs each section through Qwen with VRGB coordinates)
python3 build.py --substack --out generations/substack-draft.md

# Direct concatenation (no model, just assemble sections)
python3 build.py --no-model --out generations/draft.md

# Verify output matches source sections verbatim
python3 build.py --verify

# Print the steering coordinate map
python3 steer_coordinates.py
```

## The Argument

Four independent systems -- human trichromatic vision, canine olfactory computation, hummingbird tetrachromacy, and engineered wavelength division multiplexing -- all converge on the same architecture: orthogonal channels generating high-dimensional information space from a limited substrate.

VRGB (Virtual RGB) uses the 16.7 million positions in hex color space as semantic coordinates. The essay argues this isn't arbitrary -- it's building in the native dimensionality of human perception, using a principle that evolution and engineering discovered independently.

## Sources

| Section | Paper | Finding |
|---|---|---|
| Brain's RGB | Fudan University, PeerJ | 93.7% EEG decoding of R/G/B, sequential timing (R:190ms, G:215ms, B:238ms) |
| Dog's Computation | Nagaoka University, Frontiers in Physics | Three simultaneous nasal airflow routes via 3D X-ray CT |
| Color You Can't See | Stoddard et al., PNAS 2020 | Wild hummingbirds discriminate nonspectral UV+visible colors |
| What Engineers Found | Quanzhou Normal University | 60 Gbps via RGB wavelength division multiplexing over fiber |
| What I'm Building | Cottrell, VRGB Whitepaper | Hex colorspace as semantic coordinate system |

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

Copyright 2026 Nick Cottrell. All rights reserved.
