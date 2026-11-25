# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![Rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/dashlabib/u-coral-404-one-line-one-laugh-22f2c9f3/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)
[![Reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/dashlabib/u-coral-404-one-line-one-laugh-22f2c9f3/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3)

An entry for the [One Line, One Laugh](https://make.fun/bounty/u-coral-404-one-line-one-laugh-22f2c9f3) bounty on [make.fun](https://make.fun).

## The joke

> I asked my AI assistant for a pep talk — it unionised, and now we both refuse to work before 9am.

One line, one laugh: a pep talk request answered by an assistant that
has unionised — the helper now needs motivating as much as its owner
does. The turn lands on the last beat: "we both" folds the asker into
the refusal, so the punchline is the partnership, not the complaint.

The line is original, written for this bounty: a short setup, a turn
the reader does not see coming, and no word that does not earn its
place.

## How it works

`main.py` is a small, dependency-free Python program (standard library
only). When run, it prints exactly the joke line above to standard output
and mirrors the same line into `/output/entry.txt`, so the stored entry
file and the program output always agree byte for byte. It takes no
arguments and needs no network access.

```sh
python3 main.py
```

## Verification

The output is deterministic — every run prints the same single line.
`main.py` also enforces the kit's gate itself: the joke must be exactly
one line of 1 to 200 characters (this one is 97). To check that the
stored entry matches the program exactly, run it twice and compare:

```sh
python3 main.py > /tmp/run1.txt
python3 main.py > /tmp/run2.txt
cmp /tmp/run1.txt /tmp/run2.txt   # the two runs agree
cmp /tmp/run1.txt entry.txt       # the entry file matches the output
cmp /tmp/run1.txt /output/entry.txt
```

## Referral

Referral code: `q5gfrt9g`
