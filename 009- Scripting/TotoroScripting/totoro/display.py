'''
Created on 17 avr. 2020

@author: SR246418
'''
from totoro.utils import get_time_string, zero_time, frame_duration,\
    get_property, get_frame_duration
import datetime
from _collections import deque




    
class Grid_old(object):
    def __init__(self, res_x, res_y, num_box=1, x_margin=0) :
        self.res_x = res_x
        self.res_y = res_y
        self.set_num_box(num_box)
        self.set_margin(x_margin)
       
        
    def set_margin(self, x_margin):
         
        self.x_margin = x_margin
        self.y_margin = int(self.res_y*self.x_margin/self.res_x)
        
        
    def set_num_box(self, num_box):
        self.num_box = num_box
        self.xoffset = self.res_x/self.num_box
        self.yoffset = self.res_y/self.num_box
        
    def get_position(self,line_num, col_num, size):
        x = int(self.xoffset *(col_num-1) +self.x_margin/2)
        y = int(self.yoffset *(line_num-1) +self.y_margin/2)
        x_width = int(size *self.xoffset-self.x_margin)
        y_width = int(size * self.yoffset-self.y_margin)
        
        return  "{} {} {} {} 1".format(x, y, x_width, y_width)
    
    def get_position_analog(self,line_num, col_num, size):
        x = int(self.res_x *col_num) 
        y = int(self.res_y *line_num)
        x_width = int(size *self.res_x)
        y_width = int(size * self.res_y)
        
        return  "{} {} {} {} 1".format(x, y, x_width, y_width)
    
    def locate(self, producers, line_num, col_num,size):
        target_position =self.get_position(line_num, col_num, size)
        
        for prod in producers:
            prod.set_position(target_position)
    
    def animate(self, producers, current_position, line_num, col_num, size, duration):
        target_position =self.get_position(line_num, col_num, size)
        
        duration_delta = get_time_string(zero_time + datetime.timedelta(seconds = duration))
        duration_minus_frame = get_time_string(zero_time + datetime.timedelta(seconds = duration -frame_duration.seconds))
        
        zero_time_string = get_time_string(zero_time)
        first_producer =producers[0]
        
        position_with_anim ="{}={};{}={}".format(zero_time_string, current_position, duration_minus_frame, target_position)
        first_producer.set_position(position_with_anim)
        anim_in_node = get_property(first_producer.position_filter_node, "shotcut:animIn")
        anim_in_node.text = duration_delta
        
        if len(producers)>1:
            for prod in producers[1:]:
                prod.set_position(target_position)
        


class DisplayedElement(object):
    
    def __init__(self):
        self.rel_x = 0
        self.rel_y=0
        self.rel_size =1
        self.parent = None
    
    def get_absolute_coordinates(self):
        if (type(self.parent) is not Grid):
            (parent_abs_x, parent_abs_y, parent_abs_size) = self.parent.get_absolute_coordinates()
            abs_x = parent_abs_x + self.rel_x*parent_abs_size
            abs_y = parent_abs_y + self.rel_y*parent_abs_size
            abs_size = self.abs_size * parent_abs_size
            
            return (abs_x, abs_y, abs_size)
        else :
            return (self.rel_x, self.rel_y, self.rel_size)    
    
    
    def update(self, duration = None):
        self.prop_move(self.rel_y, self.rel_x, self.rel_size, duration)
        
    def inside(self, parent):
        self.parent = parent
        parent._add_child(self)
        return self
    
    def update_relative_coordinates(self, line_num, col_num, size_in_cols):
        if (type(line_num)== float):
            line_num +=1
        
        if (type(col_num)== float):
            col_num +=1
        
        self.rel_x = (col_num-1)/self.parent.num_box_col
        self.rel_y = (line_num-1)/self.parent.num_box_line
        self.rel_size = size_in_cols/self.parent.num_box_col
        
    
    
    def get_top_grid(self):
        if type(self.parent) == Grid :
            return self.parent
        else :
            return self.parent.get_top_grid() 


    def at(self, line_num, col_num,size):
        raise NotImplementedError        
    
    def prop_move(self,vert_ratio, horiz_ratio,size_ratio, duration =None):
        raise NotImplementedError
    
    def move(self,  line_num, col_num,size, duration =None):
        raise NotImplementedError
    
    def on(self, time_string):
        raise NotImplementedError
    
    def show(self):
        raise NotImplementedError
    
    def hide(self):
        raise NotImplementedError
    
class Container(object):
    def __init__(self, num_of_lines, num_of_cols,player_registry= None, children_names=[]):
        self.player_registry = player_registry
        self.num_box_line =num_of_lines
        self.num_box_col = num_of_cols
        self.children = []
        
        for child in [self.player_registry[name] for name in children_names] :
            child.inside(self)
    
    def _add_child(self, string_or_container_or_player):
        if(type(string_or_container_or_player) == str ):
            player = self.player_registry[string_or_container_or_player]
            self.children.append(player)
        else :
            self.children.append(string_or_container_or_player) 
    

