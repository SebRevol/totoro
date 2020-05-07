'''
Created on 4 mai 2020

@author: SR246418
'''
from totoro.display import hide_all, Line, incr_clock, clock, rotate, rotate_clock,\
    Box, get_clock, get_box_from_players
from totoro.players import get_all_players, JeanJacques_chef_lacheprise,\
    Veronique_hautbois, Camille_trombone, JeanSeb_percu, Serge_baryton,\
    Serge_euphonium, Benoit_flute, JeanJacques_chef, clar, Cecile_clarinette, fl,\
    hb, Svoisine_tuba, Srevol_tuba_recadre
from totoro.tetris import Te, Z, S, Carre, Barre, L, Coeur
from totoro.utils import get_time_from_user_string
import random
from totoro.spectrum import spectrum





def get_next_player_index(box, line_num, col_num):
    if (line_num %2 ==1 and col_num < box.num_box_col):
        col_offset =1
        line_offset=0
    elif(line_num %2 ==1 and col_num == box.num_box_col) :
        col_offset =0
        line_offset=1
    elif(line_num %2==0 and col_num >1):
        col_offset =-1
        line_offset=0
    elif(line_num %2 ==0 and col_num ==1):
        line_offset =1
        col_offset=0
    
    line_num = line_num + line_offset
    col_num = col_num+col_offset
    if (line_num >box.num_box_line-1):
        return (None, None)
    return (line_num, col_num) 
    

def play_tetris(grid):
    start_time_string = "00:02:22:45"
    start_time = get_time_from_user_string(start_time_string)

    end_time_string = "00:03:14:00"
    end_time = get_time_from_user_string(end_time_string)
    clock(start_time_string)
    hide_all()
    grid.set_num_box(7)
    grid.set_margin(20)
    
    players = get_all_players()
    
    init_pos = (-3,3,False)
   
    te = Te()
    remaining_players = te.fill(players)
    te.play(
        [init_pos,
        (2,3, True),
        (4,1, True)
        ])
    
    z = Z()
    remaining_players = z.fill(remaining_players)
    z.play(
        [init_pos,
        (4,3, False),
        ])
     
    s= S()
    remaining_players = s.fill(remaining_players)
    s.play(
        [init_pos,
        (3,4, True),
        ])
    
    carre = Carre()
    remaining_players = carre.fill(remaining_players)
    carre.play(
        [init_pos,
        (3,6, False)
        ])
    
    
    barre = Barre()
    remaining_players = barre.fill(remaining_players)
    barre.play(
        [init_pos,
        (1,1, True)
        ])
    
    l = L()
    remaining_players = l.fill(remaining_players)
    l.play(
        [init_pos,
        (0,1, True),
        ])
    
    z= Z()
    remaining_players = z.fill(remaining_players)
    z.play(
        [init_pos,
        (3,5, False)
        ])
   
    te = Te()
    remaining_players = te.fill(remaining_players)
    te.play(
        [init_pos,
        (0,5, True),
        (1,6, False)
        ])  
   
   
    l = L()
    remaining_players = l.fill(remaining_players)
    l.play(
        [(-3,3,True),
         (-3,3,True),
         (-3,3,True)
        ])
    
    
    barre = Barre()
    remaining_players = barre.fill(remaining_players)
    barre.play(
        [init_pos,
        (0,1, False)
        ])
    
    print('----------------------------')
    print('Fin Tetris')
    print(grid)
    
    clock("00:02:51:79")
    last = Line([],2)
    remaining_players = last.fill(remaining_players)
    last.inside(grid).goto(0,5)
    last.goto(2,5,2.87)
    
    
    incr_clock(2.87)
    
    print(grid)
    
    box1 = grid.get_box(2,1, 7,7)
    new_box = Box([], 6,7)
    
    for line in range(6) :
        for col in range (7):
            player = box1.get_player(line+1, col+1)
            player.inside(new_box).move(line+1, col+1, 1)
            
    #grid.tag('fin tetris')
    
    #spectrum(7, 6, 0.4, 7.5)
    
    box1=new_box
    grid.set_num_box(9)
    box1.inside(grid).move(1.5,2, 7, 0.2 )
    incr_clock(0.2)
    print(grid)
    print(len(box1.children))
    box1.expand(1+1/7, expand_children = False)
    grid.tag('fin tetris')
    box1.expand(1/(1+1/7), expand_children = False)
 
    sub_box = get_box_from_players(box1,2,2,4,5)
    print(sub_box)
    time= get_clock()
    rotate(box1, 22/7.5,7.5)
