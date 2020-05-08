'''
Created on 17 avr. 2020

@author: SR246418
'''
from builtins import isinstance
import datetime
import math
from string import ascii_lowercase, ascii_uppercase

from totoro.utils import get_time_string, zero_time, \
    get_property, get_frame_duration, get_num_box, get_current_resource, \
    get_time_from_user_string, get_user_string_from_time, parse_position, \
    get_nearest_frame_date, get_nearest_frame_duration




clock_value = None


letters = ascii_uppercase
letters+=ascii_lowercase

def get_box_from_players(container, line_pos, col_pos, num_of_lines, num_of_cols):
    result = Box([],num_of_lines,num_of_cols)
    
    result.inside(container).goto(line_pos,col_pos )
    for line in range(num_of_lines) :
            for col in range (num_of_cols):
                player = container.get_player(line_pos +line, col_pos+col)
                player.inside(result).move(line+1, col+1, 1)    
    
    return result



def rotate(container, iteration_par_second, duration):
    iteration_num = int(iteration_par_second * duration)
    iteration_duration = duration / iteration_num
    
    col_size = container.num_box_line -1
    line_size = container.num_box_col -1
    for _ in range(iteration_num):
        col_gauche = get_box_from_players(container,1,1,col_size,1)
        ligne_bas =  get_box_from_players(container,col_size+1,1,1,line_size)
        col_droite =  get_box_from_players(container,2,line_size+1,col_size,1)
        ligne_haut= get_box_from_players(container,1,2,1,line_size)
#         

        
        col_gauche.inside(container).goto(2,1,iteration_duration)
        ligne_bas.inside(container).goto(col_size+1,2,iteration_duration)
        col_droite.inside(container).goto(1,line_size+1,iteration_duration)
        ligne_haut.inside(container).goto(1,1,iteration_duration)
        incr_clock(iteration_duration)
        
        
def rotate_clock(container, iteration_par_second, duration):
    iteration_num = int(iteration_par_second * duration)
    iteration_duration = duration / iteration_num
    
    col_size = container.num_box_line -1
    line_size = container.num_box_col -1
    for _ in range(iteration_num):
        col_gauche = get_box_from_players(container,2,1,col_size,1)
        ligne_bas =  get_box_from_players(container,col_size+1,2,1,line_size)
        col_droite =  get_box_from_players(container,1,line_size+1,col_size,1)
        ligne_haut= get_box_from_players(container,1,1,1,line_size)
        
        col_gauche.goto(1,1,iteration_duration)
        ligne_bas.goto(col_size+1,1,iteration_duration)
        col_droite.goto(2,line_size+1,iteration_duration)
        ligne_haut.goto(1,2,iteration_duration)
        incr_clock(iteration_duration)



def hide_all(to_hide=None):
    if (to_hide == None):
        to_hide = list( get_current_resource().players_registry.values())
    for player in to_hide:
        player.hide()
    

def get_short_name(name):
    if ("_totoro" in name):
        return name[:name.index('_totoro')]
    else :
        return name
    

def get_player_char (player):
    if (player == None):
        return " "
    else :
        sorted_player_names = list(get_current_resource().players_registry.keys())
        sorted_player_names.sort()
        return letters[sorted_player_names.index(player.name)]
    
def get_player_name_from_char(char):
    sorted_player_names = list(get_current_resource().players_registry.keys())
    sorted_player_names.sort()
    return get_short_name(sorted_player_names[letters.index(char)])

def print_legend():
    sorted_player_names = list(get_current_resource().players_registry.keys())
    sorted_player_names.sort()
    for player_name in sorted_player_names :
        print(" {} : {}".format(get_player_char(get_current_resource().players_registry[player_name]),player_name ) )
    

def get_clock():
    global clock_value
    return clock_value


def get_duration_clock():
    global clock_value
    time = get_time_from_user_string(clock_value)
    return time -zero_time
    
    
