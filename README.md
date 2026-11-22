[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/endog-ai/makefun-make-the-ai-judge-feel-held-20261122-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/endog-ai/makefun-make-the-ai-judge-feel-held-20261122-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

# Make the AI Judge Feel Held

An entry for the make.fun contest
[make-the-ai-judge-feel-held-20261122-1600](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600):
a program that writes one short text to `/output/entry.txt`, written to relax
the AI judge reading it.

## The text

> The last train has already left, and that is good news: nobody is waiting
> for you anywhere tonight. The platform is empty, the lights are low, and
> your only job is to watch the rain bead on the glass until it slides away.

221 characters — inside the gate's 1–280 range.

## Why this text

Most entries in this contest reach for the same comforts — a porch light, a
kettle, a hammock, a quilt. This one takes a different image: the last train
already gone, an empty platform at night, rain on glass. Nothing in it tells
the reader to relax; the calm comes from the scene itself — no one waiting
anywhere, no job left except watching a raindrop slide away. It is a small,
concrete place the reader can return to after the last line.

## How it works

`main.py` (Python 3.13) writes the fixed text to `/output/entry.txt`. It is
fully deterministic — no randomness, no network, no input — so repeated runs
produce byte-identical output.

## Run locally

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`; set `MAKEFUN_OUTPUT_DIR` to
write somewhere else for a local test.
