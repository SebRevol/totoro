'''
Created on 6 avr. 2020

@author: SR246418
'''


from totoro.utils import    collect_video_files_names,Resource, get_num_box
import os

def get_space(name, max_len):
    current_len = len(name)
    result = ''
    for _ in range (max_len - current_len) :
        result += ' '
    return result

if __name__ == '__main__':
    resource= Resource('../001 - Montage orchestre dématérialisé/Orchestre dematerialisé - V1/Orchestre dematerialisé - V1_pupitres incomplets.mlt')
  
    
    video_file_names = collect_video_files_names("../006 - Videos format youtube")
    names_to_show = []
    for name in resource.players_registry :
        if name in video_file_names :
            names_to_show.append(name)
    num_box = get_num_box(names_to_show)

    file_content ='''


def locate(mus, grid) :
    
    grid.set_num_box({})
    grid.set_margin(10) 
    
    
'''.format(num_box)
    
    max_len =  len(max(names_to_show, key=len)) 

    for col in range(num_box) :
        for line in range(num_box):
            if (col*num_box+line < len(names_to_show) ):
                name = names_to_show[col*num_box+line ]
                file_content += '    mus["{}"{}].at({},{},1)\n'.format(name,get_space(name, max_len),line+1,col+1  )
    
    import codecs
    
    f = codecs.open("TotoroScripting/totoro/locate_generated.py", "w", "utf-8")
    f.write(file_content)
    f.close()
    
    path = os.path.join(os.getcwd(), "TotoroScripting/totoro/locate_generated.py")
    path_final = os.path.join(os.getcwd(), "TotoroScripting/totoro/locate.py")
    print("generation de "+path)
    print("copier et modifier son contenu dans  {} avant d'exécuter 'execute_grille_manuelle.bat'".format(path_final))