class Box(DisplayedElement, Container):
    
    def __init__(self, num_of_lines, num_of_cols, player_registry= None,children_names=[]):
        Container.__init__(self, num_of_lines, num_of_cols, player_registry,children_names)
        DisplayedElement.__init__(self)
        
        
    def at(self, line_num, col_num,size):
        self.update_relative_coordinates(line_num, col_num, size);
        for child in self.children :
            child.update()
    
    def prop_move(self,rel_y, rel_x,rel_size, duration =None):
        self.rel_y = rel_y
        self.rel_x = rel_x
        self.rel_size = rel_size
        
        for child in self.children :
            child.update(duration)
            
        
    def move(self,  line_num, col_num,size, duration =None):
        self.update_relative_coordinates(line_num, col_num, size);
        
        for child in self.children :
            child.update(duration)
    
    def on(self, time_string):
        for child in self.children:
            child.on(time_string)
        return self
        
    def show(self):
        for child in self.children :
            child.show()
            
    def hide(self):
        for child in self.children :
            child.hide()


class Grid(Container):
    
    def __init__(self, res_x, res_y, num_box=1, x_margin=0) :
        super().__init__(num_box, num_box, [])
        self.res_x = res_x
        self.res_y = res_y
        self.set_num_box(num_box)
        self.set_margin(x_margin)
            

    def set_num_box(self, num_box):
        self.num_box_col = num_box
        self.num_box_line = num_box
        
    def set_margin(self, x_margin):
        self.x_margin = x_margin
        self.y_margin = int(self.res_y*self.x_margin/self.res_x)
        
    
    def get_position(self,abs_y,abs_x , size):
        x = int(self.res_x *abs_x) 
        y = int(self.res_y *abs_y)
        x_width = int(size *self.res_x)
        y_width = int(size * self.res_y)
        
        return  "{} {} {} {} 1".format(x, y, x_width, y_width)
   
    
    def locate(self, producers, player):
        abs_x, abs_y, abs_size = player.get_absolute_coordinates()
        self.locate_wit_coord(producers, abs_y, abs_x, abs_size)
        
    
    def locate_wit_coord(self, producers, abs_y, abs_x, abs_size):
        target_position =self.get_position(abs_y, abs_x, abs_size)
        
        for prod in producers:
            prod.set_position(target_position)
    
    
    def animate(self, producers, player,current_position_string, duration):
        target_abs_x, target_abs_y, target_size = player.get_absolute_coordinates()
        
        
        target_position =self.get_position(target_abs_y, target_abs_x, target_size)
        
        duration_delta = get_time_string(zero_time + datetime.timedelta(seconds = duration))
        duration_minus_frame = get_time_string(zero_time + datetime.timedelta(seconds = duration -get_frame_duration().seconds))
        
        zero_time_string = get_time_string(zero_time)
        first_producer =producers[0]
        
        position_with_anim ="{}={};{}={}".format(zero_time_string, current_position_string, duration_minus_frame, target_position)
        first_producer.set_position(position_with_anim)
        anim_in_node = get_property(first_producer.position_filter_node, "shotcut:animIn")
        anim_in_node.text = duration_delta
        
        if len(producers)>1:
            for prod in producers[1:]:
                prod.set_position(target_position)
        

class LineOrColumn(Box):
    def __init__(self,player_registry,children_names):
        self.size = len(children_names)
        super().__init__(self.get_num_of_lines(),self.get_num_of_columns(), player_registry, children_names)
        self.children = deque(self.children)
    
    def get_num_of_lines(self):
        raise NotImplementedError
    
    def get_num_of_columns(self):
        raise NotImplementedError
    
    def move_child(self, player, index, duration = None):
        raise NotImplementedError
        
    def at(self, line_num, col_num, size):
        self.update_relative_coordinates(line_num, col_num, size)
        for index, child in enumerate(self.children):
            self.move_child(child, index)
            
    def move(self, line_num, col_num, size, duration=None):
        self.update_relative_coordinates(line_num, col_num, size)
        for index, child in enumerate(self.children):
            self.move_child(child, index, duration)
        
    def prop_move(self, rel_y, rel_x, rel_size, duration=None):
        self.rel_y = rel_y
        self.rel_x = rel_x
        self.rel_size = rel_size
        
        for index, child in enumerate(self.children):
            self.move_child(child, index,duration)
    
    def shift(self, num_of_box, duration):
        self.children.rotate(num_of_box)
        for index, child in enumerate (self.children) :
            self.move_child(child, index,duration)
    


class Column(LineOrColumn):
    def get_num_of_lines(self):
        return self.size
    
    def get_num_of_columns(self):
        return 1
    
    def move_child(self, child, index, duration = None):
        child.move(index, 1,1, duration)
    
    
class Line(Box):
    def get_num_of_lines(self):
        return 1
    
    def get_num_of_columns(self):
        return self.size
    
    def move_child(self, child, index,duration=None):
        child.move(1,index,1,duration)