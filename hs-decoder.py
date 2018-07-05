#!/usr/bin/env python
import os
import sys
import json
import requests
import base64
import argparse
from hearthstone.deckstrings import Deck

def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return data
def get_format():
    if int(deck.format) == 2:return "STANDARD"
    else:return "WILD"
def get_card(dbf_id):
    return next((card for card in db if card["dbfId"] == dbf_id), None)
def sort_cards():
    cards = []
    for s in deck.cards:
        card = get_card(s[0])
        card["ammount"] = int(s[1])
        cards.append(card)
    return sorted(cards, key=lambda card:(card["cost"], card["cardClass"], card["name"]))
parser = argparse.ArgumentParser(description="Print hearthstone decklist to terminal from deckid")
parser.add_argument('<deckid>', type=str, help='Hearthstone deckID to be converted')
args = parser.parse_args()

db_url = "https://api.hearthstonejson.com/v1/24769/enUS/cards.collectible.json"
db_path = "./db.json"
deckstring = decode_base64(sys.argv[1])
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
print (get_card(deck.heroes[0])["cardClass"])
print (get_format())
print (lb)
for i in sort_cards():
    print ("%dx (%s) %s" % (i["ammount"], i["cost"], i["name"]))
print (lb)
print ("Deckstring: %s" % (deckstring))
