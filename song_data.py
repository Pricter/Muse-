from piano import *
import numpy as np
def get_song_data(music_notes):
    note_freqs=get_piano_notes()
    song=[get_wave(note_freqs[i]) for i in music_notes.split('-')]
    song=np.concatenate(song)

    return song

if __name__=='__main__':
    get_piano_notes('A-B-C')