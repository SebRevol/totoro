'''
Created on 6 avr. 2020

@author: SR246418
'''
from totoro.model import merge_files, Resource
from totoro.display import clock, incr_clock, get_duration_clock, Column
from totoro.utils import set_current_resource, hide_all, get_duration
from totoro.tetris import Barre, Te, Carre, Coeur
from totoro.spectrum import get_audio_data, SepctrumCol
from totoro.spectrum import spectrum


def rotate(container, iteration_par_second, duration):
    iteration_num = iteration_par_second * duration
    iteration_duration = duration / iteration_num
    
    col_size = container.num_box_line -1
    line_size = container.num_box_col -1
    for _ in range(iteration_num):
        col_gauche = container.get_box(1,1,col_size,1)
        ligne_bas =  container.get_box(col_size+1,1,1,line_size)
        col_droite =  container.get_box(2,line_size+1,col_size,1)
        ligne_haut= container.get_box(1,2,1,line_size)
        
        col_gauche.goto(2,1,iteration_duration)
        ligne_bas.goto(col_size+1,2,iteration_duration)
        col_droite.goto(1,line_size+1,iteration_duration)
        ligne_haut.goto(1,1,iteration_duration)
        incr_clock(iteration_duration)


if __name__ == '__main__':

    # changer ici les chemin des fichiers à fusionner, rajouter autant de lignes que de fichiers
    merge_files([
        # in
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - percussion.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - barytons.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - clarinette1.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - cor.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - flute et hautbois.mlt',
	    '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - saxophone.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - trombone.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - trompette.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - tuba.mlt'
        ],
        # out
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Test-API-merge2.mlt'
    )


    resource=Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Test-API-merge2.mlt')
    set_current_resource(resource)
   # from totoro.players import *

    
    instru_map = resource.instru_map
    mus = resource.players_registry
    
    grid = resource.grid
    grid.auto_layout()
     
     
    grid.tag("initial")
    
    
#     grid.set_num_box(8)
#     grid.set_margin(40)
#      
#     clock("00:00:30:00")
#     columns = 3
#     lines =8
#     rate = 0.4
#     duration = 10
#     
#     Chloe_saxophone.hide()
#     
#     spectrum(columns, lines, rate, duration)
#     
#     clock("00:00:45:00")
#   
#     columns = 3
#     lines =8
#     rate = 0.3
#     duration = 10
#             
#     spectrum(columns, lines, rate, duration)
#     
#     
#     clock("00:01:00:00")
#   
#     columns = 3
#     lines =8
#     rate = 0.2
#     duration = 10
#             
#     spectrum(columns, lines, rate, duration)
    
            
    
    
    
    bottom_line = grid.get_line(5)
    bottom_line.goto(5,-0.5,2)
    
    grid.tag("aligned")
     
    clock("00:00:30:00")
    column = grid.get_column(1)
     
    column.shift(4, 2)
     
    clock("00:00:32:00")
    grid.get_line(5).shift(4,2)
     
    clock("00:00:34:00")
    grid.get_column(5).shift(-4,2)
     
    clock("00:00:36:00")
    column = grid.get_column(5)
    column.goto(-4,5,2)
     
    clock("00:00:38:00")
    grid.get_box(1,1,5,4).goto(1,2,1)
    clock("00:00:39:00")
    column.goto(-4,1)
    column.goto(1,1,1)
     
     
    clock("00:00:41:00")
     
    
    mus["Franck_saxophone_totoro"].inside(grid).goto(5,5,1)
    center_box = grid.get_box(2,2,3,3)
    center_box.auto_layout(0.5)
     
    rotate(grid, 2, 10)
#          
#     moving_player = grid.get_player(3,1)
#      
#     for column in range(4):
#         other_player = grid.get_player(3,column +2)
#         moving_player.swap(other_player)
#         incr_clock(2)
#     
#     grid.to_tag("aligned", 2)
#     incr_clock(2)
#           
#           
#     for col in range(grid.num_box_col):
#         if (col %2 ==0):
#             num_box = -20
#         else :
#             num_box = 20
#         grid.get_column(col+1).shift(num_box, 10)
#             
#     incr_clock(10)
#     
#     
#    
#     clock("00:01:30:00")
#    
#        
#     grid.get_box(1, 1, grid.num_box_line, grid.num_box_col).hide()
#        
#     grid.set_num_box(10)
#        
#     remaining_players=list(mus.values())
#         
#     barre = Barre()
#     remaining_players = barre.fill(remaining_players)
#     barre.play([ 
#         (-3,6,False),
#         (4,2,True),
#         (6,1,True)]
#         )
#     
#     print(grid)
#        
#     carre = Carre()
#     remaining_players= carre.fill(remaining_players)
#     carre.play([
#         (-2,2,False),
#         (5,5,False)
#         ])
#         
#     print(grid)
#     barre2 = Barre()
#     remaining_players= barre2.fill(remaining_players)
#     barre2.play([
#         (-2,2,False),
#         (5,7,False)
#         ])
#       
#    
#     grid.to_tag("initial", 2)          
#     incr_clock(2)
#     grid.set_num_box(10)
#     remaining_players=list(mus.values())
#     coeur = Coeur()
#     remaining_players=coeur.fill(remaining_players)
#     
#     for player in remaining_players:
#         player.hide()
#     
#     coeur.inside(grid).move(4,4,3)
#     incr_clock(1)
#     print(coeur)
#     coeur.move(1,1,10,3)
#     print(grid)
#     
#     
#     grid.get_box(1, 1, grid.num_box_line, grid.num_box_col).hide()
#     
    
    
    
    
    resource.save("../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Test-API.mlt")
    
    
