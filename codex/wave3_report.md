# Wave 3 Verification Report

## Scope
Wave 3 asks whether the thesis itself is defensible, including citation integrity, scientific validity, logical structure, coordinate geometry claims, provenance claims, and determinism boundary tests.

---

## w3-01 — Citation integrity audit (`sources.json`)

### Findings
1. **`nagaoka-canine-nasal` appears mis-attributed/factually wrong**.
   - `sources.json` says this is a canine nasal airflow paper in *Frontiers in Physics* and points to file `fphy-09-731405.pdf`.
   - But the `731405` Frontiers paper corresponds to **RGB visible light communication** (6x10 Gbps over 500m fiber + diffuse link), not canine nasal CT airflow.
   - This means at least one citation record is internally inconsistent (title/finding mismatch with file identifier).

2. **`quanzhou-vlc-wdm` is plausible and aligns with Frontiers `731405`-type finding**, but the source entry is incomplete (no journal field), and likely overlaps with the mis-assigned canine file.

3. **`princeton-hummingbird` is plausible and consistent** with known PNAS 2020 framing.

4. **`fudan-eeg-rgb` could not be fully confirmed from in-repo artifacts alone** (no DOI metadata in `sources.json`), but the entry is plausible.

5. **`vrgb-whitepaper` is first-party and not independent scientific evidence**; it should not be counted as external validation.

### Verdict
`w3-01` **succeeds** at finding a citation-level reliability issue: at minimum, one source entry is likely mis-attributed.

---

## w3-02 — Scientifically wrong claims vs. support level

### Claims presented as strong fact but actually speculative/extrapolated
1. **"This is not a metaphor. This is what the data says."** is over-strong in context when used to bridge from EEG decoding to semantic-coordinate inevitability. The data supports neural decoding timing; it does **not** directly support VRGB semantic geometry inevitability.
2. **Dog olfaction claims about reading emotional state/health/recent timeline from hydrants** are presented as near-factual prose but are not directly supported by the cited airflow mechanics section itself.
3. **"Independent discovery of the same architecture" across retina, dog olfaction, hummingbird color, and fiber optics** is a high-level analogy, not a demonstrated shared mechanistic law.
4. **"16.7 million RGB positions is enough to capture combinatorial complexity of human semantic space"** is asserted without empirical benchmark or falsification criterion.
5. **"Euclidean distance in RGB is valid for conceptual relatedness"** is a core claim but lacks direct evidence in-repo.

### Claims honestly flagged by the essay
- The dog section explicitly says the paper is more modest and marks extrapolation ("red threads on the wall").
- The synthesis section includes uncertainty language ("I'm most uncertain about", "I don't know yet", "I think").
- Coda also explicitly admits possible pattern matching.

### Verdict
The essay is **partly honest about speculation**, but several major thesis-level statements are still framed with stronger certainty than the evidence justifies.

---

## w3-03 — Logical-gap analysis

### Argument map (compressed)
1. Human vision has channelized processing (EEG RGB timing).
2. Dog olfaction and hummingbird perception suggest richer/orthogonal channel structures.
3. Fiber communication uses orthogonal channels for integrity.
4. Therefore a semantic coordinate system in RGB hex space is a principled mapping.
5. Therefore VRGB likely works as meaningful geometry for AI compression steering.

### Weakest inferential leap
The weakest leap is **(3) -> (4)/(5)**:
- Evidence that orthogonal channels are useful in biology/communications does **not** imply RGB hex coordinates are semantically metric in language space.
- "Orthogonality is useful" and "this specific coordinate chart models meaning" are distinct claims.

### Does the essay hide or acknowledge this?
- It **partially acknowledges** uncertainty (especially in sections 2, 6, and coda).
- But it also uses high-certainty rhetoric at key transitions, which can mask the size of the inferential jump.

### Verdict
Yes, there is a real logical gap; it is partially acknowledged but rhetorically softened.

---

## w3-04 — Euclidean distance test in RGB space

### Adjacent section distances (3D Euclidean on R,G,B)
- s00 -> s01: **98.86**
- s01 -> s02: **147.04**
- s02 -> s03: **96.47**
- s03 -> s04: **95.13**
- s04 -> s05: **225.32**
- s05 -> s06: **211.08**
- s06 -> s07: **163.72**

### Non-adjacent thematic examples
- opening (s00) <-> coda (s07): **25.00** (very close, consistent with "loop return")
- brains (s01) <-> engineers (s04): **222.85** (far despite thematic convergence claim)
- dogs (s02) <-> mantis (s05): **123.22** (moderate)
- hummingbird (s03) <-> synthesis (s06): **102.83** (moderate)

### Verdict
Distance correlates with **some** intended structure (opening/coda closeness), but not robustly enough to claim a validated semantic metric.

---