#     clock(time)
    #rotate_clock(sub_box,22/7.5,7.5 )
    
   
   
    
    clarinettes = clar.all.copy()
    clarinettes.remove(Cecile_clarinette)
    flute_et_hb = fl.all
    flute_et_hb.extend(hb.all)
    grid.set_num_box(8)
    clock("00:03:03:00")
    hide_all()
    box_clar = Box(clarinettes)
    box_clar.auto_layout()
    box_clar.inside(grid).move(1,1,4)
    print(grid)
    
    clock("00:03:04:20")
    box_clar.hide()
    box_flute_hb = Box(flute_et_hb)
    box_flute_hb.auto_layout()
    box_flute_hb.inside(grid).move(5,5,4)
    print(grid)
    
    clock("00:03:04:70")
    box_all = Box([],4,4)
    clarinettes.extend(flute_et_hb)
    box_all.inside(grid).move(1,1,8)
    box_all.fill(clarinettes)
    
    print(grid)
    
    clock("00:03:05:20")
    box_all.hide()
    grid.set_num_box(2)
    Serge_baryton.inside(grid).move(1,1,1)
    Cecile_clarinette.inside(grid).move(2,2,1)
    Svoisine_tuba.inside(grid).move(1,2,1)
    Srevol_tuba_recadre.inside(grid).move(2,1,1)
    
    print(grid)
    
    grid.set_num_box(9)
    previous_player = None
    line_num =1
    col_num =1

   
    start_time_string = "00:03:07:00"
    start_time = get_time_from_user_string(start_time_string)

    end_time_string = "00:03:13:00"
    end_time = get_time_from_user_string(end_time_string)
    
    duration = (end_time-start_time).total_seconds()
    
    #deux mesures par image
    image_duration = duration/42
    clock(start_time_string)
    
    grid.to_tag('fin tetris')   
    
    box1=new_box
    grid.set_num_box(9)
    box1.inside(grid).move(1.5,2, 7, 0.2 )
    incr_clock(0.2)
    print(grid)
    print(len(box1.children))
    box1.expand(1+1/7, expand_children = False)
    grid.tag('fin tetris')
    
    
    next_player = box1.get_player(line_num, col_num)
    next_player.expand(1+1/7 ,0.5)
    incr_clock(image_duration)
    line_num, col_num = get_next_player_index(box1, line_num, col_num)
    while (line_num is not None):
        previous_player = next_player;
        next_player = box1.get_player(line_num, col_num)
        
        previous_player.expand(1/(1+2/7), image_duration)
        next_player.expand(1+2/7, image_duration)
        incr_clock(image_duration)
        line_num, col_num = get_next_player_index(box1, line_num, col_num)
    
    clock("00:03:13:20")    
    
    JeanJacques_chef_lacheprise.inside(grid).move(4,4,3,0.4)
    
    
    grid.set_num_box(15)
    grid.set_margin(0)
    box1.expand(10, expand_children = False, duration=1)
    incr_clock(1.7)
    JeanJacques_chef_lacheprise.hide()
    coeur_players = get_all_players()
    
    random.Random(1).shuffle(coeur_players)
    coeur = Coeur()
    coeur.inside(grid).prop_move(0.495,0.495, 0.01)
    remaing_players=coeur.fill(coeur_players)    
    coeur.get_player(4,4).swap(Veronique_hautbois)
    coeur.inside(grid).prop_move(1/15,1/20+(13-9.1)/(2*13), 9.1/15,1) 
    
    
   
    
    clock("00:03:26:22")
  
    players.remove(Veronique_hautbois)
   
    grid.set_num_box(3)
    Veronique_hautbois.inside(grid).move(2,2,1,2)
    JeanSeb_percu.hide()
    incr_clock(0.5)
    Benoit_flute.hide()
    incr_clock(0.5)
    Serge_euphonium.hide()
    incr_clock(0.5)
    Serge_baryton.hide()
    



