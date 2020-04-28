'''
Created on 6 avr. 2020

@author: SR246418
'''
from totoro.utils import  zero_time, get_user_string_from_time
import datetime
from totoro.model import Resource
from totoro.display import clock, Line






if __name__ == '__main__':
    #resource = Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/TestDecoupe.mlt')
    resource = Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/clarinette1-test.mlt')
    
    resource.grid.set_num_box(8)
    resource.grid.set_margin(0)
    
    
   
   
    
    line = Line(resource.players_registry.values())

    line.inside(resource.grid).move(1,1,3)
    clock('00:01:00:00')
    
    line.move(1,6,3,10)
    
    
    clock('00:01:10:00')
    line.move(1,1,3,10)
   
    clock('00:01:20:00')
    line.move(8,1,3,10)
   
   
    resource.save('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/clarinette-moved.mlt')


        
    
