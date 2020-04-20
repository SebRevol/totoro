'''
Created on 6 avr. 2020

@author: SR246418
'''

from os import listdir
from os.path import isfile
import datetime

TIME_FORMAT="%H:%M:%S.%f"
zero_time =  datetime.datetime.strptime("00:00:00.000", TIME_FORMAT)

frame_duration = None
current_resource = None


TIME_FORMAT_USER = "%H:%M:%S:%f"

def set_frame_duration(duration):
    global frame_duration
    frame_duration = duration

def get_frame_duration():
    global frame_duration
    return frame_duration

def get_current_resource():
    global current_resource
    return current_resource

def set_current_resource(resource):
    global current_resource
    current_resource = resource


def collect_video_files_names(youtube_path):
    instru_map= {}
    instru_dirs= [f for f in listdir(youtube_path) if not  isfile(youtube_path+'/'+ f)]
    video_file_names =[]
    for instru_dir in instru_dirs :
        if (not instru_dir.startswith("001")):
            player_names =[]
            path = youtube_path+'/'+ instru_dir
            for f in listdir(path) :
                full_path = path+'/'+ f
                
                if (isfile(full_path) ):
                    player_name = get_player_name(full_path)
                    video_file_names.append(player_name)
                    player_names.append(player_name)
            instru_map[instru_dir] = player_names
                    
    return video_file_names, instru_map

def fix_relpath(prexif, root):

    producers = root.findall("producer")

    for prod in producers :
        prop = get_property(prod, "resource")
        index = prop.text.find("006")
        if (index <= 0):
            index = prop.text.find("003")
        if (index >0) :
            prop.text =prexif+ prop.text[index:]
            

            
def get_child_with_attribute_value(node, child_name, attribute_name, value) :
    for child in node.findall(child_name):
            if child.get(attribute_name) == value :
                return child

def get_filter(producer_node, filter_name):
    filters = producer_node.findall("filter")
    for fil in filters :
        if (get_property(fil, "shotcut:filter") is not None and get_property(fil, "shotcut:filter").text == filter_name) :
            return fil

def get_property(node, property_name):
    return get_child_with_attribute_value(node, "property", "name", property_name)
            
def get_player_name(path):
    return path[path.rfind("/")+1: path.rfind(".")]
            

def get_time_from_user_string(time_string_without_milli):
    return datetime.datetime.strptime(time_string_without_milli, TIME_FORMAT_USER)

def get_user_string_from_time(time):
    return datetime.datetime.strftime(time, TIME_FORMAT_USER)

def get_time_string(time) : 
    return datetime.datetime.strftime(time, TIME_FORMAT)   

def get_duration(node_with_in_out):
        start_time =  datetime.datetime.strptime(node_with_in_out.get('in'), TIME_FORMAT)
        end_time =  datetime.datetime.strptime(node_with_in_out.get('out'), TIME_FORMAT)
        return end_time - start_time
    
def insert_before(next_node, node_to_insert, parent_map):
    parent_node = parent_map[next_node]
    index= list(parent_node).index(next_node)
    parent_node.insert(index, node_to_insert)
    parent_map[node_to_insert] = parent_node
    
def insert_after(previous_node, node_to_insert, parent_map):
    parent_node = parent_map[previous_node]
    index= list(parent_node).index(previous_node)
    parent_node.insert(index+1, node_to_insert)
    parent_map[node_to_insert] = parent_node
    
def get_num_box(names_num):
    
    num=0
   
    while (num*num < names_num) :
        num +=1
        
    return num

    
def get_position(producer):
    position_text = producer.position_node.text
    if (":" in position_text):
        last_equal_index = position_text.rfind("=")
        position_text =position_text[last_equal_index+1:]
    return position_text

    
    
        
    

    
    
    
        
        
    