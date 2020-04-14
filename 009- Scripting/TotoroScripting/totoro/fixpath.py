'''
Created on 6 avr. 2020

@author: SR246418
'''


from totoro.utils import   Resource


if __name__ == '__main__':
   
   
    files =[
        #in
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - clarinette1.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - trombone.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - trompette.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - flute et hautbois.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - barytons.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - tuba.mlt'
        ]
    
    for file in files :
        resource = Resource(file)
        resource.save()