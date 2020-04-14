Pour que les scripts marchent, il faut installer python sur sa machine : https://www.python.org/downloads/

Ensuite :
-fixpath.bat :                      modifie le fichier "Orchestre dematerialisé - V1.mlt" pour rendre les chemins vers le vidéos relatifs. 
                                    Permet d'échanger le fichier .mtl d'une machine à l'autre

-fusionner.bat :                    fusionne les différents mlt. Le nom des fichiers à fusionner et du fichier résultant est à spécifier dans
                                    ./TotoroScripting/totoro/mergefiles.py  Une grille automatique est générée après la fusion.
                          
-gen_grille_auto.bat :              génère une grille par défaut, histoire d'avoir un rendu rapidement. 
                                    Le nombre de cases de la grille est toujours un carré (1/4/9/16 etc...), donc il se peut que des cases soit vides.
                                    Génère le fichier "Orchestre dematerialisé - V1-grille-auto.mlt"

-gen_grille_manuelle.bat:           génère une grille avec les informations de placement situées dans ./TotoroScripting/totoro/locate.py
                                    C'est ce fichier qu'il faut modifier pour définir manuellement un placement.
                         
-initialisation_script_manuel.bat:  génère un fichier "locate.py" par défaut à partir des vidéos importées dans le     "Orchestre dematerialisé - V1.mlt".
                                    Le résultat est dans ./TotoroScripting/totoro/locate_generated.py 
                                    ==> Ne pas modifier ce fichier, mais copier coller le contenu qui nous intéresse dans ./TotoroScripting/totoro/locate.py
                          
