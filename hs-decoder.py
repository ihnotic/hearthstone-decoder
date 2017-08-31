#!/usr/bin/env python
import os
import json
import requests
import sys
from hearthstone.deckstrings import Deck

db_url = "https://api.hearthstonejson.com/v1/20457/enUS/cards.collectible.json"
db_path = "./db.json"
deckstring = sys.argv[1]
deck = Deck.from_deckstring(deckstring)
lb = "="*30
if os.path.exists(db_path):
    with open(db_path, "r") as f:
        db = json.loads(f.read())
else:
    response = requests.get(db_url)
    if response.status_code == 200:
        with open(db_path, "wb") as f:
            f.write(response.text.encode("utf-8"))
            db = response.json()
    else:
        raise RuntimeError("Couldn't download cards database: %s"
                           % response.text)
def get_card(dbf_id):
    return next((card for card in db if card["dbfId"] == dbf_id), None)
def sort_cards():
    cards = []
    for s in deck.cards:
        card = get_card(s[0])
        card["ammount"] = int(s[1])
        cards.append(card)
    cards = sorted(cards, key=lambda card:(card["cost"], card["name"]))
    return cards

print (get_card(deck.heroes[0])["cardClass"])
print ("%s \n%s" % (deck.format, lb))
for i in sort_cards():
    print ("%dx (%s) %s" % (i['ammount'], i['cost'], i['name']))
print ("%s\nDeckstring: %s" % (lb, deckstring))
