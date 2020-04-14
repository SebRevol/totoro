
def locate(mus, grid) :
    
    grid.set_num_box(8)
    grid.set_margin(0) 
    
    #colonne gauche
    mus["Jean-Jacques_chef_totoro"            ].at(1,1,1)
    mus["Jean-Jacques_percu_totoro"           ].at(2,1,1)
    mus["Jean-Jacques_chef_laché prise"       ].at(3,1,1)
    mus["Aurianne_saxophone_totoro"           ].at(4,1,1)
    mus["Franck_saxophone_totoro"             ].at(5,1,1)
    mus["Nadine_saxophone_totoro"             ].at(6,1,1)
    mus["Nathalie_saxophone_totoro"           ].at(7,1,1)
    mus["Chloe_saxophone_totoro_clown_recadre"].at(8,1,1)
    
    #ligne du bas
    mus["Amélie_clarinette_recadre"           ].at(8,2,1)
    mus["Nelly_clarinette_totoro"             ].at(8,3,1)
    mus["Natacha_clarinette_totoro"           ].at(8,4,1)
    mus["Pierre_clarinette_totoro_recadre"    ].at(8,5,1)
    mus["Anne-sonia_clarinette_totoro"        ].at(8,6,1)
    mus["Stephane_clarinette_totoro"          ].at(8,7,1)
    mus["Violette_clarinette_totoro"          ].at(8,8,1)
    
    #colone droite
    mus["Alain_flute_totoro"                  ].at(7,8,1)
    mus["Laurence_flute_totoro"               ].at(6,8,1)
    mus["Antoine_flute_totoro"                ].at(5,8,1)
    mus["Gwenn_flute_totoro"                  ].at(4,8,1) 
    mus["Aurélie_hautbois_totoro"             ].at(3,8,1)  
    mus["Bidou_euphonium_totoro"              ].at(2,8,1)
    mus["Svoisine_tuba"                       ].at(1,8,1)
    
    #ligne du haut
    mus["Serge_baryton_totoro_recadre"        ].at(1,7,1)
    mus["Srevol_tuba_recadre"                 ].at(1,6,1)
    mus["Camille_trombone_totoro"             ].at(1,5,1)
    mus["daniel_trombone_totoro"              ].at(1,4,1)
    mus["Bidou_cornet_totoro"                 ].at(1,3,1)
    mus["Serge_trompette_totoro"              ].at(1,2,1)


    #Serge au centre
    mus["Serge_euphonium_totoro"              ].at(2,2,6)
    
    
    t_clap ="00:00:22:38"
    duree_transition = 0.5 #en  secondes
    grid.set_num_box(6)

    
    mus["Aurianne_saxophone_totoro"           ].on(t_clap).move(1,1,1, duree_transition)
    mus["Franck_saxophone_totoro"             ].on(t_clap).move(2,1,1, duree_transition)
    mus["Nadine_saxophone_totoro"             ].on(t_clap).move(3,1,1, duree_transition)
    mus["Nathalie_saxophone_totoro"           ].on(t_clap).move(4,1,1, duree_transition)
    mus["Chloe_saxophone_totoro_clown_recadre"].on(t_clap).move(5,1,1, duree_transition)
    mus["Serge_baryton_totoro_recadre"        ].on(t_clap).move(6,1,1, duree_transition)
    
    
    mus["Srevol_tuba_recadre"                 ].on(t_clap).move(6,2,1, duree_transition)
    mus["Svoisine_tuba"                       ].on(t_clap).move(6,3,1, duree_transition)
    mus["Jean-Jacques_percu_totoro"           ].on(t_clap).move(6,4,1, duree_transition)
    mus["Camille_trombone_totoro"             ].on(t_clap).move(6,5,1, duree_transition)
    mus["daniel_trombone_totoro"              ].on(t_clap).move(6,6,1, duree_transition)
    
    mus["Bidou_euphonium_totoro"              ].on(t_clap).move(5,6,1, duree_transition)
    mus["Serge_euphonium_totoro"              ].on(t_clap).move(4,6,1, duree_transition)
    mus["Bidou_cornet_totoro"                 ].on(t_clap).move(3,6,1, duree_transition)
    mus["Serge_trompette_totoro"              ].on(t_clap).move(2,6,1, duree_transition)
    
    mus["Amélie_clarinette_recadre"           ].on(t_clap).move(1,6,1, duree_transition)
    mus["Nelly_clarinette_totoro"             ].on(t_clap).move(1,5,1, duree_transition)
    mus["Natacha_clarinette_totoro"           ].on(t_clap).move(2,5,1, duree_transition)
    mus["Pierre_clarinette_totoro_recadre"    ].on(t_clap).move(3,5,1, duree_transition)
    mus["Anne-sonia_clarinette_totoro"        ].on(t_clap).move(4,5,1, duree_transition)
    mus["Stephane_clarinette_totoro"          ].on(t_clap).move(5,5,1, duree_transition)
    mus["Violette_clarinette_totoro"          ].on(t_clap).move(5,4,1, duree_transition)
    
    mus["Alain_flute_totoro"                  ].on(t_clap).move(5,3,1, duree_transition)
    mus["Laurence_flute_totoro"               ].on(t_clap).move(5,2,1, duree_transition)
    mus["Antoine_flute_totoro"                ].on(t_clap).move(4,2,1, duree_transition)
    mus["Gwenn_flute_totoro"                  ].on(t_clap).move(3,2,1, duree_transition) 
    mus["Aurélie_hautbois_totoro"             ].on(t_clap).move(2,2,1, duree_transition)  
   
  

    mus["Jean-Jacques_chef_laché prise"       ].on(t_clap).move(1,2,1, duree_transition)
    mus["Jean-Jacques_chef_totoro"            ].on(t_clap).move(2,3,2, duree_transition)
