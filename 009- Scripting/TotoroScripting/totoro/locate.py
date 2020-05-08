



from totoro import locate_camille
from totoro.utils import get_time_from_user_string, get_frame_duration
from totoro.display import hide_all, incr_clock, clock, get_box_from_players,\
    get_clock, Box, rotate, rotate_clock, Line
from totoro.players import get_all_players, JeanJacques_chef, Natacha_clarinette,\
    Veronique_hautbois, JeanSeb_percu, Benoit_flute, Serge_euphonium,\
    Serge_baryton, JeanJacques_chef_lacheprise, Chloe_saxophone, Laurence_flute,\
    clar, Cecile_clarinette, fl, hb, Svoisine_tuba, Srevol_tuba_recadre,\
    Nathalie_saxophone, Serge_trompette, PierreG_clarinette, Francoise_saxophone,\
    Myrtille_cor, Flore_piano, Bidou_euphonium, Camille_bonus_recadre
from totoro.tetris import I, Coeur, E, M, G, B, Barre, L, Te, Z, Carre, S
import random

def locate(resource):
    locate_camille.locate(resource)
    grid= resource.grid
    
    
    i_love_emgb(grid)
    play_tetris(grid)
    
    #resource.cut ("00:03:00:00",  "00:03:41:00") 
     
    
    #resource.cut ("00:01:53:62","00:03:41:00")
    #resource.cut ("00:01:55:62","00:02:05:00")
    
start_time_string = "00:01:58:62"
start_time = get_time_from_user_string(start_time_string)

end_time_string = "00:02:17:80"
end_time = get_time_from_user_string(end_time_string) 
      
def i_love_emgb(grid):
    clock(start_time_string)
    grid.set_num_box(15)
    grid.set_margin(20)
    
    Camille_bonus_recadre.hide()
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
    grid.set_margin(0)
    grid.set_num_box(7)
   
    players = get_all_players()
    players.remove(Natacha_clarinette) 
    random.Random(6).shuffle(players)
    
    col_gauche = Box([],5,2)
    col_gauche.inside(grid).move(1,1,2)
    
    ligne_bas =  Box([],2,5)
    ligne_bas.inside(grid).move(6,1, 5)
    
    col_droite =  Box([],5,2)
    col_droite.inside(grid).move(3,6, 2)
    
    ligne_haut=  Box([],2,5)
    ligne_haut.inside(grid).move(1,3, 5)
    
    players = col_gauche.fill(players,0.2)
    players = ligne_bas.fill(players,0.2)
    players = col_droite.fill(players,0.2)
    players = ligne_haut.fill(players,0.2)
    
    Natacha_clarinette.inside(grid).move(3,3,3, 0.2)
    hide_all(players)
    JeanJacques_chef.hide()
    JeanJacques_chef_lacheprise.hide()
    print(grid)
    
    
    
    clock("00:02:18:70")
    
   
    
    current_time = get_time_from_user_string(get_clock())
    fin_tour = get_time_from_user_string("00:02:21:06")
    duration = ((fin_tour-current_time) - get_frame_duration()).total_seconds()
    col_gauche.inside(grid).goto(-5,1,duration)
    ligne_bas.inside(grid).goto(6,-5,duration)
    col_droite.inside(grid).goto(9,6,duration)
    ligne_haut.inside(grid).goto(1,9,duration)
    
    
    
   
  
    


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
    if (line_num >box.num_box_line):
        return (None, None)
    return (line_num, col_num) 
    

