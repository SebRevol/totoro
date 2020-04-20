'''
Created on 6 avr. 2020

@author: SR246418
'''
from totoro.model import merge_files



if __name__ == '__main__':

    # changer ici les chemin des fichiers à fusionner, rajouter autant de lignes que de fichiers
    merge_files([
        # in
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - percussion.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - barytons.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - clarinette1.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - cor.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - flute et hautbois.mlt',
	    '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - saxophone.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - trombone.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - trompette.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - tuba.mlt'
        ],
        # out
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1_pupitres incomplets.mlt'
    )