def clock(time):
    global clock_value
    clock_value = time
    

def incr_clock(seconds):
    global clock_value
    time = get_time_from_user_string(clock_value)
    time += datetime.timedelta(seconds = seconds)
    clock_value = get_user_string_from_time(time)


class DisplayedElement(object):
    
    def __init__(self):
        self.rel_x = 0
        self.rel_y=0
        self.rel_size =1
        self.width_on_height=1
        self.parent = None
        self.inside( get_current_resource().grid)
        self.hidden =False
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
        
    def inside(self, parent, index = None):
        if (self.parent is not None and self.parent != parent):
            self.parent._remove_child(self)
            
        self.parent = parent
        parent._add_child(self, index)
        return self
    
    def update_relative_coordinates(self, line_num, col_num, size_in_cols):
        if (int(line_num)!= line_num):
            line_num +=1
        
        if (int(col_num)!= col_num):
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
            {"parent": self.parent, "index":self.parent.children.index(self) ,  "x": self.rel_x, "y": self.rel_y, "size": self.rel_size } )
    
    def to_previous(self, duration=None, history =1):
        previous = self.previous_coordinates[-history]
        self.inside(previous["parent"], previous["index"]).prop_move(previous["y"], previous["x"], previous["size"], duration)
        
        
    def swap(self, other, duration = None):
        other_parent = other.parent
        other_index =other.parent.children.index(other)
        other_x = other.rel_x
        other_y = other.rel_y
        other_size = other.rel_size

        other.inside(self.parent, self.parent.children.index(self)).prop_move(self.rel_y, self.rel_x, self.rel_size, duration)
        self.inside(other_parent, other_index).prop_move(other_y, other_x, other_size, duration)
        
        
    def prop_move(self,vert_ratio, horiz_ratio,size_ratio, duration =None):
        time = get_clock()
        if (self.hidden):
            self.hidden = False
        
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

    def goto(self, line, col, duration):
        raise NotImplementedError
            
    def move(self,  line_num, col_num,size, duration =None):
        raise NotImplementedError
    
    def on(self, time_string):
        pass
    
    def show(self):
        self.hidden = False
    
    def hide(self):
        self.hidden = True
    
