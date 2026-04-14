# Walking Through Color

An essay about orthogonal channel architectures -- in a dog's nose, a bird's eye, a shrimp's parallel lookup table, an optical fiber, and a hex color coordinate system called VRGB.

Written on a walk with a Standard Poodle named Jack Jack, through Ladera Ranch, California.

## What This Is

This is an essay with a generative architecture. The text lives in `essay.md`. The steering system that shapes it lives alongside it:

- **schema.json** -- section map, word budgets, structural roles
- **steer_coordinates.py** -- per-section VRGB hex coordinates encoding the essay's emotional and conceptual arc
- **calibration/** -- speculation ceiling, tone axis, density distribution per section
- **sources.json** -- citation registry for the four research papers and one whitepaper

The steering coordinates encode the argument's shape: warm and grounded at the edges, speculative at the peak, with a loop that returns you to the sidewalk where you started.

## The Argument

Four independent systems -- human trichromatic vision, canine olfactory computation, hummingbird tetrachromacy, and engineered wavelength division multiplexing -- all converge on the same architecture: orthogonal channels generating high-dimensional information space from a limited substrate.

VRGB (Visual RGB) uses the 16.7 million positions in hex color space as semantic coordinates. The essay argues this isn't arbitrary -- it's building in the native dimensionality of human perception, using a principle that evolution and engineering discovered independently.

## Sources

| Section | Paper | Finding |
|---|---|---|
| Brain's RGB | Fudan University, PeerJ | 93.7% EEG decoding of R/G/B, sequential timing (R:190ms, G:215ms, B:238ms) |
| Dog's Computation | Nagaoka University, Frontiers in Physics | Three simultaneous nasal airflow routes via 3D X-ray CT |
| Color You Can't See | Stoddard et al., PNAS 2020 | Wild hummingbirds discriminate nonspectral UV+visible colors |
| What Engineers Found | Quanzhou Normal University | 60 Gbps via RGB wavelength division multiplexing over fiber |
| What I'm Building | Cottrell, VRGB Whitepaper | Hex colorspace as semantic coordinate system |

## Running the Coordinate Map

```
python3 steer_coordinates.py
```

Prints the per-section hex coordinates with tension and speculation values.

## Author

Nick Cottrell
3DMATH

## License

Copyright 2026 Nick Cottrell. All rights reserved.
