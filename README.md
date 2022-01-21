# 2021-2022_TpPython_SpaceInvader
Augustin Laprais Alix Deleule

Ce programme permet d'executer le jeux Space Invader selon notre point de vue. Le but est de déplacer horizontalement un vaisseau qui tire des missiles et détruit des vaisseaux Alien pour obtenir le plus gros score. Le vaisseaux à 3 vie, il y a 2 types de vaisseaux Aliens (Alien strong en vert foncé et Alien weak en vert clair) les vaisseaux aliens se déplacent d'un bord à l'autre et avancent d'un cran vers le bas à chaque fois qu'ils rencontrent un bord de l'écran de jeux, les aliens weak tirent des missiles jaunes qui vont tout droit vers le bas de manière aléatoire, tandis que les aliens strong tirent des missiles roses qui suivent le vaisseaux du joueur et ils ont plus de vie(4). On déclenche la partie avec le bouton start et 5 aliens sont générés, puis des aliens strong et weak apparraissent un par un durant la partie jusqu'à ce que la partie soit finie. Des blocs bleu permettent de protéger le vaisseaux et se détruisent s'ils sont trop endommagé. On peut quitter le programme via le bouton quitter, le score et la vie du vaisseaux change en temps réel.

On utilise une liste afin de stocker les aliens et ainsi parcourir cette liste afin de detecter une collision avec un missile. Cette liste est une attributs de la classe Game.

