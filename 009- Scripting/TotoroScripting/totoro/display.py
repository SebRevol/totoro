'''
Created on 17 avr. 2020

@author: SR246418
'''
from totoro.utils import get_time_string, zero_time, frame_duration,\
    get_property, get_frame_duration, get_num_box, get_current_resource
import datetime
from _collections import deque
import math


clock_value = None

def get_clock():
    global clock_value
    return clock_value

def clock(time):
    global clock_value
    clock_value = time
    

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
        self.width_on_height=1
        self.parent = None
        self.inside( get_current_resource().grid)
        
        self.previous_move_times = []
        self.previous_coordinates=[]
    
    def  get_width_on_height(self):
        return 1
    
    def get_absolute_coordinates(self):
        if (type(self.parent) is not Grid):
            (parent_abs_x, parent_abs_y, parent_abs_size) = self.parent.get_absolute_coordinates()
            abs_x = parent_abs_x + self.rel_x*parent_abs_size
            abs_y = parent_abs_y + self.rel_y*parent_abs_size/self.parent.get_width_on_height()
            abs_size = self.rel_size * parent_abs_size
            
            return (abs_x, abs_y, abs_size)
        else :
            return (self.rel_x, self.rel_y, self.rel_size)    
    
    
    def update(self, duration = None):
        self.prop_move(self.rel_y, self.rel_x, self.rel_size, duration)
        
    def inside(self, parent):
        if (self.parent is not None ):
            self.parent._remove_child(self)
            
        self.parent = parent
        parent._add_child(self)
        return self
    
    def update_relative_coordinates(self, line_num, col_num, size_in_cols):
        if (type(line_num)== float):
            line_num +=1
        
        if (type(col_num)== float):
            col_num +=1
        
        self.store_previous_coordinates()
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
    
    def store_previous_coordinates(self):
        self.previous_coordinates.append(
            {"parent": self.parent, "x": self.rel_x, "y": self.rel_y, "size": self.rel_size } )
    
    def to_previous(self, duration=None, history =1):
        previous = self.previous_coordinates[-history]
        self.inside(previous["parent"]).prop_move(previous["y"], previous["x"], previous["size"], duration)
        
        
    def swap(self, other, duration = None):
        other_parent = other.parent
        other_x = other.rel_x
        other_y = other.rel_y
        other_size = other.rel_size

        other.inside(self.parent).prop_move(self.rel_y, self.rel_x, self.rel_size, duration)
        self.inside(other_parent).prop_move(other_y, other_x, other_size, duration)
        
        
    def prop_move(self,vert_ratio, horiz_ratio,size_ratio, duration =None):
        time = get_clock()
        
        if (time is not None):
            self.on(time)
#             if (time in self.previous_move_times):
#                 print("WARNING: {} already moved on time {}".format(self, time) )
#             else :
#                 self.previous_move_times.append(time)
                
        self.store_previous_coordinates()
        self.rel_y = vert_ratio
        self.rel_x = horiz_ratio
        self.rel_size = size_ratio
        
    def move(self,  line_num, col_num,size, duration =None):
        raise NotImplementedError
    
    def on(self, time_string):
        pass
    
    def show(self):
        raise NotImplementedError
    
    def hide(self):
        raise NotImplementedError
    