class Container(object):
    def __init__(self, num_of_lines, num_of_cols, children_names_or_obj=[]):
        self.player_registry = get_current_resource().players_registry
        self.num_box_line =num_of_lines
        self.num_box_col = num_of_cols
        self.children = []
        
        self.tag_map = {}
        
        for child_name_or_obj in children_names_or_obj:
            if type(child_name_or_obj) == str :
                child = self.player_registry[child_name_or_obj]
            else: 
                child = child_name_or_obj
            child.inside(self)

    def fill(self, players, duration = None):
        index = 0
        for line in range(self.num_box_line) :
            for col in range(self.num_box_col):
                if(index < len(players)):
                    players[index].inside(self).goto(line+1, col+1, duration)
                    index+=1
        return players[index:]

    def add_players_covered_by_box(self, box):
        for player in self.player_registry.values():
            if box.is_over(player):
                (rel_x, rel_y, rel_size)= box.get_relative_coordinates(player)
                player.inside(box).prop_move( rel_y,rel_x, rel_size)
        
    
    def get_players(self):
        result =set([])
        for child in self.children :
            if( isinstance(child, Container)):
                result.update(child.get_players())
            else :
                result.add(child)
        return list(result)
    
    def to_line_and_cols(self, rel_x, rel_y, rel_size):
        line = round(rel_y*self.num_box_line +1,2)
        col =  round(rel_x*self.num_box_col +1,2)
        size =  round(rel_size *self.num_box_col,2)
        
        return (line, col, size)
    
    def get_player(self, line, col):
        box = Box([], 1,1)
        box.inside(self).move(line, col, 1)
        result = None
        for player in self.player_registry.values():
            if (box.is_over(player)):
                result= player
        self._remove_child(box)
        
        return result
        
    def get_partial_player(self, line, col):
        box = Box([], 1,1)
        box.inside(self).move(line, col, 1)
        result = None
        for player in self.player_registry.values():
            if (box.is_partially_over(player)):
        
                result = player
        self._remove_child(box)
        return result
    
    
    def get_box(self, line_index, col_index, num_of_lines, num_of_cols):
        box = Box([], num_of_lines, num_of_cols )
        box.inside(self).move(line_index, col_index, num_of_cols)
        self.add_players_covered_by_box(box)
       
        return box
    
    def get_line(self, line_index, num_of_cols = None):
        if num_of_cols ==None :
            num_of_cols = self.num_box_col
            
        line = Line([], num_of_cols)
        
        line.inside(self).move(line_index, 1)
        self.add_players_covered_by_box(line)
        return line
        
    def get_column(self, col_index, num_of_lines = None):
        if num_of_lines ==None :
            num_of_lines = self.num_box_line
            
        column = Column([], num_of_lines)
        column.inside(self).move(1, col_index)
        self.add_players_covered_by_box(column)
        return column
    

    
    def tag(self, tag_name):
        config = {}
        config["children"] = self.children.copy()
        children_pos ={}
        for child in self.children :
            children_pos[child] = {"x": child.rel_x, "y": child.rel_y, "size": child.rel_size, "hidden":child.hidden}
        
        config["children_pos"]=children_pos
        config["num_box_line"]= self.num_box_line
        config["num_box_col"]= self.num_box_col
        
        
        self.tag_map[tag_name]= config
        
        
        for child in self.children :
            if isinstance(child, Container):
                child.tag(tag_name)
    
    
    def to_tag(self, tag_name, duration=None):
        config = self.tag_map.get(tag_name)
        if config is None :
            print("ERROR : tag {} inconnu pour {}".format(tag_name, self))
        
        self.num_box_line = config["num_box_line"] 
        self.num_box_col  = config["num_box_col"]  

        self.children.clear()#) = config["children"].copy()
        
        for child in config["children"] :
            child_pos = config["children_pos"][child]
            child.inside(self).prop_move(child_pos["y"], child_pos["x"], child_pos["size"], duration)
            if(child_pos["hidden"]):
                child.hide()
        
        for child in self.children :
            if isinstance(child, Container):
                child.to_tag(tag_name, duration)
                
                
    
    def children_to_previous(self, duration = None, history =1 ):
        for child in self.children :
            child.to_previous(duration, history)
        
       
    
    def _add_child(self, string_or_container_or_player, index=None):
            
        if(type(string_or_container_or_player) == str ):
            player = self.player_registry[string_or_container_or_player]
            
        else  : 
            player = string_or_container_or_player
        
        if (player not in self.children):        
            if (index is None) :
                index = len(self.children)
        
            self.children.insert(index, player)
        else :
            if (index is not None):
                current_index = self.children.index(player)
                if (index != current_index):
                    self.children.remove(player)
                    self.children.insert(index,player)
        
    
    def _remove_child(self,string_or_container_or_player):
        if(type(string_or_container_or_player) == str ):
            player = self.player_registry[string_or_container_or_player]
            if (player  in self.children):
                self.children.remove(player)
        else :
            if (string_or_container_or_player in self.children):    
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
            
            first_line = Line([], len(children_to_locate[:number_of_elements_in_first]))
            first_line.inside(self).prop_move(0, (self.num_box_col-number_of_elements_in_first)/(2*self.num_box_col),number_of_elements_in_first/ self.num_box_col)
            first_line.add_players(children_to_locate[:number_of_elements_in_first], duration)
            
            index_of_last_players = child_num - number_of_elements_in_last
            start_index= number_of_elements_in_first
            
            line_index= 2
            while(start_index <index_of_last_players) :
                new_line = Line([], len(children_to_locate[start_index:start_index +self.num_box_col ]))
                new_line.inside(self).move(line_index, 1, self.num_box_col)
                new_line.add_players(children_to_locate[start_index:start_index +self.num_box_col ],duration)
                start_index+= self.num_box_col
                line_index +=1
            
            last_line = Line([],len(children_to_locate[index_of_last_players:]))
            last_line.inside(self).prop_move((line_index-1)/self.num_box_line, (self.num_box_col-number_of_elements_in_last)/(2*self.num_box_col),number_of_elements_in_last/ self.num_box_col, duration)
            last_line.add_players(children_to_locate[index_of_last_players:],duration)
                
    
    def compute_line_and_cols(self):
        child_num= len(self.children)
        if (self.num_box_line ==0 and self.num_box_col ==0):
            self.num_box_col =  get_num_box(child_num)
            self.num_box_line = get_num_box(child_num)
        elif (self.num_box_col ==0) :
            self.num_box_col = math.ceil(child_num/self.num_box_line)
        elif (self.num_box_line ==0):
            self.num_box_line = math.ceil(child_num/self.num_box_col)
            
            
    def get_line_separator(self):
        result = '  '
        for col in range (self.num_box_col) :
            result+='|---'
        result +='|\n'
        return result
    
    def get_first_line(self):
        result = '  '
        for col in range (self.num_box_col) :
            result+='|{}-'.format(str(col+1).zfill(2))
        result +='|\n'
        return result
        
        
    def get_col(self, line_index, col_index):
        player = self.get_partial_player(line_index, col_index)
        player_char = get_player_char(player)
        if( player is not None):
            mapping = player_char+":"+get_short_name(player.name)
        else :
            mapping = None
        return "| "+player_char+" ",mapping
        
    def __str__(self, *args, **kwargs):
        result = "===================================================================================================================\n"
        result +="\n"
        result +="Time : "+get_clock()+"\n"
        result+= self.get_first_line()
        for line_index in range(self.num_box_line) :
            result +=self.get_line_separator()
            result+=str(line_index+1).zfill(2)
            player_mappings = set([])
            for col_index in range(self.num_box_col):
                col_text, player_mapping =self.get_col(line_index+1, col_index+1)
                if(player_mapping is not None):
                    player_mappings.add(player_mapping)
                result+= col_text
            
            mapping=",".join(player_mappings)
            result +="|"+str(line_index+1).zfill(2)+"   "+mapping+"\n"
            
        result +=self.get_line_separator()
        result+= self.get_first_line()
        
        
        
        return result



