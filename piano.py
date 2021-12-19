import numpy as np
from numpy.random.mtrand import sample


samplerate=44100

def get_wave(freq,duration=1):
    amplitude=4096

    t=np.linspace(0,duration,int(samplerate*duration))
    
    wave=amplitude*np.sin(2*np.pi*freq*t)

    return wave



def get_piano_notes():
    #white keys are uppercase, black keys are lower case
    octave=['C','c','D','d','E','F','f','G','g','A','a','B']
    base_freq=261.63

    note_freqs={octave[i]:base_freq*2**(i/12) for i in range(len(octave))}

    note_freqs['']=0.0 #silent note

    return note_freqs
if __name__=='__main__':
    get_piano_notes()