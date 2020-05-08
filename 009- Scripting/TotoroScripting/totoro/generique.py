'''
Created on 6 avr. 2020

@author: SR246418
'''
from totoro.model import Resource

from totoro.utils import get_time_from_user_string, get_user_string_from_time
from totoro.display import clock, incr_clock, hide_all
import datetime
from totoro.tetris import L_inverse, L, S, Te, Z, Carre

def get_cell_position(ratio, column):
    line = 1.5
    x = (column-1)/3
    y= (line-1)/3
    
    size = 0.4
    
    new_size = ratio*size
 
    rel_x = x+(size/2)*(1-ratio)
    rel_y = y+(size/2)*(1-ratio)
         
    return (rel_y, rel_x, new_size)





def defile_3_blocks():
    
    minus_1 = None
    one = None
    center = None
    two = None
    plus_1 = None
    
    
    size = len(blocks)
    for index in range (size+4) :
        if (index < size):
            minus_1 = blocks[index]
        else :
            minus_1 = None
        if (index >0 and index < size+1):
            one = blocks[index-1]
        else :
            one = None
        if (index >1 and  index < size+2):
            center = blocks[index-2]
        else:
            center = None
        if (index >2 and index < size +3):
            two = blocks[index-3]
        else :
            two = None
            
        if (index >3):
            plus_1 = blocks[index-4]
        else :
            plus_1 =None
        
        if (minus_1 is not None):
            minus_1.inside(grid).prop_move(*get_cell_position(0.6,4))
            
        
        if (one is not None):
            one.inside(grid).prop_move(*get_cell_position(0.6,3),shift_duration)
         

        if (center is not None ):
            center.inside(grid).prop_move(*get_cell_position(1.2,2),shift_duration)
            #center.expand(1/0.6, shift_duration)
        
        if (two is not None):
            two.inside(grid).prop_move(*get_cell_position(0.6,1),shift_duration)
        
        if (plus_1 is not None):
            plus_1.inside(grid).prop_move(*get_cell_position(0.6,0),shift_duration)
            
        if (index > 0):
            incr_clock(2*shift_duration)
        
        else : 
            incr_clock(shift_duration)
        
#         if (one is not None):
#             one.switch()
#         if (center is not None):
#             center.switch()
#         if (two is not None):
#             two.switch()
            
        print(grid)


if __name__ == '__main__':
    resource = Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1_pupitres incomplets.mlt')


    from totoro.players import get_all_players, Bidou_cornet, Serge_trompette,\
        Camille_trombone, Srevol_tuba_recadre, JeanJacques_chef,\
        JeanJacques_chef_lacheprise

    grid = resource.grid
    grid.set_num_box(3)
    hide_all()
    all_players = get_all_players()
    all_players.remove(Bidou_cornet)
    all_players.remove(Serge_trompette)
    all_players.remove(Camille_trombone)
    all_players.remove(Srevol_tuba_recadre)
    all_players.append(JeanJacques_chef_lacheprise)
    
    block_classes = [Te,L_inverse, Z, L, S]
    blocks = []
    for index in range(10):
        block = block_classes[index % len(block_classes)]()
        block.inside(grid).move(-1,-1,1)
        
        all_players = block.fill(all_players)
        blocks.append(block)
        
    
    print(len(all_players))
    
    
    t_start_string ="00:02:20:00"
    
    duration = 55.416
    
    t_end  =  get_time_from_user_string(t_start_string) + datetime.timedelta(seconds = duration)
    t_end_string = get_user_string_from_time(t_end)
    
    
    shift_duration = duration /(2*(len(blocks)+4))
    
    clock(t_start_string)
    
    defile_3_blocks()
    
    resource.cut(t_start_string, t_end_string)
    
    resource.save('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Generique.mlt')
    
    
def defile_simple_block():
    grid.set_margin(20)
    grid.set_num_box(5)
    y=2 
    for block in blocks :
        block.move()
        

    
    


        
    
