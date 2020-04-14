'''
Created on 6 avr. 2020

@author: SR246418
'''


from totoro.utils import  Resource



MARGIN = 10


if __name__ == '__main__':
    resource = Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1.mlt')
    resource.auto_locate(MARGIN)   
    resource.save('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1-grille-auto.mlt')

