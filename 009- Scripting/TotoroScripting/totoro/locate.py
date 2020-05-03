
from totoro.display import Line, Column, Box, clock, hide_all, incr_clock
from totoro.utils import get_num_box, get_user_string_from_time,\
    get_time_from_user_string
import datetime
from totoro.spectrum import spectrum

from totoro.players import *
from totoro.tetris import Coeur, I, E, M, G, B, Te, Z, S, Carre, Barre, L
import random
def locate(resource):
    
    grid= resource.grid
    
    
    
    
    grid.auto_layout()
     
     
    grid.tag("initial")
    
  
    
    grid.set_num_box(13)
    grid.set_margin(20)
      
    clock("00:00:25:00")
    
    
    #tetris
    hide_all()
    grid.set_num_box(7)
    
    players = list(mus.values())
    
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
        (2,3, True),
        (4,3, True),
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
    
    
    last = Line([],2)
    remaining_players = last.fill(remaining_players)
    last.inside(grid).goto(0,4)
    last.goto(1,5,0.5)
    print(grid)
    last.goto(2,5,0.5)
    print(grid)
    
#     i = I()
#     i_players = list(mus.values())
#     i.inside(grid).move(1,5,4)
#     remaing_players =i.fill(i_players, 1)
#     
#     hide_all(remaing_players)
#     print(grid)
#     incr_clock(2)
#     
#     
#     coeur = Coeur()
#     coeur.inside(grid).prop_move(0,(13-9.1)/(2*13), 9.1/13) 
#     
#     coeur_players = list(mus.values())
#     random.shuffle(coeur_players)
#     
#     remaing_players =coeur.fill(coeur_players, 1)
#     hide_all(remaing_players)
#     print(grid)
#     
#     incr_clock(2)
#     
#     e = E()
#     e_players = list(mus.values())
#     random.shuffle(e_players)
#     e.inside(grid).move(1,5,5 ) 
#     remaing_players = e.fill(e_players, 1)
#     hide_all(remaing_players)
#     
#     incr_clock(2)
#     #hide_all(remaing_players)
#     
#     print(grid)
#     m_players = list(mus.values())
#     random.shuffle(e_players)
#     m = M()
#     m.inside(grid).move(1,4,7)
#     remaing_players=m.fill(m_players, 1) 
#     hide_all(remaing_players)
#     
#     incr_clock(2)
#     
#     
#     print(grid)
#     
#     g_players = list(mus.values())
#     random.shuffle(g_players)
#     g =G()
#     g.inside(grid).move(1,3.5,6)
#     remaing_players=g.fill(g_players, 1) 
#     hide_all(remaing_players)
#     incr_clock(2)
# 
#    
#     print(grid)
#     
#     b_players = list(mus.values())
#     random.shuffle(b_players)
#     #g_players.extend(m.get_players())
#     b =B()
#     b.inside(grid).move(1,3.5,6)
#     remaing_players=b.fill(b_players, 1) 
#     hide_all(remaing_players)
#     
#     incr_clock(2)
#     print(grid)
#     
#     
#     
#     coeur = Coeur()
#     coeur.inside(grid).move(5,5, 5)
#     
#     shuffled = all_players
#     random.shuffle(shuffled)
#     remaing_players =coeur.fill(shuffled, 1)
#     
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
     
    
    
    
    
