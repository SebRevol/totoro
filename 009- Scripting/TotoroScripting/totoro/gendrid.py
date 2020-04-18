'''
Created on 6 avr. 2020

@author: SR246418
'''
from totoro.model import Resource






if __name__ == '__main__':
    resource = Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1_pupitres incomplets.mlt')
    print(resource.players_registry)
    resource.locate()   
    resource.save('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1_pupitres incomplets-grille-manuelle.mlt')


        
    
