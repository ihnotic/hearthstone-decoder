# hearthstone-decoder
Python command line script to print out decklist based from deckid string input
## Requirements

* Python 2.7 or Python 3.4
* hearthstone python library (https://github.com/HearthSim/python-hearthstone)
* `pip install hearthstone`
* Other pip packages: enum34, requests

## Usage

From command line: `./hs-decoder.py <deckstring>`

## Example
```
$ ./hs-decoder.py AAECAa0GBgm0A6irAoW4Are7ApDTAgwelwKhBMkG0wrXCrW7Auq/AtHBAuXMArTOAvDPAgA=
PRIEST
FormatType.FT_STANDARD 
==============================
2x (1) Holy Smite
2x (1) Potion of Madness
2x (2) Mind Blast
2x (2) Shadow Visions
2x (2) Shadow Word: Pain
2x (2) Spirit Lash
2x (3) Shadow Word: Death
2x (3) Thoughtsteal
1x (4) Barnes
2x (4) Eternal Servitude
1x (4) Greater Healing Potion
2x (5) Holy Nova
2x (6) Dragonfire Potion
2x (6) Shadow Essence
1x (7) Prophet Velen
1x (8) Shadowreaper Anduin
1x (9) Malygos
1x (10) Y'Shaarj, Rage Unbound
==============================
Deckstring: AAECAa0GBgm0A6irAoW4Are7ApDTAgwelwKhBMkG0wrXCrW7Auq/AtHBAuXMArTOAvDPAgA=
```
