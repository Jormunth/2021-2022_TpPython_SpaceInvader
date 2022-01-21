# 2021-2022_TpPython_SpaceInvader
Augustin Laprais Alix Deleule

Ce programme permet d'executer le jeux Space Invader selon notre point de vue. Le but est de déplacer horizontalement grace au touche(qd ou ad) un vaisseau qui tire des missiles(avec la touche espace) et détruit des vaisseaux Alien pour obtenir le plus gros score. Le vaisseaux à 3 vie, il y a 2 types de vaisseaux Aliens (Alien strong en vert foncé et Alien weak en vert clair) les vaisseaux aliens se déplacent d'un bord à l'autre et avancent d'un cran vers le bas à chaque fois qu'ils rencontrent un bord de l'écran de jeux, les aliens weak tirent des missiles jaunes qui vont tout droit vers le bas de manière aléatoire, tandis que les aliens strong tirent des missiles roses qui suivent le vaisseaux du joueur et ils ont plus de vie(4). On déclenche la partie avec le bouton start et 5 aliens sont générés, puis des aliens strong et weak apparraissent un par un durant la partie jusqu'à ce que la partie soit finie. Des blocs bleu permettent de protéger le vaisseaux et se détruisent s'ils sont trop endommagé. On peut quitter le programme via le bouton quitter, le score et la vie du vaisseaux change en temps réel. De plus nous avons réalisé un cheat code qui détruit tout les vaisseaux alien si l'on appuie sur la touche "j".

On utilise une liste afin de stocker les aliens et ainsi parcourir cette liste afin de detecter une collision avec un missile. Cette liste est une attributs de la classe Game.

to do list: 
- changer les blocs carrés du vaisseau et des aliens par des images
- creer des niveaux de difficultés
- améliorer l'interface graphique
- optimiser le programme, en minimisant les fonctions update(ex: une seule fonction update appele en boucle)

lien git-hub:
https://github.com/Jormunth/2021-2022_TpPython_SpaceInvader