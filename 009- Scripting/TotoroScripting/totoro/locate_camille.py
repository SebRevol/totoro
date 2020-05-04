
from totoro.display import Line, Column, Box, clock, incr_clock
from totoro.utils import get_num_box, get_user_string_from_time,\
    get_time_from_user_string
import datetime
#from totoro.spectrum import spectrum

from totoro.players import *
def locate(resource):

    grid= resource.grid
    grid.auto_layout()
 
#initialisation de la grille à partir du auto layout    
   # JeanJacques_chef_lacheprise.swap(JeanSeb_percu)
    JeanJacques_chef_lacheprise.inside(grid).goto(0,0)
    Camille_bonus=mus["Camille_bonus_recadre"] #je les initialise ici car tu as effacé mon fichier players xD
    Laurence_bonus=mus["Laurence_bonus_recadre"]
    Nadine_bonus=mus["Nadine_bonus_recadre"]
    Bidou_bonus=mus["Bidou_bonus_recadre"]
    Nelly_bonus=mus["Nelly_bonus_recadre"]
    JeanJacques_chef=mus["Jean-Jacques_chef_totoro"]
    JeanSeb_percu=mus["Jean-Seb_percu_totoro"]
    Patrick_trompette=mus["Patrick_trompette_totoro_recadre"]

    #Camille_bonus.swap(Serge_baryton)
    #Bidou_bonus.swap(Srevol_tuba_recadre)
    
    Camille_bonus.inside(grid).goto(-1,-1)
    Laurence_bonus.inside(grid).goto(-2,-2)
    Nadine_bonus.inside(grid).goto(-3,-3)
    Bidou_bonus.inside(grid).goto(-4,-4)
    Nelly_bonus.inside(grid).goto(-5,-5)
   

    daniel_trombone.inside(grid).goto(1,2)
    JeanJacques_percu.inside(grid).goto(1,3)
    Amelie_clarinette_recadre.inside(grid).goto(1,4)
    Aurianne_saxophone.inside(grid).goto(1,5)
    Stephane_clarinette.inside(grid).goto(2,1)
    Gwenn_flute.inside(grid).goto(2,2)
    Andre_cor.inside(grid).goto(2,3)
    Aurelie_hautbois.inside(grid).goto(2,4)
    Nadine_saxophone.inside(grid).goto(2,5)
    Pierre_clarinette.inside(grid).goto(2,6)
    JeanJacques_chef.inside(grid).goto(-2,-7) #on le vire pour mettre serge en avant
    MarieClaude_saxophone.inside(grid).goto(3,1)
    Bidou_cornet.inside(grid).goto(3,2)
    Svoisine_tuba.inside(grid).goto(1,6)
    Myrtille_cor.inside(grid).goto(1,7)
    Laurence_flute.inside(grid).goto(7,1)
    JeanSeb_percu.inside(grid).goto(3,6)
    Annesonia_clarinette.inside(grid).goto(3,7)
    Veronique_hautbois.inside(grid).goto(4,1)
    Francoise_saxophone.inside(grid).goto(4,2)
    Natacha_clarinette.inside(grid).goto(1,1)
    Serge_euphonium.inside(grid).move(3,3,3)
    Cecile_trombone.inside(grid).goto(7,6)
    Benoit_flute.inside(grid).goto(4,6)
    Chloe_saxophone.inside(grid).goto(4,7)
    Franck_saxophone.inside(grid).goto(5,1)
    Alain_flute.inside(grid).goto(5,2)    
    Cecile_clarinette.inside(grid).goto(7,7)
    Serge_trompette.inside(grid).goto(5,7)
    Nelly_clarinette.inside(grid).goto(5,6)
    Marianne_trompette.inside(grid).goto(2,7)
    Bidou_euphonium.inside(grid).goto(-5,-5)    
    Violette_clarinette.inside(grid).goto(6,1)
    Antoine_flute.inside(grid).goto(6,2)
    Nathalie_saxophone.inside(grid).goto(6,3)
    Patrick_trompette.inside(grid).goto(6,4)
    Alizee_piano.inside(grid).goto(6,5)
    Ineke_clarinette.inside(grid).goto(6,6)
    Camille_trombone.inside(grid).goto(6,7)
    Jawad_flute.inside(grid).goto(7,2)
    Serge_baryton.inside(grid).goto(7,3)
    Srevol_tuba_recadre.inside(grid).goto(7,4)
    PierreG_clarinette.inside(grid).goto(7,5)
    
    clock("00:00:22:00")
    print(grid)
    grid.tag("initial")
    grid.tag("table1")
    
    clock("00:00:23:00") #c'est le clap
    #print(grid.tag("initial"))
    #grid.tag_map.get("initial")

    Annesonia_clarinette.inside(grid).goto(1,1,0.5)
    Camille_trombone.inside(grid).goto(1,2,0.5)
    JeanSeb_percu.inside(grid).goto(1,3,0.5)
    Nelly_clarinette.inside(grid).goto(1,4,0.5)
    Franck_saxophone.inside(grid).goto(1,5,0.5)
    Srevol_tuba_recadre.goto(1,6,0.5)
    Andre_cor.goto(1,7,0.5)
    Cecile_clarinette.inside(grid).goto(2,1,0.5)
    Laurence_flute.inside(grid).goto(2,2,0.5)
    Myrtille_cor.inside(grid).goto(2,3,0.5)
    Veronique_hautbois.inside(grid).goto(2,4,0.5)
    Nathalie_saxophone.inside(grid).goto(2,5,0.5)
    PierreG_clarinette.inside(grid).goto(2,6,0.5)
    Francoise_saxophone.inside(grid).goto(2,7,0.5)
    Chloe_saxophone.inside(grid).goto(3,1,0.5)
    Serge_baryton.inside(grid).goto(3,2,0.5) 
    JeanJacques_chef.inside(grid).move(3,3,3) 
    Antoine_flute.inside(grid).goto(3,6,0.5)
    Alain_flute.inside(grid).goto(3,7,0.5)       
    Aurelie_hautbois.inside(grid).goto(4,1,0.5)
    Ineke_clarinette.inside(grid).goto(4,2,0.5)
    Jawad_flute.inside(grid).goto(4,6,0.5)
    MarieClaude_saxophone.inside(grid).goto(4,7,0.5)     
    Aurianne_saxophone.inside(grid).goto(5,1,0.5)
    Cecile_trombone.inside(grid).goto(5,2,0.5)
    Amelie_clarinette_recadre.inside(grid).goto(5,6,0.5)
    Natacha_clarinette.inside(grid).goto(5,7,0.5)
    Benoit_flute.inside(grid).goto(6,1,0.5)
    Marianne_trompette.inside(grid).goto(6,2,0.5)
    Nadine_saxophone.inside(grid).goto(6,3,0.5)
    Bidou_euphonium.inside(grid).goto(6,4,0.5)    
    Serge_trompette.inside(grid).goto(6,5,0.5)
    Violette_clarinette.inside(grid).goto(6,6,0.5)
    daniel_trombone.inside(grid).goto(6,7,0.5)
    Gwenn_flute.inside(grid).goto(7,1,0.5)
    Serge_euphonium.inside(grid).goto(7,2,0.5)
    Patrick_trompette.inside(grid).goto(7,3,0.5) 
    Svoisine_tuba.inside(grid).goto(7,4,0.5)
    Pierre_clarinette.inside(grid).goto(7,5,0.5)
    Alizee_piano.inside(grid).goto(7,6,0.5)  
    Stephane_clarinette.inside(grid).goto(7,7,0.5) 

    Bidou_cornet.inside(grid).goto(-3,-2)#on le vire pour mettre serge en avant
    JeanJacques_percu.inside(grid).goto(-5,-2) 

    grid.tag("table2")
    
    print(grid)
    
    clock("00:00:30:00")
    grid.set_num_box(8)
    Srevol_tuba_recadre.inside(grid).move(10,10,1)
    Annesonia_clarinette.inside(grid).move(-1,-1,1)
    Franck_saxophone.inside(grid).move(-1,-1,1)
    Nelly_clarinette.inside(grid).move(-1,-1,1)
    JeanSeb_percu.inside(grid).move(-1,-1,1)
    Andre_cor.inside(grid).move(-1,-1,1)
    Cecile_clarinette.inside(grid).move(-1,-1,1)
    PierreG_clarinette.inside(grid).move(-1,-1,1)
    Alain_flute.inside(grid).move(-1,-1,1)
    Aurelie_hautbois.inside(grid).move(-1,-1,1)
    Ineke_clarinette.inside(grid).move(-1,-1,1)
    Amelie_clarinette_recadre.inside(grid).move(-1,-1,1)
    Benoit_flute.inside(grid).move(-1,-1,1)
    Gwenn_flute.inside(grid).move(-1,-1,1)
    Serge_euphonium.inside(grid).move(-1,-1,1)
    Nadine_saxophone.inside(grid).move(-1,-1,1)
    Bidou_euphonium.inside(grid).move(-1,-1,1)
    Patrick_trompette.inside(grid).move(-1,-1,1)
    Alizee_piano.inside(grid).move(-1,-1,1)
    Stephane_clarinette.inside(grid).move(-1,-1,1)
    Pierre_clarinette.inside(grid).move(-1,-1,1)
    Natacha_clarinette.inside(grid).move(-1,-1,1)
    Camille_trombone.inside(grid).move(-1,-1,1)
    #Srevol_tuba_recadre.inside(grid).move(-10,-10,1)
    Laurence_flute.inside(grid).move(-1,-1,1)
    Myrtille_cor.inside(grid).move(-1,-1,1)
    Veronique_hautbois.inside(grid).move(-1,-1,1)
    Nathalie_saxophone.inside(grid).move(-1,-1,1)
    Francoise_saxophone.inside(grid).move(-1,-1,1)
    Antoine_flute.inside(grid).move(-1,-1,1)
    Chloe_saxophone.inside(grid).move(-1,-1,1)
    Laurence_bonus.inside(grid).move(-1,-1,1)
    MarieClaude_saxophone.inside(grid).move(-1,-1,1)
    Jawad_flute.inside(grid).move(-1,-1,1)
    Aurianne_saxophone.inside(grid).move(-1,-1,1)
    Violette_clarinette.inside(grid).move(-1,-1,1)
    daniel_trombone.inside(grid).move(-1,-1,1)
    Marianne_trompette.inside(grid).move(-1,-1,1)
    Serge_trompette.inside(grid).move(-1,-1,1)
    Svoisine_tuba.inside(grid).move(-1,-1,1)
    Cecile_trombone.inside(grid).move(-1,-1,1)
    Serge_baryton.inside(grid).move(-1,-1,1)
    JeanJacques_chef.inside(grid).move(2,2,6)
    grid.tag("8x8")
    
    line1=Line(clar.all)
    line1.inside(grid).goto(1,1)
    line8=Line(sax.all)
    line8.inside(grid).goto(8,2)
    col8=Column(fl.all)
    col8.inside(grid).goto(2,8)
    col1=Column(trb.all)
    col1.inside(grid).goto(2,1)
    col1b=Column(trp.all)
    col1b.inside(grid).goto(5,1)
    col1c=Column(tb.all)
    col1c.inside(grid).goto(8,1)
    
    print(grid)
    line1.h_shift(16,20)
    col8.v_shift(12,20)
    line8.h_shift(-14,20)
    

    clock("00:00:50:00")
    JeanJacques_chef_lacheprise.inside(grid).move(10,10,6)
    JeanJacques_chef.swap(JeanJacques_chef_lacheprise)
    clock("00:00:53:00")
    JeanJacques_chef.swap(JeanJacques_chef_lacheprise)
    clock("00:00:57:00")
    JeanJacques_chef.swap(JeanJacques_chef_lacheprise) 
