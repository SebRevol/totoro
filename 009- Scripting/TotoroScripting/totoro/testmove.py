'''
Created on 6 avr. 2020

@author: SR246418
'''
from totoro.utils import  zero_time, get_user_string_from_time
import datetime
from totoro.model import Resource






if __name__ == '__main__':
    resource = Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/TestDecoupe.mlt')
    
    resource.grid.set_num_box(5)
    resource.grid.set_margin(0)
    
   
    bidou = resource.players_registry['Bidou_euphonium_totoro']
    for second in range(25) :
        time = zero_time + datetime.timedelta(seconds = 0.5*second)
        time_string = get_user_string_from_time(time)     
        col =int(second/5)
        line = second % 5
        
        bidou.on(time_string).move(line+1,col+1,1, 0.5)
    
    t2 = zero_time + datetime.timedelta(seconds = 0.5*25)
    
    
    for index in range (3) :
        time = t2 + datetime.timedelta(seconds = 2*index)
        time_string = get_user_string_from_time(time)     
      
        bidou.on(time_string).move(3-index,3-index,3+index,1)
        
    bidou.on("00:02:00:00").hide()
    
    bidou.on("00:02:02:00").show()
    
    bidou.on("00:02:10:00").move(1, 2.5, 2.5,3)
      
    bidou.on("00:02:15:00").prop_move(1/3,1/3,2/3,3)
    
    
    
    print(resource.players_registry)
    resource.save('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/TestDecoupe-moved.mlt')


        
    
