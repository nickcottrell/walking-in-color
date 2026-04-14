# Codex Environment Setup

## Backend

This repo supports two model backends. Codex should use the OpenAI backend:

```
export WALKING_BACKEND=openai
export OPENAI_API_KEY=sk-...
```

Then all build.py commands route to gpt-4o-mini instead of local Ollama.

## Model Equivalence

| Property | Local (Ollama) | Cloud (OpenAI) |
|---|---|---|
| Model | Qwen 2.5 7B Instruct Q4_K_M | gpt-4o-mini |
| Parameters | ~7B | undisclosed |
| Quantization | 4-bit (Q4_K_M) | API-served |
| Determinism | seed=42, temp=0, top_k=1, CPU | seed=42, temp=0 |
| Cost | free (local) | ~$0.01 per full essay build |

Using a different model is a feature, not a limitation. If the steering
coordinates produce coherent output across two completely different
architectures (Qwen and GPT), that is stronger evidence than testing
on the same model twice.

## Running tasks

```
# Voice filter test
python3 build.py --backend openai --voice pirate --out generations/pirate-openai.md

# Verbatim test
python3 build.py --backend openai --out generations/verbatim-openai.md

# Determinism test (run twice, compare)
python3 build.py --backend openai --voice pirate --out /tmp/run1.md
python3 build.py --backend openai --voice pirate --out /tmp/run2.md
diff /tmp/run1.md /tmp/run2.md

# Verify (no model needed)
python3 build.py --verify
```

## Determinism note

OpenAI documents seed-based determinism as "mostly deterministic" --
not bit-identical like CPU Ollama. If determinism tests show small
variations on the OpenAI backend, that is an expected difference
between backends, not a pipeline failure. Report both the hash
comparison AND whether the semantic content is identical.
