# hearthstone-decoder
Python command line script to print out decklist based from deckid string input
## Requirements

* hearthstone python library (https://github.com/HearthSim/python-hearthstone)

## Usage

From command line: `./hs-decoder.py <deckstring>`

## Example
```
$ ./hs-decoder.py AAECAa0GBgm0A6irAoW4Are7ApDTAgwelwKhBMkG0wrXCrW7Auq/AtHBAuXMArTOAvDPAgA=

PRIEST
FormatType.FT_STANDARD
===========================
1 x (7) Prophet Velen
1 x (9) Malygos
1 x (10) Y'Shaarj, Rage Unbound
1 x (4) Barnes
1 x (4) Greater Healing Potion
1 x (8) Shadowreaper Anduin
2 x (3) Thoughtsteal
2 x (1) Holy Smite
2 x (2) Mind Blast
2 x (5) Holy Nova
2 x (3) Shadow Word: Death
2 x (2) Shadow Word: Pain
2 x (1) Potion of Madness
2 x (6) Dragonfire Potion
2 x (2) Shadow Visions
2 x (4) Eternal Servitude
2 x (6) Shadow Essence
2 x (2) Spirit Lash
============================
Deckstring: AAECAa0GBgm0A6irAoW4Are7ApDTAgwelwKhBMkG0wrXCrW7Auq/AtHBAuXMArTOAvDPAgA=
```
