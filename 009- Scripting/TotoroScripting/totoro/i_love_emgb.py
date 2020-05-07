'''
Created on 4 mai 2020

@author: SR246418
'''
from totoro.utils import get_time_from_user_string
from totoro.display import clock, hide_all, incr_clock
from totoro.tetris import I, Coeur, E, M, G, B
from totoro.players import get_all_players, Natacha_clarinette, JeanJacques_chef
import random


start_time_string = "00:01:58:62"
start_time = get_time_from_user_string(start_time_string)

end_time_string = "00:02:17:80"
end_time = get_time_from_user_string(end_time_string)

def i_love_emgb(grid):
    
    grid.set_num_box(15)
    grid.set_margin(20)
    
    hide_all()
   
    nb_mesure = 12
    duration = (end_time-start_time).total_seconds()
    
    #deux mesures par image
    image_duration = 2*duration /nb_mesure
    temps_duration = duration/(4*nb_mesure)
    clock(start_time_string)
    
    ######### I #################
    
    i = I()
    i_players = get_all_players()
    i.inside(grid).move(2,6,4)
    remaing_players =i.fill(i_players, temps_duration)
     
    hide_all(remaing_players)
    print(grid)
    incr_clock(image_duration)
    
    
    grid.set_margin(0)
    coeur_players = get_all_players()
    random.shuffle(coeur_players)
    coeur = Coeur()
    coeur.inside(grid).prop_move(0.495,0.495, 0.01)
    remaing_players=coeur.fill(coeur_players)
    coeur.inside(grid).prop_move(1/15,1/15+(13-9.1)/(2*13), 9.1/15,temps_duration) 
     

    hide_all(remaing_players)
    print(grid)
     
    incr_clock(image_duration)
    
    
    grid.set_margin(20) 
    e = E()
    e_players = get_all_players()
    random.shuffle(e_players)
    e.inside(grid).move(2,6,5 ) 
    remaing_players = e.fill(e_players, temps_duration)
    hide_all(remaing_players)
     
    incr_clock(image_duration)
    #hide_all(remaing_players)
     
    print(grid)
    m_players = get_all_players()
    random.shuffle(e_players)
    m = M()
    m.inside(grid).move(2,4,9)
    remaing_players=m.fill(m_players, temps_duration) 
    hide_all(remaing_players)
     
    incr_clock(image_duration)
     
     
    print(grid)
     
    g_players = get_all_players()
    random.shuffle(g_players)
    g =G()
    g.inside(grid).move(2,4.5,6)
    remaing_players=g.fill(g_players, temps_duration) 
    hide_all(remaing_players)
    incr_clock(image_duration)
 
    
    print(grid)
     
    b_players = get_all_players()
    random.shuffle(b_players)
    #g_players.extend(m.get_players())
    b =B()
    b.inside(grid).move(2,4.5,6)
    remaing_players=b.fill(b_players, temps_duration) 
    hide_all(remaing_players)
     
    incr_clock(image_duration)
    print(grid)
    
    grid.to_tag("table2",0.5)
    Natacha_clarinette.swap(JeanJacques_chef,0.5)
    
     
    
    
    
 