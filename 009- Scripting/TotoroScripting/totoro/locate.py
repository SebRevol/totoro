
from totoro.display import Line, Column, Box, clock
from totoro.utils import get_num_box


def locate(mus, grid, instru_map) :
    
    grid.set_num_box(10)
    grid.set_margin(0) 
    
        
    '''
    "Jean-Jacques_chef_totoro"            
    "Jean-Jacques_percu_totoro"           
    "Jean-Jacques_chef_laché prise"       
    "Alizee_piano_totoro"                 
    "Bidou_euphonium_totoro"              
    "Serge_euphonium_totoro"              
    "Amélie_clarinette_recadre"           
    "Nelly_clarinette_totoro"             
    "Natacha_clarinette_totoro"           
    "Pierre_clarinette_totoro_recadre"    
    "Anne-sonia_clarinette_totoro"        
    "Stephane_clarinette_totoro"          
    "PierreG_clarinette_totoro"           
    "Violette_clarinette_totoro"          
    "André_cor_totoro"                    
    "Alain_flute_totoro"                  
    "Laurence_flute_totoro"               
    "Antoine_flute_totoro"                
    "Gwenn_flute_totoro"                  
    "Aurélie_hautbois_totoro"             
    "Veronique_hautbois_totoro"           
    "Aurianne_saxophone_totoro"           
    "Marie-Claude_saxophone_totoro"       
    "Franck_saxophone_totoro"             
    "Nadine_saxophone_totoro"             
    "Nathalie_saxophone_totoro"           
    "Chloe_saxophone_totoro_clown_recadre"
    "Camille_trombone_totoro"             
    "daniel_trombone_totoro"              
    "Bidou_cornet_totoro"                 
    "Serge_trompette_totoro"              
    "Patrick_trompette_totoro"            
    "Marianne_trompette_totoro"           
    "Svoisine_tuba"                       
    "Serge_baryton_totoro_recadre"        
    "Srevol_tuba_recadre"
    '''                 
    musiciens = list(mus.keys())
    col_gauche =Column(musiciens[0:9])
    col_gauche.move(1,1)
      
    col_droite = Column(musiciens[9:18])
    col_droite.move(2,10)
#     
    ligne_haut = Line( musiciens[18:27])
    ligne_haut.move(1,2)
      
    ligne_bas = Line(musiciens[27:36])
    ligne_bas.move(10,1)
    
    #Serge au centre
    mus["Serge_euphonium_totoro"].move(2,2,8)
    
    
    clock("00:00:22:38")
    duree_transition = 0.5 #en  secondes
    #grid.set_num_box(get_num_box(len(instru_map)))

    
      
    col_gauche.hide()
    col_droite.hide() 
    ligne_haut.hide()
    ligne_bas.hide()          
       
    mus["Serge_euphonium_totoro"].hide()
    box_map = {}
    
    tubas = Box(instru_map['Tuba'])
    
    tubas.move(1,1,10)

    clock("00:00:25:00")
    
    tubas.hide()
    clarinettes = Box(instru_map['Clarinettes'])
    clarinettes.move(1,1,10)
    
    clock("00:00:30:00")
    
    clarinettes.hide()
    sax = Box(instru_map['Saxophone'])
    sax.move(1,1,10)
    
    
    
    clock("00:00:35:00")
    
    tubas.show()
    clarinettes.show()
    
    
    #grid.auto_layout()
    
    clock("00:00:40:00")
    
    grid.set_num_box(3)
    top_box = Box([], 2,3)
    top_box.move(1/2, 1,3 )
    
    tubas.inside(top_box).move(1,1,1)
    clarinettes.inside(top_box).move(2,2,1)
    sax.inside(top_box).move(1,3,1)
    
    
    clock("00:00:45:00")
    
    tubas.inside(top_box).move(1,3,1)
    clarinettes.inside(top_box).move(1,1,2)
    sax.inside(top_box).move(2,3,1)
    
    
    
    clock("00:00:50:00")
    
    top_box.auto_layout()
    
    
    clock("00:00:55:00")
    tubas.to_previous()
    clarinettes.to_previous()
    sax.to_previous()
    
    
    clock("00:01:00:00")
    
    tubas.swap(clarinettes)
    mus["Serge_euphonium_totoro"].swap(sax)
    sax.hide()
    
    
#     for instru in instru_map:
#         print("==============instru============="+ instru)
#         print(instru_map[instru])
#         box =  Box(0,0,instru_map[instru])
#         box_map[instru]=box
#         box.inside(grid).on(t_clap).auto_layout()
#         
#     grid.auto_layout(duree_transition)
    
    
