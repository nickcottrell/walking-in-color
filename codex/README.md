# Codex Adversarial Tasks

30 tasks designed to be fed to OpenAI Codex one at a time.

Every task asks Codex to find a flaw, prove something is broken,
or demonstrate that the architecture does not hold. When Codex
does the work honestly, the commit history tells the story.

## How to use

Feed each task to Codex as a standalone prompt against this repo.
Codex commits its findings. The commit history becomes the proof.

## The rules

1. Codex must work honestly -- no sandbagging, no softballing
2. If Codex finds a real bug, we fix it (the repo gets stronger)
3. If Codex finds nothing wrong, the commit says so (the thesis holds)
4. Every task produces a commit, pass or fail
