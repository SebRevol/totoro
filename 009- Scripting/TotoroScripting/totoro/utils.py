'''
Created on 6 avr. 2020

@author: SR246418
'''

from os import listdir
from os.path import isfile
import xml.etree.ElementTree as ET



import datetime
from totoro import locate
import copy
import uuid
import math

TIME_FORMAT="%H:%M:%S.%f"
zero_time =  datetime.datetime.strptime("00:00:00.000", TIME_FORMAT)

frame_duration = None

TIME_FORMAT_USER = "%H:%M:%S:%f"

def collect_video_files_names(youtube_path):
    instru_dirs= [f for f in listdir(youtube_path) if not  isfile(youtube_path+'/'+ f)]
    video_file_names =[]
    for instru_dir in instru_dirs :
        if (not instru_dir.startswith("001")):
            path = youtube_path+'/'+ instru_dir
            for f in listdir(path) :
                full_path = path+'/'+ f
                
                if (isfile(full_path)):
                    video_file_names.append(get_player_name(full_path))
                    
    return video_file_names

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
    
def get_num_box(names):
    
    num=0
    names_num = len(names)
    while (num*num < names_num) :
        num +=1
        
    return num


def merge_files(resources_to_merge, output_path, MARGIN=0):
    receiving_resource= Resource(resources_to_merge[0], "receiving")
    
    for  index, res in enumerate(resources_to_merge[1:]):
        imported_resource = Resource(res, "imported_{}".format(index))

        for player in imported_resource.players_registry.values() :
            if (player.name not in receiving_resource.players_registry):
                receiving_resource.add_player(player)
            
    receiving_resource.auto_locate(MARGIN)
    receiving_resource.enable_tracks()
    receiving_resource.save(output_path)
    
    
def get_position(producer):
    position_text = producer.position_node.text
    if (":" in position_text):
        last_equal_index = position_text.rfind("=")
        position_text =position_text[last_equal_index+1:]
    return position_text

