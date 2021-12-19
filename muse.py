import sys
import song_data 
with open(sys.argv[1]) as f:

    r=f.read().split('\n')
r=list(filter(lambda x: x!='',[i for i in r]))

for idx,i in enumerate(r):
    r[idx]=i.split()

filename=''
for i in r:
    if i[0]=='start':
        filename=i[1]
    elif i[0]=='song':
        data=song_data.get_song_data(i[1])
        from scipy.io.wavfile import write
        import numpy as np
        write(f'{filename}.wav',44100,data.astype(np.int16))
    elif i[0]=='end':
        break