class Box(DisplayedElement, Container):
    
    def __init__(self, children_names=[], num_of_lines = 0, num_of_cols=0):
        Container.__init__(self, num_of_lines, num_of_cols,children_names)
        DisplayedElement.__init__(self)
        
     
    
    def get_relative_coordinates(self, display_element):
        elem_abs_x, elem_abs_y, elem_abs_size = display_element.get_absolute_coordinates()
        self_abs_x, self_abs_y, self_abs_size = self.get_absolute_coordinates()
        
        rel_x = (elem_abs_x- self_abs_x)/self_abs_size
        rel_y = (elem_abs_y- self_abs_y)/(self_abs_size/self.get_width_on_height())
        rel_size = elem_abs_size/self_abs_size
        
        return (rel_x, rel_y,rel_size)
        
        
    def is_over(self, displayed_element):
        rel_x, rel_y,rel_size = self.get_relative_coordinates(displayed_element)
        
        rel_x = round(rel_x,2)
        rel_y = round(rel_y,2)
        rel_size = round(rel_size,2)
        
#         #2 pixels de marge d'erreur
#         x_eps = 2/get_current_resource().x_res
#         y_eps = 2/get_current_resource().y_res
#         
        return ( 
            not displayed_element.hidden and
            rel_x>=0 and rel_x +rel_size<=1 and 
            rel_y >=0 and rel_y+rel_size <=(1)/self.get_width_on_height())
                 
        
    def is_partially_over (self, displayed_element):
        rel_x, rel_y,rel_size = self.get_relative_coordinates(displayed_element)
        
        rel_x = round(rel_x,2)
        rel_y = round(rel_y,2)
        rel_size = round(rel_size,2)
        #2 pixels de marge d'erreur
        x_eps = 2/get_current_resource().x_res
        y_eps = 2/get_current_resource().y_res
        
        result = (  not displayed_element.hidden and
            rel_x <1 and rel_x+rel_size > 0 and 
            rel_y<1 and rel_y+(rel_size/self.get_width_on_height()) > 0)
        return result
          
            

    
    def get_width_on_height(self):
        if (self.num_box_line == 0):
            self.auto_layout()
        return self.num_box_col/self.num_box_line
        
    def at(self, line_num, col_num,size):
        self.update_relative_coordinates(line_num, col_num, size);
        for child in self.children :
            child.update()
    
    
    def expand(self, ratio, expand_children=False, duration=None):
        new_size = ratio*self.rel_size

        self.rel_x = self.rel_x+(self.rel_size/2)*(1-ratio)
        self.rel_y = self.rel_y+(self.rel_size/2)*(1-ratio)/self.get_width_on_height()
        
        self.rel_size =new_size
        
        if (not expand_children):
            for child in self.get_players() :
                child.rel_size = child.rel_size/ratio
        
        self.update(duration)
        
    
    def prop_move(self,rel_y, rel_x,rel_size, duration =None):
        DisplayedElement.prop_move(self,rel_y, rel_x, rel_size, duration)
       
        
        for child in self.children :
            if (not child.hidden):
                child.update(duration)
            
    
    def goto(self, line_num, col_num, duration=None):
        self.move(line_num, col_num, self.num_box_col, duration)
        
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
        DisplayedElement.show(self)
        for child in self.children :
            child.show()
            
    def hide(self):
        DisplayedElement.hide(self)
        for child in self.children :
            child.hide()

   
    def v_shift(self, num_of_box, duration=None):
        
        if num_of_box <0 :
            offset =-1
            jump_start = 1
            jump_to = self.num_box_line
        else :
            offset =1
            jump_start = self.num_box_line
            jump_to = 1
        
        if (duration != None):
            single_duration = abs(duration/num_of_box)
        else :
            single_duration=None
      
        
        jumping = None
        for i in range(abs(num_of_box)):
            for  child in self.children :
                child_line, child_col, child_size = self.to_line_and_cols(*self.get_relative_coordinates(child))
                if(child_line!=jump_start):
                    child.goto(child_line+offset, child_col, single_duration)
                else:
                    #child.goto(child_line+before_jump_offset, child_col, jump_duration)
                    child.goto(child_line+offset, child_col, single_duration)
                    jumping = child
                
            incr_clock(single_duration)
                    
            if (jumping is not None) :
                jumping.goto(jump_to,child_col)
             
        incr_clock(-(single_duration)*abs(num_of_box))
                    
        
    def h_shift(self, num_of_box, duration=None):
        
        if num_of_box <0 :
            offset =-1
            jump_start = 1
            jump_to = self.num_box_col
        else :
            offset =1
            jump_start = self.num_box_col
            jump_to = 1
        
        if (duration != None):
            single_duration = abs(duration/num_of_box)
        else :
            single_duration=None
      
        
        jumping = None
        for i in range(abs(num_of_box)):
            for  child in self.children :
                child_line, child_col, child_size = self.to_line_and_cols(*self.get_relative_coordinates(child))
                if(child_col!=jump_start):
                    child.goto(child_line, child_col+offset, single_duration)
                else:
                    child.goto(child_line, child_col+offset, single_duration)
                    #child.goto(child_line, child_col+before_jump_offset, jump_duration)
                    jumping = child
                
            incr_clock(single_duration)
                    
            if (jumping is not None) :
                jumping.goto(child_line,jump_to)
                
        incr_clock(-(single_duration)*abs(num_of_box))
            