#    clock("00:01:00:00")
#    JeanJacques_chef.swap(JeanJacques_chef_lacheprise)
         
    print(grid)

    clock("00:01:04:00")
    
    grid.to_tag("initial")
   # print(grid)
    #prévoir un retour à une grille proche du départ 7x7
    daniel_trombone.inside(grid).move(1,1,3)
    Natacha_clarinette.goto(4,3)
    JeanJacques_percu.goto(-1,-2)
    Stephane_clarinette.goto(-1,-3)
    Gwenn_flute.goto(-1,-4)
    Andre_cor.goto(5,6)
    MarieClaude_saxophone.goto(-1,-6)
    Bidou_cornet.goto(4,4)
    Serge_euphonium.move(-1,-8,1)
    
    Marianne_trompette.inside(grid).move(2,5,3)
    Nadine_saxophone.goto(-2,-1)
    Pierre_clarinette.goto(-2,-2)
    JeanSeb_percu.goto(-2,-3)
    Annesonia_clarinette.goto(-2,-4)
    Benoit_flute.goto(-2,-5)
    Chloe_saxophone.goto(3,4)
    
    Nelly_clarinette.move(5,3,3)
    Nathalie_saxophone.goto(-3,-1)
    Patrick_trompette.goto(-3,-2)
    Alizee_piano.goto(-3,-3)
    Cecile_clarinette.goto(-3,-4)
    Srevol_tuba_recadre.goto(-3,-5)
    PierreG_clarinette.goto(7,7)
    Serge_baryton.goto(-3,-6)
   # print(grid)
    
    clock("00:01:12:00")
    daniel_trombone.inside(grid).move(-1,-1,1)
    Marianne_trompette.inside(grid).move(-2,-1,-1)
    Nelly_clarinette.move(-3,-1,-1)
    
    Svoisine_tuba.move(2,1,3)
    Veronique_hautbois.goto(-2,-2)
    Francoise_saxophone.goto(-2,-2)
    Natacha_clarinette.goto(-2,-2)

    Alain_flute.move(1,5,3)
    Aurianne_saxophone.goto(-2,-2)
    Myrtille_cor.goto(-2,-2)
    
    Aurianne_saxophone.move(5,5,3)
    Andre_cor.goto(1,1)
    PierreG_clarinette.goto(1,2)
    Serge_trompette.goto(5,2)
    Ineke_clarinette.goto(4,5)
    Camille_trombone.goto(-5,-5)
    Cecile_trombone.goto(1,3)
    Franck_saxophone.swap(Serge_baryton)
    Violette_clarinette.swap(Stephane_clarinette)
    Laurence_flute.swap(Gwenn_flute)
    Jawad_flute.swap(Nadine_saxophone)
    Antoine_flute.swap(Srevol_tuba_recadre)
    Bidou_cornet.goto(7,3)
    Amelie_clarinette_recadre.goto(4,6)
    Chloe_saxophone.goto(7,4)
    Aurelie_hautbois.goto(4,7)
    JeanJacques_percu.goto(6,3)
    Nathalie_saxophone.goto(6,4)
    Annesonia_clarinette.goto(1,4)
    MarieClaude_saxophone.goto(2,4)
    Myrtille_cor.goto(5,3)
    Veronique_hautbois.goto(5,4)
    Natacha_clarinette.goto(3,4)
    Patrick_trompette.goto(4,4)
    
    #print(grid)

    
    clock("00:01:20:00")

    grid.set_num_box(6)
    grid.auto_layout()
    
    Antoine_flute.goto(-2,-2)
    PierreG_clarinette.goto(-3,-3)
    
    Camille_trombone.inside(grid).move(1,1,3)
    Cecile_trombone.inside(grid).move(4,4,3)
    
    Amelie_clarinette_recadre.inside(grid).goto(4,1)
    Nelly_clarinette.inside(grid).goto(4,2)
    Natacha_clarinette.inside(grid).goto(4,3)
    Pierre_clarinette.inside(grid).goto(5,1)
    PierreG_clarinette.inside(grid).goto(5,2)
    Ineke_clarinette.inside(grid).goto(5,3)
    Annesonia_clarinette.inside(grid).goto(6,1)
    Stephane_clarinette.inside(grid).goto(6,2)
    Violette_clarinette.inside(grid).goto(6,3)
    Bidou_cornet.inside(grid).goto(1,4)
    Serge_trompette.inside(grid).goto(1,5)
    Patrick_trompette.inside(grid).goto(1,6)
    Marianne_trompette.inside(grid).goto(2,4)
    Andre_cor.inside(grid).goto(2,5)
    Myrtille_cor.inside(grid).goto(2,6)
    Svoisine_tuba.inside(grid).goto(3,4)
    Serge_baryton.inside(grid).goto(3,5)
    Srevol_tuba_recadre.inside(grid).goto(3,6)
    #print(grid)

    clock("00:01:27:00")
    Camille_trombone.inside(grid).move(-1,-1,1)
    Cecile_trombone.inside(grid).move(-4,-4,1)
    
    Amelie_clarinette_recadre.inside(grid).goto(-4,1)
    Nelly_clarinette.inside(grid).goto(-4,2)
    Natacha_clarinette.inside(grid).goto(-4,3)
    Pierre_clarinette.inside(grid).goto(-5,1)
    PierreG_clarinette.inside(grid).goto(-5,2)
    Ineke_clarinette.inside(grid).goto(-5,3)
    Annesonia_clarinette.inside(grid).goto(-6,1)
    Stephane_clarinette.inside(grid).goto(-6,2)
    Violette_clarinette.inside(grid).goto(-6,3)
    Bidou_cornet.inside(grid).goto(-1,4)
    Serge_trompette.inside(grid).goto(-1,5)
    Patrick_trompette.inside(grid).goto(-1,6)
    Marianne_trompette.inside(grid).goto(-2,4)
    Andre_cor.inside(grid).goto(-2,5)
    Myrtille_cor.inside(grid).goto(-2,6)
    Svoisine_tuba.inside(grid).goto(-3,4)
    Serge_baryton.inside(grid).goto(-3,5)
    Srevol_tuba_recadre.inside(grid).goto(-3,6)
    Jawad_flute.inside(grid).goto(-1,-1)    

    Gwenn_flute.inside(grid).move(1,4,3)
    Franck_saxophone.inside(grid).move(4,1,3)
    
    Nadine_saxophone.inside(grid).goto(1,1)
    Aurianne_saxophone.inside(grid).goto(1,2)
    MarieClaude_saxophone.inside(grid).goto(1,3) #ok
    Nathalie_saxophone.inside(grid).goto(2,1)
    Francoise_saxophone.inside(grid).goto(2,2)
    Chloe_saxophone.inside(grid).goto(2,3) 
    JeanSeb_percu.inside(grid).goto(3,1)
    
    Nadine_saxophone.swap(daniel_trombone)
    Aurianne_saxophone.swap(Cecile_trombone)
    Nathalie_saxophone.swap(Camille_trombone)
    Francoise_saxophone.swap(Myrtille_cor)
    Chloe_saxophone.swap(Andre_cor)
    JeanSeb_percu.swap(Serge_baryton)
    Alizee_piano.inside(grid).goto(3,2) #ok
    JeanJacques_percu.inside(grid).goto(3,3) #ok
    
    Antoine_flute.inside(grid).goto(4,4)
    Laurence_flute.inside(grid).goto(4,5)
    Alain_flute.inside(grid).goto(4,6)
    Serge_euphonium.inside(grid).goto(5,4)
    JeanJacques_chef_lacheprise.inside(grid).goto(5,5)
    Bidou_euphonium.inside(grid).goto(5,6)
    Veronique_hautbois.inside(grid).goto(6,4)
    Benoit_flute.inside(grid).goto(6,5)
    Aurelie_hautbois.inside(grid).goto(6,6)
    
    #print(grid)

    clock("00:01:35:00")
    grid.to_tag("table2")
