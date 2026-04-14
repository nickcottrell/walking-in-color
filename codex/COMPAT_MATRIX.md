# Model Compatibility Matrix

Same steering coordinates. Same voice filters. Different models.
Think browser compat testing circa 2012.

## Backends

| Backend | Model | Tier | API | Cost/build | Determinism |
|---|---|---|---|---|---|
| ollama | Qwen 2.5 7B Q4_K_M | baseline | local | free | bit-identical (CPU) |
| openai | gpt-4o-mini | baseline | OpenAI | ~$0.01 | seed-based |
| openai-4o | gpt-4o | stretch | OpenAI | ~$0.25 | seed-based |
| anthropic | claude-sonnet-4-6 | stretch | Anthropic | ~$0.10 | temp=0 |

## Test Matrix

For each backend, run:

1. **Verbatim fidelity** -- does the model reproduce the source exactly?
2. **Voice filter (pirate)** -- does the pirate voice preserve all facts?
3. **Voice filter (morse)** -- does maximum compression preserve the argument?
4. **Determinism** -- do two runs produce the same output?
5. **Section structure** -- do all 7 markers appear in order?

```
python3 build.py --backend ollama --voice pirate --out generations/pirate-ollama.md
python3 build.py --backend openai --voice pirate --out generations/pirate-openai.md
python3 build.py --backend openai-4o --voice pirate --out generations/pirate-4o.md
python3 build.py --backend anthropic --voice pirate --out generations/pirate-anthropic.md
```

## Reporting

Results go in codex/reports/ with the naming convention:

```
compat-{backend}-{voice}-{date}.md
```

## What We Are Testing

The steering coordinates claim to be model-independent. If the same
hex coordinates, tension values, and speculation ceilings produce
coherent output across Qwen, GPT-4o-mini, GPT-4o, and Claude --
four different architectures, four different training sets, four
different compression strategies -- then the coordinates are
encoding something real about the structure of the argument,
not something specific to one model's embedding space.

If a model breaks, that is also data. The compat matrix tells you
where the architecture's assumptions stop holding.

## Tier Definitions

**Baseline** -- run these on every wave. Cheap enough to burn.
Codex uses openai by default. Local development uses ollama.

**Stretch** -- run these when baseline passes and you want to
know if higher-resolution models produce qualitatively different
output. These cost more. Use them deliberately, not routinely.
