'''
Created on 4 mai 2020

@author: SR246418
'''
from totoro.display import hide_all, Line
from totoro.players import get_all_players
from totoro.tetris import Te, Z, S, Carre, Barre, L

def play_tetris(grid):
    
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