#    print(grid)

    Bidou_euphonium.inside(grid).move(1,4,3)
    Laurence_bonus.inside(grid).move(4,1,3) #à vérifier
    Nadine_bonus.inside(grid).move(5,4,3) 
    
    JeanJacques_chef.inside(grid).move(-1,-1,1)
    JeanSeb_percu.inside(grid).goto(4,3)
    Nelly_clarinette.inside(grid).goto(5,3)
    Franck_saxophone.inside(grid).goto(4,4)
    Myrtille_cor.inside(grid).goto(-1,-1)
    Veronique_hautbois.inside(grid).goto(-2,-2)
    Nathalie_saxophone.inside(grid).goto(-3,-3)
    Aurianne_saxophone.inside(grid).goto(-1,-1)
    Cecile_trombone.inside(grid).goto(-1,-1)
    Nelly_clarinette.inside(grid).goto(-1,-1)
    Benoit_flute.inside(grid).goto(-1,-1)
    Marianne_trompette.inside(grid).goto(-1,-1)
    Nadine_saxophone.inside(grid).goto(-1,-1)
    Gwenn_flute.inside(grid).goto(-1,-1)
    Serge_euphonium.inside(grid).goto(-1,-1)
    Patrick_trompette.inside(grid).goto(-1,-1)
    Serge_trompette.inside(grid).goto(-1,-1)
    Violette_clarinette.inside(grid).goto(-1,-1)
    Svoisine_tuba.inside(grid).goto(-1,-1)
    Pierre_clarinette.inside(grid).goto(-1,-1)
    Alizee_piano.inside(grid).goto(-1,-1)
    Amelie_clarinette_recadre.inside(grid).goto(4,5)
    Laurence_flute.swap(Myrtille_cor)
    Srevol_tuba_recadre.inside(grid).goto(1,3)
    PierreG_clarinette.inside(grid).goto(2,3)
    Antoine_flute.inside(grid).goto(3,3)
    Aurelie_hautbois.inside(grid).goto(7,1)
    Ineke_clarinette.inside(grid).goto(7,2)
    JeanSeb_percu.inside(grid).goto(7,3)
    
    
    #print(grid)

    clock("00:01:44:00")
    grid.to_tag("table1")
    #print(grid)
    Serge_euphonium.inside(grid).move(-1,-1,1)
    Bidou_euphonium.inside(grid).move(-1,-1,1)
    Laurence_bonus.inside(grid).move(-1,-1,1)
    Nadine_bonus.inside(grid).move(-1,-1,1)
    Serge_baryton.inside(grid).move(1,5,3)
    Srevol_tuba_recadre.inside(grid).move(1,2,3)
    Pierre_clarinette.inside(grid).move(5,3,3)
    
    daniel_trombone.inside(grid).goto(4,3)
    JeanJacques_percu.inside(grid).goto(4,4)
    PierreG_clarinette.inside(grid).goto(4,5)
    Nathalie_saxophone.inside(grid).goto(-1,-1)
    Patrick_trompette.inside(grid).goto(-1,-1)
    Alizee_piano.inside(grid).goto(-1,-1)
    Amelie_clarinette_recadre.inside(grid).goto(-1,-1)
    Aurianne_saxophone.inside(grid).goto(-1,-1)
    Svoisine_tuba.inside(grid).goto(-1,-1)
    Myrtille_cor.inside(grid).goto(-1,-1)
    Gwenn_flute.inside(grid).goto(-1,-1)
    Andre_cor.inside(grid).goto(-1,-1)
    Aurelie_hautbois.inside(grid).goto(-1,-1)
    Nadine_saxophone.inside(grid).goto(-1,-1)
    Marianne_trompette.inside(grid).goto(-1,-1)
    Bidou_cornet.inside(grid).goto(-1,-1)
    JeanSeb_percu.inside(grid).goto(-1,-1)
    Annesonia_clarinette.inside(grid).goto(-1,-1)
   
    #print(grid)
    
    clock("00:01:51:00")
    #alizee, patrick, camille, daniel, amélie, JJ laché prise, tous les saxs
    
    grid.set_num_box(6)
    grid.auto_layout()
    
    Marianne_trompette.inside(grid).goto(-1,-1)
    Nathalie_saxophone.inside(grid).goto(-1,-1)
    Violette_clarinette.inside(grid).goto(-1,-1)
    Bidou_euphonium.inside(grid).goto(-1,-1)
    Antoine_flute.inside(grid).goto(-1,-1)
    Nelly_clarinette.inside(grid).goto(-1,-1)
    
    Alizee_piano.inside(grid).move(1,1,2)
    Patrick_trompette.inside(grid).move(1,3,2)
    Amelie_clarinette_recadre.inside(grid).move(1,5,2)
    Stephane_clarinette.inside(grid).move(3,1,2)
    JeanJacques_chef.inside(grid).move(3,3,2)
    Natacha_clarinette.inside(grid).move(3,5,2)
    Aurelie_hautbois.inside(grid).move(5,3,2)
    Cecile_clarinette.inside(grid).move(5,1,2)
    Chloe_saxophone.inside(grid).move(5,5,2)
    Gwenn_flute.inside(grid).goto(-1,-1)
    Serge_trompette.inside(grid).goto(-1,-1)
    Pierre_clarinette.inside(grid).goto(-1,-1)
    Serge_baryton.inside(grid).goto(-1,-1)
    Srevol_tuba_recadre.inside(grid).goto(-1,-1)
    Ineke_clarinette.inside(grid).goto(-1,-1)
    PierreG_clarinette.inside(grid).goto(-1,-1)
    Camille_trombone.inside(grid).goto(-1,-1)
    Jawad_flute.inside(grid).goto(-1,-1)
    
    
    #print(grid)
    
  #  incr_clock(2)

   #grid.auto_layout()
  #  all=mus.values()
  #  box1=grid.get_box(1,1,7,7) #(1,1 = angle en haut à gauche, 7,7 = dimension)
   # box1.inside(grid).goto(1,1)
   # box1.hide()
  #  print(grid)
   # line1=Line(sax.all)
 #   all.remove(Camille_trombone)#permet de retirer qqun
 #   remaining_players=line1.fill(sax.all)
    
  #  incr_clock(2)
    
  #  box2=Box([Camille_trombone,Srevol_tuba_recadre],3,3) #box([]=liste vide,ligne,colonne) dimension à l'intérieur de la box   
   # box2.auto_layout()
  #  Camille_trombone.inside(box2).move(1,1,1)
  #  Srevol_tuba_recadre.inside(box2).move(2,2,2)
   # box2.move(1,1,7)
  #  print(box2)
    
   # print(grid)
    
    #incr_clock(2)
  #  Srevol_tuba_recadre.swap(Camille_trombone)
   
   # print(grid)
   
   # print(box2)
    
   
     
    
    #grid.set_num_box(7)
    #grid.set_margin(40)
      

   # incr_clock(1) #(1) = 1seconde
    #columns = 7
    #lines =6
    #rate = 0.2
    #duration = 1
     
    
    #Camille_trombone.inside(grid).goto(1,1)
    
