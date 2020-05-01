'''
Created on 1 mai 2020

@author: SR246418
'''



from scipy.fftpack import fft

import numpy as np

from scipy.io import wavfile # scipy library to read wav files
from totoro.display import Column, get_duration_clock, incr_clock
from totoro.utils import get_current_resource



def spectrum(columns, lines, rate, duration):
    cols=[]
    mus = get_current_resource().players_registry
    grid = get_current_resource().grid
    remaining_players=list(mus.values())
    
    for col_num in range(columns) :
        col = SepctrumCol([], lines)
        remaining_players = col.fill(remaining_players)
        col.inside(grid).goto(2,col_num+0.5)
        cols.append(col)
       
    
    audio_data = get_audio_data(columns,rate,duration)
    #print(audio_data.shape)
    #print(grid)
    
    for  index  in range(audio_data.shape[0]):
        print(audio_data[index,:])
        for col_index in range(columns):
            cols[col_index].set_level(audio_data[index,col_index])
        
        incr_clock(rate) 



def average(arr, n):
    end =  n * int(len(arr)/n)
    
    return np.mean(arr[:end].reshape(-1, n), 1)


def get_audio_data(line_number, rate, duration, file='./totoro.wav'):
    
    fs, audiodata = wavfile.read(file)
    
    CHUNK= int(rate*fs)
    n_col =line_number+4
    n= int(CHUNK/(2*n_col))
    

    
    
    values =[]
    
    index = 0
    
    while index < len(audiodata)-CHUNK:
        
        # binary data
        data_np = audiodata[index:index+CHUNK]  
        index+=int(CHUNK)
        
        # compute FFT and update line
        yf = fft(data_np)
        yf_line=10*np.log10(np.abs(yf[0:int(CHUNK/2)])+1)
        yf_mean = average(yf_line, n)
        values.append(list(yf_mean))
    
        
    array = np.array(values)
    
    start_index= int(get_duration_clock().total_seconds()/rate)
    end_index=  start_index + int(duration/rate)
    array= array[start_index:end_index,2:2+line_number]
    return normalize(array)
   
   
    
   
def normalize(array):
    min_val= np.min(array, axis=0)
    max_val = np.max(array, axis=0)
    array_norm = (array-min_val)/(max_val-min_val)    
    print(array_norm)
    return array_norm

class SepctrumCol(Column):
    
    
    def set_level(self, level):
        num_to_show = int(level*self.num_box_line)+1
        #print("level :{}-num_to_show:{}".format(level,num_to_show))
        self.show()
        for i in range (self.num_box_line):
            player = self.get_player(i+1)
            if (player is not None):
                if i<self.num_box_line-num_to_show :
                    if (not player.hidden):
                        player.hide()
                else :
                    if (player.hidden):
                        player.show()
            
        
        
        