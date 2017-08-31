#!/usr/bin/env python
import os
import json
import requests
import sys
import requests
from hearthstone.deckstrings import Deck

deckstring = sys.argv[1]
db_url = "https://api.hearthstonejson.com/v1/20457/enUS/cards.collectible.json"
db_path = "./db.json"
lb = "="*30
if os.path.exists(db_path):
    with open(db_path, "r") as f:
        db = json.loads(f.read())
else:
    response = requests.get(db_url)
    if response.status_code == 200:
        with open(db_path, "w") as f:
            f.write(response.text.encode("utf-8"))
            db = response.json()
    else:
        raise RuntimeError("Couldn't download cards database: %s"
                           % response.text)

def get_card(dbf_id):
    return next(card for card in db if card["dbfId"] == dbf_id)
def format_card(card):
    return "(%d) %s" % (card["cost"], card["name"])
deck = Deck.from_deckstring(deckstring)
print (get_card(deck.heroes[0])["cardClass"])
print ("%s \n%s" % (deck.format, lb))
for s in deck.cards:
    print ("%dx %s" % (s[1], format_card(get_card(s[0]))))
print ("%s \nDeckstring: %s:" % (lb, deckstring))

