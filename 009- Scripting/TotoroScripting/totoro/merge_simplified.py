'''
Created on 6 avr. 2020

@author: SR246418
'''
from totoro.model import merge_files, Resource
from totoro.display import clock, incr_clock
from totoro.utils import set_current_resource


def rotate(container, iteration_par_second, duration):
    iteration_num = iteration_par_second * duration
    iteration_duration = duration / iteration_num
    
    col_size = container.num_box_line -1
    line_size = container.num_box_col -1
    for _ in range(iteration_num):
        col_gauche = container.get_box(1,1,col_size,1)
        ligne_bas =  container.get_box(4,1,1,line_size)
        col_droite =  container.get_box(2,4,col_size,1)
        ligne_haut= container.get_box(1,2,1,line_size)
        
        col_gauche.move(2,1,1,iteration_duration)
        ligne_bas.move(4,2,line_size,iteration_duration)
        col_droite.move(1,4,1,2)
        ligne_haut.move(1,1,line_size,iteration_duration)
        incr_clock(iteration_duration)


if __name__ == '__main__':

    # changer ici les chemin des fichiers à fusionner, rajouter autant de lignes que de fichiers
    merge_files([
        # in
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - percussion.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - barytons.mlt',
#        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - clarinette1.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - cor.mlt',
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - flute et hautbois.mlt',
	    '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - saxophone.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - trombone.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - trompette.mlt',
#         '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1 - tuba.mlt'
        ],
        # out
        '../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Test-API.mlt'
    )


    resource=Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Test-API.mlt')
    set_current_resource(resource)
    instru_map = resource.instru_map
    mus = resource.players_registry
    
    grid = resource.grid
    grid.auto_layout()
    
    
    grid.tag("initial")
    
    
    bottom_line = grid.get_line(4)
    
    clock("00:00:25:00")
    
    bottom_line.move(4,-0.5,1,2)
    
    clock("00:00:30:00")
    column = grid.get_column(1)
    
    column.shift(3, 2)
    
    clock("00:00:32:00")
    grid.get_line(4).shift(3,2)
    
    clock("00:00:34:00")
    grid.get_column(4).shift(-4,2)
    
    
    clock("00:00:36:00")
    column = grid.get_column(4)
    column.move(-4,4,1,2)
    
    clock("00:00:38:00")
    grid.get_box(1,1,4,3).move(1,2,3,1)
    clock("00:00:39:00")
    column.move(-4,1)
    column.move(1,1,1,1)
    
    
    clock("00:00:41:00")
    
  
    mus["Aurianne_saxophone_totoro"].move(4,4,1)
    center_box = grid.get_box(2,2,2,2)
    center_box.auto_layout(0.5)
    
    rotate(grid, 2, 10)
        
    moving_player = grid.get_player(2,1)
    
    for column in range(3):
        other_player = grid.get_player(2,column +2)
        moving_player.swap(other_player)
        incr_clock(2)
         
    grid.to_tag("initial", 2)
    
    resource.save("../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Test-API.mlt")
    
    