class Resource(object):
    def __init__(self, resource_path, name= ""):
        
        self.path = resource_path
        self.name = name
        self.element_tree = ET.parse(resource_path)
        self.root = self.element_tree.getroot()
        
        profile = list(self.root)[0]
        self.x_res = int(profile.get("width"))
        self.y_res = int(profile.get("height"))
        self.frame_rate = int(profile.get("frame_rate_num"))
        
        global frame_duration
        frame_duration =datetime.timedelta(milliseconds = math.ceil(1000/self.frame_rate))
        self.grid = Grid(self.x_res,#resolution X 
                   self.y_res) #resolution Y
                
        
        self.parent_map = {c:p for p in self.root.iter( ) for c in p}
        fix_relpath('../../', self.root)
        
        self.producer_registry ={}
        self.playsist_registry={}
        self.players_registry = {}
        
        self.node_to_object ={}
        
        self.tractor = None
        
        self.init_producers()
        self.init_playlists()
        self.init_tractor()
        self.init_players()
    
        
        
    
    def locate(self):
        locate.locate(self.players_registry, self.grid)
    
    def auto_locate(self, margin):
           
        video_file_names = collect_video_files_names("../006 - Videos format youtube")
     
        #video_file_names.remove('Jean-Jacques_chef_totoro')
        names_to_show = []
        for name in self.players_registry :
            if name in video_file_names :
                names_to_show.append(name)
        
        
        #names_to_show.remove("Serge_baryton_audio")      
        num_box = get_num_box(names_to_show)
        
        
        self.grid.set_num_box(num_box)  
        self.grid.set_margin(margin)
        
        for col in range(num_box) :
            for line in range(num_box):
                if (col*num_box+line < len(names_to_show) ):
                    self.players_registry[names_to_show[col*num_box+line ]].at(line+1,col+1,1)  
        
    
    def save(self, path=None):
        if (path == None) :
            path =self.path
        self.fix_ids()
        print("Sauvegarde du fichier "+ self.name +" in " + path)
        self.element_tree.write(path, xml_declaration=True)
        
        
    
    def init_producers(self):
        for prod in self.root.findall("producer") :
            producer =Producer(prod, self)
            self.producer_registry[producer.get_id()]= producer
            
        
    def init_playlists(self):
        for play in self.root.findall("playlist"):
            playlist = Playlist(play, self)
            self.playsist_registry[playlist.get_id()]=playlist
            
            
    def init_tractor(self):
        tractor_node = self.root.findall("tractor")[0]
        self.tractor= Tractor(tractor_node,  self.playsist_registry, self.parent_map)
        
    
    def init_players(self):
        player_names = collect_video_files_names("../006 - Videos format youtube")
        
        for track in self.tractor.tracks :
            if (track.get_name() in player_names) :
                player = Player(track.get_name(),track, self.grid)
                self.players_registry[track.get_name()]= player
                player.transitions = self.get_transitions(player)
        
    def enable_tracks(self):
        for player in self.players_registry.values():
            player.enable_track()    
                 
    def fix_ids(self):
        
        index =0
        for transition in self.tractor.transitions :
            node = transition.node
            node.set('id', 'transition{}'.format(index))
            index+=1
            
        index =0
        for node in self.root.iter("filter") :
            node.set("id", 'filter{}'.format(index))
            index+=1
        
        index =0
        for node in self.root.iter("producer") :
            if( node.get("id") != "black"):
                prod = self.node_to_object[node]
                prod.set_id('producer{}'.format(index))
                index+=1
        
        index =0
        for node in self.root.iter("playlist") :
            if (node.get("id")!= "background" and node.get("id")!= "main_bin"):
                playlist = self.node_to_object[node]
                playlist.set_id('playlist{}'.format(index))
                index+=1
        
    def __str__(self, *args, **kwargs):
        result = 'Resource :' + self.path + '\n'
        
        for player in self.players_registry :
            result += self.players_registry[player].__str__()+'\n'
        
        return result
            
    
    def get_transitions(self, player): 
        result = []
        for transition in self.tractor.transitions :
            if (transition.get_b_track() == player.track):
                result.append(transition)
        return result
    
    
    def add_player(self, player):
        self.players_registry[player.name] = player
        self.tractor.add_track(player.track)
        self.tractor.add_transitions(player)
        
        for producer in player.producers :
            self.add_producer_node(producer.node)
            self.node_to_object[producer.node]=producer
            producer.set_resource(self)
        
        self.add_playlist_node(player.playlist.node)
        self.node_to_object[player.playlist.node] = player.playlist
        player.playlist.set_resource(self)
        
        player.grid = self.grid
        
    
    def add_producer_node(self, producer_node):
        insert_before(self.tractor.node, producer_node, self.parent_map)
        
        
    def add_playlist_node(self, playlist_node):
        insert_before(self.tractor.node, playlist_node, self.parent_map)
        
        
        
        
        
    
   
    



class Player(object) :
    def __init__(self, name, track, grid):
        self.track = track
        self.playlist = track.playlist
        self.producers = self.playlist.producers
        self.transitions = []
        self.name = name
        self.grid = grid
        self.pos_init = None
        self.current_time = zero_time
        self.current_position ={"line_num" :-1, "col_num":-1, "size" :-1}
        
    def at(self, line_num, col_num,size):
        self.grid.locate( self.producers, line_num, col_num,size)
        
    def prop_move(self,vert_ratio, horiz_ratio,size_ratio, duration =None):
        num_box = self.grid.num_box
        self.move(vert_ratio* num_box, horiz_ratio*num_box, size_ratio * num_box, duration)        

    def move(self,  line_num, col_num,size, duration =None):
        if (type(line_num)== float):
            line_num +=1
        
        if (type(col_num)== float):
            col_num +=1
        
        self.current_position["line_num"] = line_num
        self.current_position["col_num"] = col_num
        self.current_position["size"] = size
        
        current_producer = self.current_entry.producer
        current_prod_index= self.producers.index(current_producer)
        if (duration == None):
            self.grid.locate(self.producers[current_prod_index:], line_num, col_num, size)
        else :
            current_position = get_position(current_producer)
            self.grid.animate(self.producers[current_prod_index:], current_position, line_num, col_num, size, duration)
    
    def on(self, time_string):
        self.current_time = get_time_from_user_string(time_string)
        print(self.name)
        self.current_entry = self.playlist.get_current_entry(self.current_time)
        
        return self
        
    def show(self):
        current_producer = self.current_entry.producer
        current_prod_index= self.producers.index(current_producer)
        self.grid.locate(self.producers[current_prod_index:],self.current_position["line_num"],self.current_position["col_num"],self.current_position["size"])
    
    def hide(self):
        current_producer = self.current_entry.producer
        current_prod_index= self.producers.index(current_producer)
        self.grid.locate(self.producers[current_prod_index:],-1,-1,1)
    
                
    def __str__(self, *args, **kwargs):
           
        result = 'Player : '+ self.name +'\n'
        result+= '     Track:'
        result += str(self.track.node)
        
        result += '\n    Playslist:\n'
        result += str(self.playlist.node)
        
        result += '\n   Producers:\n'
        for prod in self.producers :
            result +=str(prod.node)
        
        return result
        
    def enable_track(self):
        self.track.set_enable(True)
    
    