def play_tetris(grid):
    
    start_time_string = "00:02:21:16"
    end_time_string = "00:03:14:00"

    start_time = get_time_from_user_string(start_time_string)
    end_time = get_time_from_user_string(end_time_string)
    
    grid.set_margin(20)
    clock(start_time_string)
    
    
    hide_all()
    grid.set_num_box(7)
    grid.set_margin(20)
    
    players = get_all_players()
    players.remove(Serge_trompette)
    
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
    grid.tag('fin tetris')
     
    print(grid)
    

    players = get_all_players()
    players.remove(Serge_trompette)
    random.Random(4).shuffle(players)
    grid.set_num_box(7)
    grid.set_margin(0)
    
    col_gauche = Box([],5,2)
    col_gauche.inside(grid).goto(1,1)
    ligne_bas =  Box([],2,5)
    ligne_bas.inside(grid).goto(6,1)
    col_droite =  Box([],5,2)
    col_droite.inside(grid).goto(3,6)
    ligne_haut= Box([],2,5)
    ligne_haut.inside(grid).goto(1,3)
    hide_all()
    remaining_players= col_gauche.fill(players, 0.5)
    remaining_players= ligne_bas.fill(remaining_players, 0.5)
    remaining_players= col_droite.fill(remaining_players, 0.5)
    remaining_players= ligne_haut.fill(remaining_players, 0.5)
    Laurence_flute.swap( Chloe_saxophone)  # @UndefinedVariable
    Chloe_saxophone.inside(grid).move(3,3,3)  # @UndefinedVariable
    
    box_chloe = grid.get_box(1,1,7,7)
    #box_chloe.expand(0.5, expand_children = True)
    #box_chloe.expand(2, expand_children = False)
    Chloe_saxophone.inside(grid).move(3,3,3)  # @UndefinedVariable
   
    sub_box = grid.get_box(2,2,5,5)
    time= get_clock()
    
    rotate(grid, 0.3,7.5)
    clock(time)
    rotate_clock(sub_box,0.3,7.5 )
    
    grid.set_margin(0)
   
    
    clarinettes = clar.all.copy()
    clarinettes.remove(Cecile_clarinette)
    flute_et_hb = fl.all
    flute_et_hb.extend(hb.all)
    grid.set_num_box(8)
    clock("00:03:03:30")
    hide_all()
    box_clar = Box(clarinettes)
    box_clar.auto_layout()
    box_clar.inside(grid).move(1,1,4)
    
    clock("00:03:04:20")
    box_clar.hide()
    box_flute_hb = Box(flute_et_hb)
    box_flute_hb.auto_layout()
    box_flute_hb.inside(grid).move(5,5,4)
    
    clock("00:03:04:70")
    box_all = Box([],4,4)
    clarinettes.extend(flute_et_hb)
    box_all.inside(grid).move(1,1,8)
    remaining_players=box_all.fill(clarinettes)
    hide_all(remaining_players)
    
    
    clock("00:03:05:20")
    box_all.hide()
    grid.set_num_box(2)
    Serge_baryton.inside(grid).move(1,1,1)  # @UndefinedVariable
    Cecile_clarinette.inside(grid).move(2,2,1)  # @UndefinedVariable
    Svoisine_tuba.inside(grid).move(1,2,1)  # @UndefinedVariable
    Srevol_tuba_recadre.inside(grid).move(2,1,1)  # @UndefinedVariable
    
    
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
    box1 = grid.get_box(2,1, 7,7)
    new_box = Box([], 6,7)
    
    for line in range(6) :
        for col in range (7):
            player = box1.get_player(line+1, col+1)
            player.inside(new_box).move(line+1, col+1, 1)
            
    #grid.tag('fin tetris')
    
    
    box1=new_box
    grid.set_num_box(9)
    box1.inside(grid).move(1.5,2, 7, 0.2 )
    incr_clock(0.2)
    print(len(box1.children))
    ratio = 1+2/7
    box1.expand(ratio, expand_children = False)  
   
    rel_x, rel_y,rel_size = box1.get_absolute_coordinates()
    rel_x=rel_x-(rel_size/2)*(1-ratio)/8
    box1.prop_move(rel_y, rel_x, rel_size)
    
    
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
    
    JeanJacques_chef_lacheprise.inside(grid).move(4,4,3,0.4)  # @UndefinedVariable
    
    
    grid.set_num_box(15)
    grid.set_margin(0)
    box1.expand(10, expand_children = False, duration=1)
    incr_clock(1.7)
    JeanJacques_chef_lacheprise.hide()  # @UndefinedVariable
    JeanJacques_chef.hide()  # @UndefinedVariable
    coeur_players = get_all_players()
    coeur_players.remove(Serge_trompette)
    coeur_players.remove(Bidou_euphonium)
    random.Random(1).shuffle(coeur_players)
    coeur = Coeur()
    coeur.inside(grid).prop_move(0.495,0.495, 0.01)
    remaing_players=coeur.fill(coeur_players)    
    coeur.get_player(4,4).swap(Veronique_hautbois)
    coeur.inside(grid).prop_move(1/15,1/20+(13-9.1)/(2*13), 9.1/15,1) 
    
    
   
    
    clock("00:03:26:22")
  
    players.remove(Veronique_hautbois)
   
    grid.set_num_box(3)
    Veronique_hautbois.inside(grid).move(2,2,1,2)  # @UndefinedVariable
    JeanSeb_percu.hide()  # @UndefinedVariable
    incr_clock(0.5)
    Benoit_flute.hide()  # @UndefinedVariable
    incr_clock(0.5)
    Serge_euphonium.hide()  # @UndefinedVariable
    incr_clock(0.5)
    Serge_baryton.hide()  # @UndefinedVariable
    


    