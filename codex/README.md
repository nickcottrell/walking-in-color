# Codex Adversarial Backlog

Open backlog of tasks designed to be fed to OpenAI Codex in waves.

Every task asks Codex to find a flaw, prove something is broken,
or demonstrate that the architecture does not hold. When Codex
does the work honestly, the commit history tells the story.

## Waves

Tasks are batched in waves of 10. Each wave targets a specific unknown.
Wave N+1 is shaped by Wave N results. New tasks can be added between waves.

- **Wave 1: Does the pipeline actually work?** -- Mechanical verification
- **Wave 2: Does the voice filter preserve the argument?** -- Semantic verification
- **Wave 3: Is the thesis itself defensible?** -- Intellectual verification

## How to use

Feed one wave at a time to Codex against this repo. Wait for results.
Review findings. Decide what the next unknown is. Revise wave N+1 if needed.
Add new tasks to the backlog as they emerge.

## The rules

1. Codex must work honestly -- no sandbagging, no softballing
2. If Codex finds a real bug, we fix it (the repo gets stronger)
3. If Codex finds nothing wrong, the commit says so (the thesis holds)
4. Every task produces a commit, pass or fail
5. The backlog is always open -- this is progressive and always revisable