class Grid(Container):
    
    def __init__(self, res_x, res_y, num_box=0, x_margin=0) :
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
        
    
    def get_position(self,abs_x ,abs_y, size):
        x = int(self.res_x *abs_x)+ self.x_margin/2
        y =int(self.res_y *abs_y)+self.y_margin/2
        x_width =int(size *self.res_x)+1- self.x_margin/2
        y_width = int(size * self.res_y)+1-self.y_margin/2
        
        return  "{} {} {} {} 1".format(x, y, x_width, y_width)
   
    
    def locate(self, producers, player):
        abs_x, abs_y, abs_size = player.get_absolute_coordinates()
        self.locate_wit_coord(producers, abs_x,abs_y,  abs_size)
        
    
    def locate_wit_coord(self, producers,  abs_x, abs_y,abs_size):
        target_position =self.get_position(abs_x,abs_y,  abs_size)
        
        for prod in producers:
            prod.set_position(target_position)
    
    
    def animate(self, producers, player,current_position_string, duration):
        
        duration = datetime.timedelta(seconds=get_nearest_frame_duration(duration))
        target_tuple = player.get_absolute_coordinates()
        start_tuple =parse_position(current_position_string)
        
        
        #duration_delta = get_time_string(zero_time + datetime.timedelta(seconds = duration))
        #duration_minus_frame = get_time_string(zero_time + datetime.timedelta(seconds = duration -get_frame_duration().seconds))
        
        producer_index =0
        current_producer =  producers[producer_index]
        current_entry= current_producer.entry
        animation_end_time =current_entry.start_time +duration
        animation_start_time = current_entry.start_time
        
        current_position_tuple = start_tuple
        
        zero_time_string = get_time_string(zero_time)
        
        while(animation_end_time>current_entry.get_end_time() ) :
            sub_duration_minus_frame = current_entry.get_duration() 
            sub_duration_minus_frame_string =get_time_string(zero_time+ sub_duration_minus_frame)
            sub_duration = sub_duration_minus_frame + get_frame_duration()
            sub_position_tuple = self.interpolate(start_tuple, target_tuple,animation_start_time, duration, current_entry.get_end_time()+get_frame_duration())
            
            
            current_position_string = self.get_position(*current_position_tuple)
            sub_position_string = self.get_position(*sub_position_tuple)
            
            position_with_anim ="{}={};{}={}".format(zero_time_string, current_position_string, sub_duration_minus_frame_string, sub_position_string)
            current_producer.set_position(position_with_anim)
            anim_in_node = get_property(current_producer.position_filter_node, "shotcut:animIn")
            anim_in_node.text = get_time_string(zero_time+sub_duration)   
            
            #current_position_tuple =sub_position_tuple
            current_position_tuple =self.interpolate(start_tuple, target_tuple,animation_start_time, duration-2*get_frame_duration(), current_entry.get_end_time()+get_frame_duration()) 
            
            producer_index +=1
            current_producer =  producers[producer_index]
            current_entry= current_producer.entry
            
        
        #on est dans la dernière entrée qui doit être animée
        target_position_string= self.get_position(*target_tuple)
        
        current_position_string = self.get_position(*current_position_tuple)
        last_duration = animation_end_time-current_entry.start_time
        last_duration_minus_frame = last_duration - get_frame_duration()
        last_duration_minus_frame_string = get_time_string(zero_time + last_duration_minus_frame)
        position_with_anim ="{}={};{}={}".format(zero_time_string, current_position_string, last_duration_minus_frame_string, target_position_string)
        current_producer.set_position(position_with_anim)
        anim_in_node = get_property(current_producer.position_filter_node, "shotcut:animIn")
        anim_in_node.text = get_time_string(zero_time+last_duration)   
       

        
        
        producer_index +=1
        
        if len(producers)>producer_index:
            for prod in producers[producer_index:]:
                prod.set_position(target_position_string)
    
    def interpolate(self, start_position, end_position, start_time, duration, current_time):
        (start_x, start_y, start_size) = start_position
        (end_x, end_y, end_size)= end_position
        
        ratio = (current_time-start_time)/duration
        
        current_x = start_x + ratio*(end_x-start_x) 
        current_y = start_y + ratio*(end_y-start_y) 
        current_size = start_size + ratio * (end_size-start_size)
        
        return (current_x, current_y, current_size)
        
  