class Producer(object) :
    def __init__(self,producer_node, resource): 
        self.node = producer_node
        self.name = get_player_name(get_property(self.node,  "resource").text)
        self.position_filter_node = get_filter(self.node,"affineSizePosition")
        if (self.position_filter_node is not None):
            self.position_node = get_property(self.position_filter_node, "transition.rect")
        
        self.set_resource(resource)
        self.node_to_object[self.node] = self
        self.entry = None

    def set_resource(self, resource):
        self.resource =resource
        self.node_to_object = resource.node_to_object
        
    def get_id(self):
        return self.node.get("id")
    
    def set_id(self, id_val) :
        self.node.set("id", id_val)
        if(self.entry is not None):
            self.entry.set_producer_id_ref(id_val)
        
    
    def get_position_filter_id(self):
        return self.position_node.get("id")
    
    def set_position_filter_id(self, id_val):
        self.position_filter_node.set("id", id_val)
    
        
    def set_position(self, position_string):
        self.position_node.text = position_string
      
    def set_out_time(self, time):
        time_string = get_time_string(time)
        for filter_node in self.node.findall("filter") :
            filter_node.set("out", time_string)
        
    def set_in_time(self, time):
        time_string = get_time_string(time)
        for filter_node in self.node.findall("filter") :
            filter_node.set("in", time_string)
            
                
class Playlist(object):
    def __init__(self, playlist_node, resource): 
        self.node = playlist_node
        self.track = None
        self.entries =[]
        self.producers = []
        
        self.set_resource(resource)
        
        self.node_to_object[self.node] = self
        
        current_time = datetime.datetime.strptime("00:00:00.000", TIME_FORMAT)
        for child in self.node :
            if (child.tag == "blank"):
                blank = Blank(child, current_time)
                self.entries.append(blank)
                current_time += blank.get_duration()
            elif (child.tag == "entry"):
                entry = Entry(child, current_time, self.resource)
                self.entries.append(entry)
                self.producers.append(entry.producer)
                current_time += entry.get_duration() + frame_duration
    
        if (len(self.producers)>0) :       
            self.producer_name = self.producers[0].name
        else:
            self.producer_name = "NONE"        
    
    def set_resource(self, resource):
        self.resource= resource
        self.node_to_object = resource.node_to_object
        self.producer_registry = resource.producer_registry
        
        for entry in self.entries :
            if type(entry) == Entry:
                entry.set_resource(resource)
    
    def get_current_entry(self, time):
#         
        for entry in self.entries :
            if entry.start_time == time : 
                return entry
            elif entry.start_time < time and entry.get_end_time() > time :
                print(entry.start_time)
                print(entry.get_end_time())
               
                new_entry = entry.split(time)
                self.insert_entry(entry, new_entry)
                return new_entry
        return None
    
    def insert_entry(self, current_entry, new_entry):
        current_producer = current_entry.producer
        new_producer = new_entry.producer
        
        self.producers.insert(self.producers.index(current_producer)+1, new_producer)
        self.entries.insert(self.entries.index(current_entry), new_entry)
    
    def get_id(self):
        return self.node.get("id")
    
    def set_id(self, id_val):
        if(self.track is not None) :
            self.track.set_playlist_idref(id_val)
        self.node.set("id", id_val)
    
class Blank(object):
    def __init__(self, blank_node,start_time):
        self.node = blank_node
        self.start_time = start_time
        
    def get_duration(self):
        duration = datetime.datetime.strptime(self.node.get('length'), TIME_FORMAT) 
        return duration - zero_time
    
    def set_duration(self, duration):
        end_date = zero_time + duration
        self.node.set('length', end_date.strftime(TIME_FORMAT))
        
    def get_end_time(self):
        return self.start_time + self.get_duration()-frame_duration 
        
    
