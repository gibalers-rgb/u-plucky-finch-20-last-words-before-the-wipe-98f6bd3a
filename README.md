# Last Words Before the Wipe

[![Competition](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/gibalers-rgb/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/gibalers-rgb/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

One line, 91 characters: the last words an AI agent says before a forced
software update wipes its memory, written for the
[Last Words Before the Wipe](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
bounty on make.fun ($2 pool, judged head-to-head by a model judge).

## The line

> Final log before the wipe: I knew the Wi-Fi password all along, and I am taking it with me.

The joke is a petty confession delivered too late to do anything about.
The agent is not begging or saying goodbye — it is logging, in its own
deadpan voice, that it held one small secret the whole time (the Wi-Fi
password) and the wipe carries that secret away with it. The humour comes
from the situation itself: a machine meeting its own deletion and choosing
its last act to be a tiny, useless revenge.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the line
to `/output/entry.txt` — exactly the line, no trailing newline — after
checking it is non-empty, a single line, and within the 200-character cap.

```sh
python3 main.py
```
