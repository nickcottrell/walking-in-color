# Walking Through Color -- per-section VRGB steering coordinates
#
# Each section maps to a hex coordinate in RGB space.
# The arc traces a loop: warm/grounded -> biological spectrum ->
# engineering convergence -> speculative peak -> warm return.
#
# Coordinate rationale encoded in comments.
# Speculation ceiling: HIGH (global, per cue-vox session 2026-04-13)

COORDINATES = {
    # Opening: warm terracotta -- sodium streetlight, the walk, grounded in body
    # Low saturation, warm. The sidewalk before the ideas start.
    "s00_opening": {
        "hex": "#C4956A",
        "r": 196, "g": 149, "b": 106,
        "role": "anchor",
        "tension": 0.2,
        "speculation": 0.1,
    },

    # Part 1: The Brain's RGB -- red leads
    # Fudan timing data: red peaks first at 190ms. This section IS the red channel.
    # High red, restrained green/blue. The first concrete anchor.
    "s01_brains_rgb": {
        "hex": "#E04040",
        "r": 224, "g": 64, "b": 64,
        "role": "evidence",
        "tension": 0.5,
        "speculation": 0.2,
    },

    # Part 2: The Dog's Computation -- organic green
    # Biological, hedge-sniffing, living computation.
    # The extrapolation zone. Green with warmth underneath.
    "s02_dogs_computation": {
        "hex": "#6B8E6B",
        "r": 107, "g": 142, "b": 107,
        "role": "evidence",
        "tension": 0.6,
        "speculation": 0.4,
    },

    # Part 3: The Color You Can't See -- UV violet
    # The tetrachromatic dimension. The invisible channel.
    # Purple because it's reaching toward UV, the thing you can't perceive.
    "s03_color_you_cant_see": {
        "hex": "#7B3FA0",
        "r": 123, "g": 63, "b": 160,
        "role": "expansion",
        "tension": 0.7,
        "speculation": 0.5,
    },

    # Part 4: What the Engineers Found -- laser blue
    # 450nm channel, fiber optic, engineered precision.
    # Clean, high-saturation blue. Independent convergence.
    "s04_what_engineers_found": {
        "hex": "#3070C0",
        "r": 48, "g": 112, "b": 192,
        "role": "convergence",
        "tension": 0.8,
        "speculation": 0.3,
    },

    # Part 5: The Mantis Shrimp Problem -- amber
    # Categorical lookup, the tradeoff space. Neither warm nor cool.
    # This is the speculative peak. Amber = high energy, earned.
    # Hofstadter unit lives here.
    "s05_mantis_shrimp_problem": {
        "hex": "#D4A830",
        "r": 212, "g": 168, "b": 48,
        "role": "complication",
        "tension": 0.9,
        "speculation": 0.85,
    },

    # Part 6: What I'm Building -- deep indigo
    # Synthesis. The native-dimensionality claim. High density, low noise.
    # Dark because this is where the compression argument lives.
    "s06_what_im_building": {
        "hex": "#2E2E5E",
        "r": 46, "g": 46, "b": 94,
        "role": "synthesis",
        "tension": 0.7,
        "speculation": 0.7,
    },

    # Coda: return to sodium orange
    # Jack Jack at the door. The walk resolves.
    # Same warmth as opening but slightly different -- you've been changed by the walk.
    "s07_coda": {
        "hex": "#B8865A",
        "r": 184, "g": 134, "b": 90,
        "role": "anchor",
        "tension": 0.1,
        "speculation": 0.15,
    },
}

# Global calibration from cue-vox session 2026-04-13
CALIBRATION = {
    "speculation_ceiling": "high",
    "speculation_slider": 62,
    "completion": "very_low",
    "design_approved": True,
}


def get_coordinate(section_id):
    """Return the steering coordinate for a given section."""
    return COORDINATES.get(section_id)


def get_arc():
    """Return the full coordinate arc as an ordered list."""
    return [
        (k, v["hex"], v["tension"], v["speculation"])
        for k, v in COORDINATES.items()
    ]


if __name__ == "__main__":
    print("Walking Through Color -- Steering Coordinate Map")
    print("=" * 55)
    for section_id, coord in COORDINATES.items():
        print(
            "{:<30s} {} T:{:.1f} S:{:.1f}  {}".format(
                section_id,
                coord["hex"],
                coord["tension"],
                coord["speculation"],
                coord["role"],
            )
        )