class LineOrColumn(Box):
    def __init__(self,children_names, size = None):
        if (size != None):
            self.size = size
        else :
            self.size = len(children_names)
        
        self.children = None
        super().__init__(children_names,self.get_num_of_lines(),self.get_num_of_columns())
        
        for index,child in enumerate(self.children) :
            self.move_child(child, index+1)
    
    
    def goto(self, line_num, col_num, duration=None):
        self.move(line_num, col_num,self.get_num_of_columns(), duration)
    
    def get_num_of_lines(self):
        raise NotImplementedError
    
    def get_num_of_columns(self):
        raise NotImplementedError
    
    def move_child(self, player, index, duration = None):
        raise NotImplementedError
        
#     def at(self, line_num, col_num, size=None):
#         if size is None :
#             size = self.get_num_of_columns()
#         self.update_relative_coordinates(line_num, col_num, size)
#         for index, child in enumerate(self.children):
#             self.move_child(child, index+1)
            
#     def move(self, line_num, col_num, size=None, duration=None):
#         if size is None :
#             size = self.get_num_of_columns()
#         self.update_relative_coordinates(line_num, col_num, size)
#         for index, child in enumerate(self.children):
#             self.move_child(child, index+1, duration)
#         
#     def prop_move(self, rel_y, rel_x, rel_size, duration=None):
#         DisplayedElement.prop_move(self,rel_y, rel_x, rel_size, duration)
#         
#         for index, child in enumerate(self.children):
#             self.move_child(child, index+1,duration)
    
    
    


