from random import *

print "Bienvenu chez Nath aleatoire : "


nbAleatoir = randint(0,9)

x = input("Devine le nombre :")


if (x == nbAleatoir):
	print("Bravo vous avez devine le nombre")
else:
	print("Vous avez perdu. Le nb aleatoire est : ", nbAleatoir) 



raw_input("appuyez sur une touche pour quitter...")
