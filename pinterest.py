import pprint
from pinata.client import PinterestPinata

pinata = PinterestPinata(email='royyurusravani@gmail.com', password='satyavani1996', username='sravaniroyyuru')
boards = pinata.search_boards('cats')
pprint.pprint(boards)
#a=pinterest.auth pinata
#auth=pinterest.OAuthHandler('4869303750828763830')
#auth.set_access_token('cb1a4d9d657519dc7a03c8c1698353ac0b0c7a531433e9a0d66cd652e991b7ee')

#pinterest_api = pinterest.API(auth)

#glitter_pins = pinterest_api.search(
#    q="glitter beards"
#)
#for pin in glitter_pins:
 #   pprint.pprint(pin.user.name + ": " + pin.text)