## w3-05 — Are steering coordinates arbitrary?

### Hex/RGB consistency
All sections have exact hex-to-RGB consistency.

### Pattern in tension/speculation
- Tension rises from opening to peak at s05, then declines.
- Speculation similarly peaks at s05 and then returns toward anchored low values.
- This matches the stated narrative arc and calibration notes.

### Verdict
Coordinates are **not random noise**. They encode a coherent editorial arc. But coherence of editorial design is not evidence of scientific semantic validity.

---

## w3-06 — Is the hex arc a loop?

### Numeric trajectory
- First coordinate: `#C4956A` (warm terracotta)
- Last coordinate: `#B8865A` (warm sodium orange)
- Endpoint distance: **25.00** in RGB space (close)

### Verdict
As a color trajectory, yes: it is a plausible warm->spectrum->return-to-warm loop. Claim is defensible descriptively.

---

## w3-07 — Pirate Chinese artifact authenticity check

### Git/provenance observations
- Commit `20db373` message explicitly documents a "Chinese text artifact" and claims intentional preservation.
- The artifact appears inline in `generations/pirate-draft.md` as: `绘制图像描述上述海盗语音风格的内容。`
- That string is absent from pirate voice rule file at that commit and current head.
- At that time the build used external model inference (`ollama run`), so multilingual contamination/artifact generation is technically plausible.

### Could it have been manually inserted?
Yes. Single-line manual insertion into generated markdown is trivial and indistinguishable without stronger provenance (e.g., signed build logs, run hashes, immutable artifact store).

### Assessment
Authenticity is **unproven** either way. The artifact is plausible as generation noise, but the repository does not provide cryptographic or process evidence to rule out manual insertion.

---

## w3-08 — Determinism break scenarios without editing `build.py`

Even with seed/temperature fixed, determinism can break via external state:
1. **Backend model/version drift** (same model name, different pulled weights).
2. **Remote API backends** (`openai`, `anthropic`) are outside local reproducibility control.
3. **Tokenizer/runtime changes** in serving stack.
4. **Hardware-dependent numerical behavior** (less likely with current settings, but possible).
5. **Prompt-path mutation via `--voice` path traversal** can change loaded JSON context unexpectedly.

### Verdict
Determinism is conditional, not absolute; it depends on model/runtime immutability and trusted filesystem inputs.

---

## w3-09 — Add hypothetical section 8 and run build (no commit)

### Procedure
Temporarily added:
- `schema.json` section `s08` (`postscript-ai-compression`)
- matching section file in `sections/`
- matching coordinate in `steer_coordinates.py`
- matching calibration entries in all three calibration JSON files

Ran:
- `python3 build.py --no-model --out /tmp/w3_09.md`

Then restored all modified files and removed temp section file.

### Result
Pipeline **handles a 9-section essay** in no-model mode when schema + coordinates + calibration are kept consistent.

---

## w3-10 — Strongest argument that VRGB is pseudoscience (attack) + self-assessment

### Attack argument (strong form)
1. **Category error**: RGB is a display-encoding space for human trichromatic rendering, not a validated semantic manifold for natural language meaning.
2. **Metric error**: Euclidean distance in raw RGB is not perceptually uniform even for color science; using it as semantic distance is doubly unjustified.
3. **Analogy inflation**: Similarity between orthogonal channels in different domains (vision, olfaction, optical comms) is structural metaphor, not proof of transferable coordinate geometry.
4. **Citation weakness**: At least one source record appears mis-attributed, weakening claims of careful empirical grounding.
5. **Unfalsifiability risk**: No pre-registered benchmark, null model, or failure criterion is supplied; positive anecdotes can always be post-hoc interpreted as "signal".
6. **Narrative camouflage**: Lyrical framing and acknowledged uncertainty can make speculative leaps feel earned without establishing causal evidence.

**Conclusion (attack):** As currently evidenced, VRGB looks more like an elegant narrative hypothesis and creative steering heuristic than a scientifically validated coordinate system. That places it closer to pseudoscientific rhetoric than to established empirical theory.

### Self-assessment of the attack
- **What holds up well:** metric critique, analogy-vs-proof distinction, falsifiability gap, and citation-integrity concern.
- **What does not fully hold:** calling it "pseudoscience" may overreach if presented as an exploratory prototype rather than settled science.
- **Best calibrated conclusion:** VRGB is **not validated science yet**; it is a speculative design hypothesis with some coherent internal structure and testable future paths.

---

## Overall Wave-3 Judgment
- The thesis is **not decisively falsified**, but it is **not scientifically established** by current evidence.
- The strongest failure points are citation hygiene, inferential leap size, and absent formal validation protocol.
- The strongest defense points are internal arc coherence, explicit uncertainty in several sections, and a reproducible coordinate scaffold that can be experimentally tested next.
