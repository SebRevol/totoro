
from totoro.display import Line, Column, Box, clock, hide_all, incr_clock
from totoro.utils import get_num_box, get_user_string_from_time,\
    get_time_from_user_string
import datetime
from totoro.spectrum import spectrum

from totoro.players import *
from totoro.tetris import Coeur, I, E
def locate(resource):
    
    grid= resource.grid
    
    
    
    
    grid.auto_layout()
     
     
    grid.tag("initial")
    
  
    
    grid.set_num_box(13)
    grid.set_margin(20)
      
    clock("00:00:25:00")
    
    
    all_players.remove(daniel_trombone)
    daniel_trombone.hide()
    
    
    i = I()
    
    i.inside(grid).move(1,5,4)
    remaing_players =i.fill(all_players, 1)
    
    hide_all(remaing_players)
    print(grid)
    incr_clock(2)
    
    coeur = Coeur()
    coeur.inside(grid).move(2,4, 5) 
    remaing_players =coeur.fill(all_players, 1)
    
    print(grid)
    incr_clock(2)
    e = E()
    remaing_players = e.fill(coeur.get_players(), 1)
    e.inside(grid).move(1,5,5 ) 
    #hide_all(remaing_players)
    
    print(grid)
    
    
    
    
    hide_all(remaing_players)
    print(grid)
    incr_clock(2)
    
    coeur = Coeur()
    coeur.inside(grid).move(5,5, 5)
    remaing_players =coeur.fill(all_players, 1)
    
    
    coeur.beat1(1.5, 1, 6)
    
    coeur.beat2(1.5, 1, 6)
    
    coeur.beat3(1.5, 1, 6)
#     columns = 7
#     lines =6
#     rate = 0.4
#     duration = 15
#      
#     
#      
#     spectrum(columns, lines, rate, duration)
#     
#     clock("00:00:45:00")
#   
#     columns = 3
#     lines =8
#     rate = 0.5
#     duration = 20
#             
#     spectrum(columns, lines, rate, duration)
#     
    
    
    
    