class Container(object):
    def __init__(self, num_of_lines, num_of_cols, children_names_or_obj=[]):
        self.player_registry = get_current_resource().players_registry
        self.num_box_line =num_of_lines
        self.num_box_col = num_of_cols
        self.children = []
        
        for child_name_or_obj in children_names_or_obj:
            if type(child_name_or_obj) == str :
                child = self.player_registry[child_name_or_obj]
            else: 
                child = child_name_or_obj
            child.inside(self)
            
        
        
       
    
    def _add_child(self, string_or_container_or_player):
        if(type(string_or_container_or_player) == str ):
            player = self.player_registry[string_or_container_or_player]
            if (player not in self.children):
                self.children.append(player)
        else :
            if (string_or_container_or_player):
                self.children.append(string_or_container_or_player) 
    
    
    def _remove_child(self,string_or_container_or_player):
        if(type(string_or_container_or_player) == str ):
            player = self.player_registry[string_or_container_or_player]
            self.children.remove(player)
        else :
            self.children.remove(string_or_container_or_player) 
    
    
    def auto_layout(self, duration = None):
        self.compute_line_and_cols()
        if (self.num_box_line == 1):
            new_child = Line(self.children)
            new_child.inside(self).move(1,1,self.num_box_col, duration)
        else :
            child_num = len(self.children)
            number_of_middle_lines = self.num_box_col *(self.num_box_line-2)/self.num_box_col
            num_of_remaing_children = child_num -(number_of_middle_lines* self.num_box_col)
            
            number_of_elements_in_first = math.ceil(num_of_remaing_children/2)
            number_of_elements_in_last = math.floor(num_of_remaing_children/2)
            
            children_to_locate = self.children.copy()
            
            first_line = Line(children_to_locate[:number_of_elements_in_first])
            first_line.inside(self).prop_move(0, (self.num_box_col-number_of_elements_in_first)/(2*self.num_box_col),number_of_elements_in_first/ self.num_box_col, duration)
            
            index_of_last_players = child_num - number_of_elements_in_last
            start_index= number_of_elements_in_first
            
            line_index= 2
            while(start_index <index_of_last_players) :
                new_line = Line(children_to_locate[start_index:start_index +self.num_box_col ])
                new_line.inside(self).move(line_index, 1, self.num_box_col)
                start_index+= self.num_box_col
                line_index +=1
            
            last_line = Line(children_to_locate[index_of_last_players:])
            last_line.inside(self).prop_move((line_index-1)/self.num_box_line, (self.num_box_col-number_of_elements_in_last)/(2*self.num_box_col),number_of_elements_in_last/ self.num_box_col, duration)
            
                
    
    def compute_line_and_cols(self):
        child_num= len(self.children)
        if (self.num_box_line ==0 and self.num_box_col ==0):
            self.num_box_col =  get_num_box(child_num)
            self.num_box_line = get_num_box(child_num)
        elif (self.num_box_col ==0) :
            self.num_box_col = math.ceil(child_num/self.num_box_line)
        elif (self.num_box_line ==0):
            self.num_box_line = math.ceil(child_num/self.num_box_col)
            
            

class Box(DisplayedElement, Container):
    
    def __init__(self, children_names=[], num_of_lines = 0, num_of_cols=0):
        Container.__init__(self, num_of_lines, num_of_cols,children_names)
        DisplayedElement.__init__(self)
        
        
    
    def get_width_on_height(self):
        if (self.num_box_line == 0):
            self.auto_layout()
        return self.num_box_col/self.num_box_line
        
    def at(self, line_num, col_num,size):
        self.update_relative_coordinates(line_num, col_num, size);
        for child in self.children :
            child.update()
    
    def prop_move(self,rel_y, rel_x,rel_size, duration =None):
        DisplayedElement.prop_move(self,rel_y, rel_x, rel_size, duration)
       
        
        for child in self.children :
            child.update(duration)
            
        
    def move(self,  line_num, col_num,size, duration =None):
        self.auto_layout_if_needed()
        
        self.update_relative_coordinates(line_num, col_num, size);
        
        for child in self.children :
            child.update(duration)
    
    def auto_layout_if_needed(self):
        if (self.num_box_col == 0 or self.num_box_line ==0):
            self.auto_layout()
    
    def on(self, time_string):
        super().on(time_string)
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
    def __init__(self,children_names):
        self.size_init = len(children_names)
        self.children = None
        super().__init__(children_names,self.get_num_of_lines(),self.get_num_of_columns())
        self.children = deque(self.children)
    
    def get_size(self):
        return len(self.children)
    
    def get_num_of_lines(self):
        raise NotImplementedError
    
    def get_num_of_columns(self):
        raise NotImplementedError
    
    def move_child(self, player, index, duration = None):
        raise NotImplementedError
        
    def at(self, line_num, col_num, size=None):
        if size is None :
            size = self.get_num_of_columns()
        self.update_relative_coordinates(line_num, col_num, size)
        for index, child in enumerate(self.children):
            self.move_child(child, index+1)
            
    def move(self, line_num, col_num, size=None, duration=None):
        if size is None :
            size = self.get_num_of_columns()
        self.update_relative_coordinates(line_num, col_num, size)
        for index, child in enumerate(self.children):
            self.move_child(child, index+1, duration)
        
    def prop_move(self, rel_y, rel_x, rel_size, duration=None):
        DisplayedElement.prop_move(self,rel_y, rel_x, rel_size, duration)
        
        for index, child in enumerate(self.children):
            self.move_child(child, index+1,duration)
    
    def shift(self, num_of_box, duration):
        self.children.rotate(num_of_box)
        for index, child in enumerate (self.children) :
            self.move_child(child, index+1,duration)
    


class Column(LineOrColumn):
    def get_num_of_lines(self):
        if (self.children is not None):
            return self.get_size()
        return self.size_init
    
    def get_num_of_columns(self):
        return 1
    
    def move_child(self, child, index, duration = None):
        child.move(index, 1,1, duration)
    
    
class Line(LineOrColumn):
    def get_num_of_lines(self):
        return 1
    
    def get_num_of_columns(self):
        if (self.children is not None):
            return self.get_size()
        return self.size_init
    
    def move_child(self, child, index,duration=None):
        child.move(1,index,1,duration)