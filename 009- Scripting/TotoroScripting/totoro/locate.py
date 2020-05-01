
from totoro.display import Line, Column, Box, clock
from totoro.utils import get_num_box, get_user_string_from_time,\
    get_time_from_user_string
import datetime
from totoro.spectrum import spectrum

from totoro.players import *
def locate(resource):
    
    grid= resource.grid
    
    
    
    
    grid.auto_layout()
     
     
    grid.tag("initial")
     
    
    grid.set_num_box(7)
    grid.set_margin(40)
      
    clock("00:00:30:00")
    columns = 7
    lines =6
    rate = 0.2
    duration = 15
     
    
     
    spectrum(columns, lines, rate, duration)
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
    
    
    
    
