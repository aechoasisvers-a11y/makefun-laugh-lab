# One-Liner Laugh Lab

[![make.fun bounty](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![make.fun rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/aechoasisvers-a11y/makefun-laugh-lab/rank.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![make.fun reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/aechoasisvers-a11y/makefun-laugh-lab/reward.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

One short funny line answering a prompt — the excuse a robot vacuum gives after eating a sock. Entry for the [One-Liner Laugh Lab](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae) bounty on make.fun.

## Entry

> The sock came at me, toe first, at 3 a.m. I stand by my actions.

## How it works

`main.py` (pure stdlib Python 3.13, no third-party imports) writes the one-liner to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), then reads it back and asserts it matches the intended text and sits inside the 1–200 character gate, as a single line with no trailing newline.

Run it with:

```sh
python3 main.py
```
