'''
Created on 6 avr. 2020

@author: SR246418
'''


import os

from totoro.model import Resource
from totoro.utils import collect_video_files_names, get_num_box
from totoro.display import get_short_name
import unicodedata
import re


def get_normalized_name(name):
    short_name = get_short_name(name)
    norm = unicodedata.normalize("NFD", short_name)
    norm = re.sub('[^0-9a-zA-Z_]', '', norm)
    norm = re.sub('^[^a-zA-Z_]+', '',  norm)
    return norm
    

def get_space(name, max_len):
    current_len = len(name)
    result = ''
    for _ in range (max_len - current_len) :
        result += ' '
    return result

resource= Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Test-API-merge2.mlt')


resource.clean_instru_map()

video_file_names, instru_map = collect_video_files_names("../006 - Videos format youtube")
names_to_show = []
for name in resource.players_registry :
    if name in video_file_names :
        names_to_show.append(name)
num_box = get_num_box(len(names_to_show))

file_content ='''

from totoro.utils import get_current_resource
resource = get_current_resource()
instru_map = resource.instru_map
mus = resource.players_registry

'''
instru_name_map ={"Saxophone":"sax", "Clarinettes":"clar", "Cor": "cor",
                  "Euphonium":"eph", "Flutes": "fl", "Hautbois":"hb",
                  "Percussions": "perc", "Trombone":"trb", "Trompettes et cornets": "trp",
                  "Tuba": "tb"
                  }

print(instru_map)
for name in names_to_show :
    file_content += '{}=mus["{}"]\n'.format(get_normalized_name(name), name)

for instru in instru_name_map :
    instru_name = instru_name_map[instru]
    normalized_name = get_normalized_name(instru)
    players = list( (play for play in instru_map[instru] if play in names_to_show))
    file_content +='''

class {}(object) :
    def __init__(self):
'''.format(normalized_name)
    players
    for player in players :
        file_content +="        self.{}={}\n".format(get_normalized_name(player),get_normalized_name(player))
    file_content +="        self.all=[{}]\n".format(",".join([get_normalized_name(player) for player in players]))
    file_content +="        return\n"
    
    file_content +="{}={}()".format(instru_name, normalized_name)
        
    
    
    
    
    


# 
# '''def locate(mus, grid, instru_map) :
#     
#     grid.set_num_box({})
#     grid.set_margin(10) 
#     
#     
# '''.format(num_box)
#     
#     max_len =  len(max(names_to_show, key=len)) 
# 
#     for col in range(num_box) :
#         for line in range(num_box):
#             if (col*num_box+line < len(names_to_show) ):
#                 name = names_to_show[col*num_box+line ]
#                 file_content += '    mus["{}"{}].at({},{},1)\n'.format(name,get_space(name, max_len),line+1,col+1  )
    
import codecs

f = codecs.open("TotoroScripting/totoro/players.py", "w", "utf-8")
f.write(file_content)
f.close()

path = os.path.join(os.getcwd(), "TotoroScripting/totoro/locate_generated.py")
path_final = os.path.join(os.getcwd(), "TotoroScripting/totoro/locate.py")
print("generation de "+path)
print("copier et modifier son contenu dans  {} avant d'exécuter 'execute_grille_manuelle.bat'".format(path_final))