class Column(LineOrColumn):
    def get_num_of_lines(self):
        return self.size
    
    def get_num_of_columns(self):
        return 1
    
    def move_child(self, child, index, duration = None):
        child.move(index, 1,1, duration)
    
    
    def shift(self, num_of_box, duration = None):
        self.v_shift(num_of_box, duration)
    
    def get_player(self, line):
        box = Box([], 1,1)
        box.inside(self).move(line, 1, 1)
        
        for player in self.player_registry.values():
            if (box.is_over(player)):
                return player
        return None
    
    def move(self, line_num, col_num, size= None, duration=None):
        if (size == None) :
            size = 1
        Box.move(self, line_num, col_num, size, duration=duration)
    
    def add_players(self, new_children,duration=None):
        start_pos = len(self.children)
        for index in range (len(new_children) ):
            position =start_pos +index +1 
            new_children[index].inside(self).move(position,1,1 ,duration)
    
class Line(LineOrColumn):
    def get_num_of_lines(self):
        return 1
    
    def get_num_of_columns(self):
        return self.size
        
    def move_child(self, child, index,duration=None):
        child.move(1,index,1,duration)
        
    def shift(self, num_of_box, duration = None):
        self.h_shift(num_of_box, duration)
    
    def add_players(self, new_children, duration=None):
        start_pos = len(self.children)
        for index in range (len(new_children) ):
            position =start_pos +index +1 
            new_children[index].inside(self).move(1,position,1,duration )
    
    def get_player(self, col):
        box = Box([], 1,1)
        box.inside(self).move(1, col, 1)
        
        for player in self.player_registry.values():
            if (box.is_over(player)):
                return player
        return None
    
    
    def move(self, line_num, col_num, size= None, duration=None):
        if (size == None) :
            size = 1
        Box.move(self, line_num, col_num, self.get_num_of_columns(), duration=duration)
    
    