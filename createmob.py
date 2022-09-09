from genMob import *
from random import choice

def createMob():
   monsterlist = ["pikachu", "bulbizarre", "salamèche","carapuce", "Rondoudou"]
   nommonstre = choice(monsterlist)
   
   return genMob(nommonstre)
