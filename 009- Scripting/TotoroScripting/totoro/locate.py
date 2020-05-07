



from totoro.players import *
from totoro.i_love_emgb import i_love_emgb
from totoro import locate_camille
from totoro.play_tetris import play_tetris

def locate(resource):
    locate_camille.locate(resource)
    grid= resource.grid
    
    
    i_love_emgb(grid)
    play_tetris(grid)
    
    #resource.cut ("00:03:00:00",  "00:03:41:00") 
     
    
    #resource.cut ("00:01:53:62","00:03:41:00")
    #resource.cut ("00:02:51:79","00:03:03:00")
    
    
      
   
    
    
   
  
    
    
    
    
    
    
    
    
    

     
#     
#     coeur.beat1(1.5, 1, 6)
#     
#     coeur.beat2(1.5, 1, 6)
#     
#     coeur.beat3(1.5, 1, 6)
#     
#     hide_all()
    
#     clock("00:01:10:00")
#     grid.set_num_box(7)
#     columns = 7
#     lines =6
#     rate = 0.4
#     duration = 15
#        
#       
#        
#     spectrum(columns, lines, rate, duration)
#       
#     clock("00:01:30:00")
#     
#     columns = 7
#     lines =6
#     rate = 0.5
#     duration = 20
#               
#     spectrum(columns, lines, rate, duration)
     
    
    
    
    
