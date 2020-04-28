'''
Created on 24 avr. 2020

@author: SR246418
'''
from totoro.display import Box, incr_clock
from totoro.utils import get_current_resource, get_frame_duration
import math

#Line per seconds
MOVE_DOWN_SPEED = 3
MOVE_SPEED =2

def check_lines(grid):
    first_full_line =0
    lines_to_remove = []
    for line_index in range(grid.num_box_line):
        line = grid.get_line(line_index+1)
        if (len(line.children) == grid.num_box_col):
            if(first_full_line== 0):
                first_full_line = line_index+1
            lines_to_remove.append(line)
    
    if(len(lines_to_remove)>0):    
        incr_clock(1)
        for line in lines_to_remove:
            line.hide()
        incr_clock(0.5)
        for line in lines_to_remove:
            line.show()
        incr_clock(0.5)
        for line in lines_to_remove:
            line.hide()
        incr_clock(0.1)    
        box = grid.get_box(1,1,first_full_line, grid.num_box_col )
        t_move = len(lines_to_remove)/MOVE_DOWN_SPEED
        box.goto(1+len(lines_to_remove), 1, t_move)
        incr_clock(t_move)
        
        
        

class BaseTetrisBox(Box):
    def __init__(self, children, shapes):
        self.shapes = shapes
        self.size = self.get_size()
        Box.__init__(self, children, self.size, self.size)
        
        self.current_shape_index = 0
        self.move_children()
        
        
    
    def fill(self, players, duration = None):
        children_num = min(len(players), self.compute_num_of_children())
        self.children= players[: children_num]
        self.move_children(duration)
        return players[children_num:]

    
    def compute_num_of_children(self):
        num =0
        shape = self.shapes[self.current_shape_index]
        
        for line in shape :
            for  col in line :
                if (col ==1):
                    num +=1
        return num
    
    def get_size(self):
        return len(self.shapes[0][0])
        
    def switch(self):
        self.current_shape_index = (self.current_shape_index +1) % len(self.shapes)
        self.move_children()
        
        
    def move_children(self,duration = None):
        shape = self.shapes[self.current_shape_index]
        child_index = 0
        
        for line_index, line in enumerate(shape) :
            for col_index, col in enumerate(line) :
                if (col ==1):
                    if (child_index < len(self.children)):
                        self.children[child_index].inside(self).goto(line_index+1, col_index+1,duration)
                    child_index+=1
                    
    
    def move_down(self):
        grid = self.get_top_grid()
        min_distance =grid.num_box_line
        max_line =0
        
        for child in self.children :
            child_abs_line, child_abs_col, child_abs_size = grid.to_line_and_cols(*child.get_absolute_coordinates())
            
            max_line = max(max_line, child_abs_line)
            
            for player in get_current_resource().players_registry.values():
                if (player.parent != self and not player.hidden): 
                    player_line, player_col, player_size = grid.to_line_and_cols(*player.get_absolute_coordinates())
                    
                    if(player_col == child_abs_col and player_line > child_abs_line):
                        min_distance = min(min_distance, player_line -(child_abs_line+child_abs_size))
                        
        
        
        if (min_distance == grid.num_box_line):
            min_distance = grid.num_box_line - (max_line)
        
        self_abs_x, self_abs_y, self_abs_size = self.get_absolute_coordinates()
        
        move_down_time = min_distance/MOVE_DOWN_SPEED
        abs_distance = min_distance/grid.num_box_line
        self.inside(grid).prop_move(self_abs_y + abs_distance, self_abs_x, self_abs_size, MOVE_DOWN_SPEED)
        incr_clock(move_down_time)
        check_lines(self.get_top_grid())
        
   
    
    def play(self,moves): 
       
        previous_line, previous_col, switch =moves[0]
        self.inside(self.get_top_grid()).goto(previous_line,previous_col)
        
        if (len(moves) >1) :
            for line, col, switch in moves[1:] :
           
                distance = math.sqrt((line-previous_line)**2+ (col-previous_col)**2)
                self.goto(line, col, distance/MOVE_SPEED)
                incr_clock(distance/(MOVE_SPEED)) 
                if (switch): 
                    self.switch()
                previous_line = line
            
        self.move_down()
            
            
    
    
class Barre(BaseTetrisBox):
    
    def __init__(self, children=[]):
        shapes = [
            [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [1,1,1,1]],
            
            [[1,0,0,0],
             [1,0,0,0],
             [1,0,0,0],
             [1,0,0,0]]
            
            ]
            
        BaseTetrisBox.__init__(self, children, shapes)
    

class Carre(BaseTetrisBox):
    def __init__(self, children=[]):
        shapes = [
            
            [[1,1],
             [1,1]]       
            
            ]
        
        BaseTetrisBox.__init__(self, children, shapes)
       
     
class Te(BaseTetrisBox):
    
    def __init__(self, children=[]):
        shapes = [
            [[0,0,0],
             [1,1,1],
             [0,1,0]],
            
            [[0,1,0],
             [1,1,0],
             [0,1,0]],
            
            [[0,1,0],
             [1,1,1],
             [0,0,0]],
            
            [[0,1,0],
             [0,1,1],
             [0,1,0]]
            
            ]
            
        BaseTetrisBox.__init__(self, children, shapes)

     
class L(BaseTetrisBox):
    
    def __init__(self, children=[]):
        shapes = [
            [[0,0,0],
             [1,1,1],
             [1,0,0]],
            
            [[1,1,0],
             [0,1,0],
             [0,1,0]],
            
            [[0,0,1],
             [1,1,1],
             [0,0,0]],
            
            [[0,1,0],
             [0,1,0],
             [0,1,1]]
            
            ]
            
        BaseTetrisBox.__init__(self, children, shapes)
    
class L_inverse(BaseTetrisBox):
    
    def __init__(self, children=[]):
        shapes = [
            [[0,0,0],
             [1,1,1],
             [0,0,1]],
            
            [[0,1,0],
             [0,1,0],
             [1,1,0]],
            
            [[1,0,0],
             [1,1,1],
             [0,0,0]],
            
            [[0,1,1],
             [0,1,0],
             [0,1,0]]
            
            ]
    
        BaseTetrisBox.__init__(self, children, shapes)
        
        
class Z(BaseTetrisBox):
    
    def __init__(self, children=[]):
        shapes = [
            [[1,1,0],
             [0,1,1],
             [0,0,0]],
            
            [[0,0,1],
             [0,1,1],
             [0,1,0]]
            
           ]
    
        BaseTetrisBox.__init__(self, children, shapes)

        
class S(BaseTetrisBox):
    
    def __init__(self, children=[]):
        shapes = [
            [[0,1,1],
             [1,1,0],
             [0,0,0]],
            
            [[1,0,0],
             [1,1,0],
             [0,1,0]]
            
           ]
    
        BaseTetrisBox.__init__(self, children, shapes)
        
        
class Coeur(BaseTetrisBox):
    def __init__(self, children=[]):
        shapes = [
            [[0,1,1,0,1,1,0],
             [1,1,1,1,1,1,0],
             [0,1,1,1,1,1,0],
             [0,1,1,1,1,0,0],
             [0,0,1,1,1,0,0],
             [0,0,1,1,0,0,0],
             [0,0,0,1,0,0,0]],

           ]
    
        BaseTetrisBox.__init__(self, children, shapes)
    def fill(self, players, duration=None):
        result = BaseTetrisBox.fill(self, players, duration=duration)
        self.get_line(2).inside(self).goto(2,0.5)
        self.get_line(4).inside(self).goto(4,0.5)
        self.get_line(6).inside(self).goto(6,0.5)
        return result
    
    