class Entry(object):
    def __init__(self, entry_node,  start_time, resource ):
        self.node = entry_node
        self.set_resource(resource)
        
        self.producer = self.producer_registry.get(self.node.get('producer'))
        self.producer.entry = self
        self.start_time = start_time
        
    def set_resource(self, resource):
        self.resource= resource
        self.producer_registry = resource.producer_registry
            
    
    def get_duration(self):
        return get_duration(self.node)
        
    def get_end_time(self):
        return self.start_time + self.get_duration()
    
    def set_producer_id_ref(self, producer_id):
        self.node.set('producer', producer_id)
    
    def split(self, time):
        entry_local_time = time -self.start_time
        producer_local_time = self.get_in_time()+entry_local_time
        previous_producer_out_time = producer_local_time - frame_duration
        
        new_producer_node = copy.deepcopy(self.producer.node)
        insert_after(self.producer.node, new_producer_node, self.resource.parent_map)
        new_producer = Producer(new_producer_node, self.resource)
        tmp_id = uuid.uuid1()
        new_producer.set_id(tmp_id)
        self.producer_registry[tmp_id] = new_producer
        
        #on utilise le registre pour recréer le lien entre le producer et l'entry via le constructeur
        new_entry_node = copy.deepcopy(self.node)
        insert_after(self.node, new_entry_node, self.resource.parent_map)
        new_entry_node.set('producer', tmp_id)
        new_entry = Entry(new_entry_node,time , self.resource)
        
        self.set_out_time(previous_producer_out_time)
        new_entry.set_in_time(producer_local_time)
        
        return new_entry
        
    def set_out_time(self, time):
        time_string = get_time_string(time)
        self.node.set("out", time_string)    
        self.producer.set_out_time(time)
        
        
    def set_in_time(self, time):
        time_string = get_time_string(time)
        self.node.set("in", time_string)    
        self.producer.set_in_time(time)
        
    def get_in_time(self):
        return  datetime.datetime.strptime(self.node.get('in'), TIME_FORMAT)
    
        

class Tractor(object):
    def __init__(self, tractor_node, playlist_registry, parent_map):
        self.node = tractor_node
        self.parent_map = parent_map
        
        self.tracks = []
        self.transitions = []
        for track_node in self.node.findall("track"):
            self.tracks.append(Track(track_node, playlist_registry))
        
        for transition_node in self.node.findall("transition"):
            self.transitions.append(Transition(transition_node, self.tracks, self))
            
        
   
        
    def add_track(self, track):
        last_track = self.tracks[-1]
        insert_after(last_track.node, track.node, self.parent_map)
        self.tracks.append(track)
        
        
        
    def add_transitions(self, player): 
        
        for transition in player.transitions :
            self.node.append(transition.node)
            self.transitions.append(transition)
            transition.parent_tractor=self
            transition.update_b_track(player.track)
        
class Track(object):
    def __init__(self, track_node, playlist_registry): 
        self.node =   track_node
        self.playlist = playlist_registry[self.node.get('producer')]
        self.playlist.track = self
    
    def get_name(self):
        return self.playlist.producer_name
    
    def set_playlist_idref(self, idref):
        self.node.set("producer", idref) 
        
    def get_playlist_idref(self):
        return self.node.get('producer')
    
    def set_enable(self,enable ):
        if (enable):
            if( "hide" in  self.node.attrib):
                self.node.attrib.pop("hide")
        else :
            self.node.set('hide', "both")
        
        
class Transition(object):
    def __init__(self,  transition_node, tracks, parent_tractor):
        self.node = transition_node
        self.tracks = tracks
        self.b_track_node = get_property(self.node, "b_track")
        self.parent_tractor = parent_tractor
        
    def get_b_track(self):
        track_nodes = self.parent_tractor.node.findall("track")
        node_index =  int(self.b_track_node.text)
        track_node = track_nodes[node_index]
        
        for track in self.parent_tractor.tracks :
            if track.node == track_node :
                return track
            
        return None
        
    def update_b_track(self, track):
        track_nodes = self.parent_tractor.node.findall("track")
        node_index= track_nodes.index(track.node)
        self.b_track_node.text = str(node_index) 
    
    
        
    
class Grid(object):
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
        
        