#   spectrum(columns, lines, rate, duration)
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
    
    #daniel_trombone.goto(1,2)
    #JeanJacques_percu.goto(1,3)
    #Amelie_clarinette_recadre.goto(1,4)
    #Aurianne_saxophone.goto(1,5)
    #Stephane_clarinette.goto(2,1)
    #Gwenn_flute.goto(2,2)
    #Andre_cor.goto(2,3)
    #Aurelie_hautbois.goto(2,4)
    #Nadine_saxophone.goto(2,5)
    #Pierre_clarinette.goto(2,6)
    #JeanJacques_chef.goto(2,7)
    #MarieClaude_saxophone.goto(3,1)
    #Bidou_cornet.goto(3,2)
    #Svoisine_tuba.goto(3,3)
    #Myrtille_cor.goto(3,4)
    #Laurence_flute.goto(3,5)
    #JeanSeb_percu.goto(3,6)
    #Annesonia_clarinette.goto(3,7)
    #Veronique_hautbois.goto(4,1)
    #Francoise_saxophone.goto(4,2)
    #Natacha_clarinette.goto(4,3)
    #Serge_euphonium.goto(4,4)
    #Cecile_trombone.goto(4,5)
    #Benoit_flute.goto(4,6)
    #Chloe_saxophone.goto(4,7)
    #Franck_saxophone.goto(5,1)
    #Alain_flute.goto(5,2)    
    #Cecile_clarinette.goto(5,3)
    #Serge_trompette.goto(5,7)
    #Nelly_clarinette.goto(5,6)
    #Marianne_trompette.goto(5,4)
    #Bidou_euphonium.goto(5,5)    
    #Violette_clarinette.goto(6,1)
    #Antoine_flute.goto(6,2)
    #Nathalie_saxophone.goto(6,3)
    #Patrick_trompette.goto(6,4)
    #Alizee_piano.goto(6,5)
    #Ineke_clarinette.goto(6,6)
    #Camille_trombone.goto(6,7)
   
    #Jawad_flute.goto(7,2)
    #Serge_baryton.goto(7,3)
    #Srevol_tuba_recadre.goto(7,4)
    #PierreG_clarinette.goto(7,5)
    
       
    #Serge_euphonium.swap(Jawad_flute)
    #Jawad_flute.goto(7,5)
    #Cecile_clarinette.swap(daniel_trombone)
    #Amelie_clarinette_recadre.swap(MarieClaude_saxophone)
    #Bidou_euphonium.swap(Annesonia_clarinette)
    #Annesonia_clarinette.goto(7,2)
    #Nelly_clarinette.swap(Benoit_flute)
    #Natacha_clarinette.swap(Andre_cor)
    ##Ineke_clarinette.swap(Franck_saxophone)
    ##PierreG_clarinette.swap(Srevol_tuba_recadre)
    #Alain_flute.swap(Camille_trombone)
    #Violette_clarinette.swap(Patrick_trompette)
    #Antoine_flute.swap(Bidou_cornet)
    ##Veronique_hautbois.swap(Marianne_trompette)
    #JeanJacques_percu.swap(Aurianne_saxophone)
    #Annesonia_clarinette.swap(Alizee_piano)
    ##JeanJacques_chef.swap(Chloe_saxophone)
    #Gwenn_flute.swap(Antoine_flute)
    

  
    
    
    
    
    
    
    
