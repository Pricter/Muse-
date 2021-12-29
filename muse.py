import sys
import numpy as np
from scipy.io.wavfile import write

class Musepp:
    def __init__(self, filename: str, sampleRate: int):
        self.filename: str = filename
        self.sampleRate: int = sampleRate
        # List of notes
        self.freqs: dict = {
                           "CCCC": 8.176,
                           "CCC": 16.352, 
                           "CC": 32.703, 
                           "C": 65.406,
                           "c": 130.81,
                           "c'": 261.63,
                           "c''": 523.25,
                           "c'''": 1046.50,
                           "c''''": 2093.00,
                           "c'''''": 4186.01,
                           "c''''''": 8372.02,
                            "c'''''''": 16744.04,
                            "DDDD": 9.1777,
                            "DDD": 18.352,
                            "DD": 36.708,
                            "D": 73.416,
                            "d": 146.83,
                            "d'": 293.66,
                            "d''": 587.33,
                            "d'''": 1174.66,
                            "d''''": 2349.32,
                            "d'''''": 4698.64,
                            "d''''''": 9397.27,
                            "d'''''''": 18899.05,
                            "EEEE": 10.814,
                            "EEE": 20.61,
                            "EE": 41.203,
                            "E": 82.407,
                            "e": 164.81,
                            "e'": 329.63,
                            "e''": 659.25,
                            "e'''": 1318.51,
                            "e''''": 2637.02,
                            "e'''''": 5274.04,
                            "e''''''": 10548.08,
                            "e'''''''": 21096.16,
                            "FFFF": 10.913,
                            "FFF": 21.827,
                            "FF": 43.654,
                            "F": 87.307,
                            "f": 174.61,
                            "f'": 349.23,
                            "f''": 698.46,
                            "f'''": 1396.91,
                            "f''''": 2793.83,
                            "f'''''": 5587.66,
                            "f''''''": 11175.31,
                            "f'''''''": 22351.63,
                            "GGGG": 11.735,
                            "GGG": 23.145,
                            "GG": 46.875,
                            "G": 92.5,
                            "g": 185.0,
                            "g'": 371.0,
                            "g''": 741.0,
                            "g'''": 1482.0,
                            "g''''": 2965.0,
                            "g'''''": 5930.0,
                            "g''''''": 11860.0,
                            "g'''''''": 23720.0,
                            "HHHH": 12.0,
                            "HHH": 24.0,
                            "HH": 49.0,
                            "H": 98.0,
                            "h": 196.0,
                            "h'": 392.0,
                            "h''": 784.0,
                            "h'''": 1568.0,
                            "h''''": 3136.0,
                            "h'''''": 6272.0,
                            "h''''''": 12544.0,
                            "h'''''''": 25088.0,
                            "AAAA": 13.75,
                            "AAA": 27.5,
                            "AA": 55.0,
                            "A": 110.0,
                            "a": 220.0,
                            "a'": 440.0,
                            "a''": 880.0,
                            "a'''": 1760.0,
                            "a''''": 3520.0,
                            "a'''''": 7040.0,
                            "a''''''": 14080.0,
                            "a'''''''": 28160.0,
                            "BBBB": 15.435,
                            "BBB": 30.868,
                            "BB": 61.735,
                            "B": 123.47,
                            "b": 246.94,
                            "b'": 493.88,
                            "b''": 987.77,
                            "b'''": 1975.53,
                            "b''''": 3951.07,
                            "b'''''": 7902.13,
                            "b''''''": 15804.26,
                            "b'''''''": 31608.5,
                           }
        self.keys: str = self.freqs.keys()
        self.amplitude: int = 4096
        self.song: list = []
        self.duration: float = 1

    def get_wave(self, freq: float, duration: float = 1) :
        amplitude=4096
        t=np.linspace(0,duration,int(self.sampleRate*duration))
        wave=amplitude*np.sin(2*np.pi*freq*t)
        return wave

    def parse(self, ops: list) -> None:
        if(len(ops) < 2):
            print("Error: EOF Reached, Program must be of atleast one operation.")
            sys.exit()
        sampleRateSpecification: int = 0
        song_iter = iter(range(len(ops)))
        for i in song_iter:
            if ops[i] == ":play":
                if i == len(ops)-1:
                    print("Error: EOF Reached, :play must be followed by a note.")
                    sys.exit()
                if ops[i+1] not in self.keys:
                    print("Error: Invalid input, :play must be followed by a valid note.")
                    sys.exit()
                freq: float = self.freqs[ops[i+1]]
                duration: float = self.duration
                self.song.append(self.get_wave(freq, duration))
            elif ops[i] in self.keys:
                if i == 0:
                    print("Error: Invalid input, :play must be preceeded by a note.")
                    sys.exit()
                elif ops[i-1] != ":play":
                    print("Error: Invalid input, :play must be preceeded by a note.")
                    sys.exit()
                pass
            elif ops[i] == ":duration":
                if i == len(ops)-1:
                    print("Error: EOF Reached, :duration must be followed by a number.")
                    sys.exit()
                try:
                    self.duration: float = float(ops[i+1])
                    if self.duration <= 0:
                        print("Error: Invalid input, :duration must be followed by a positive number.")
                        sys.exit()
                except:
                    print("Error: Invalid input, :duration must be followed by a positive number.")
                    sys.exit()
                next(song_iter)
            elif ops[i] == ":sample_rate":
                if len(sys.argv) == 3:
                    print(f"Error: sample rate already specified in command line, `{ops[i]} {ops[i+1]}`.")
                    sys.exit()
                if i == len(ops)-1:
                    print("Error: EOF Reached, :sample_rate must be followed by a number.")
                    sys.exit()
                if not ops[i+1].isdigit():
                    print("Error: Invalid input, :sample_rate must be followed by a number.")
                    sys.exit()
                sampleRateSpecification += 1
                if(sampleRateSpecification > 1):
                    print("Error: `:sample_rate` can only be specified once.")
                    sys.exit()
                self.sampleRate = int(ops[i+1])
                next(song_iter)
            elif ops[i] == ":amplitude":
                if i == len(ops)-1:
                    print("Error: EOF Reached, :amplitude must be followed by a number.")
                    sys.exit()
                if not ops[i+1].isdigit():
                    print("Error: Invalid input, :amplitude must be followed by a number.")
                    sys.exit()
                self.amplitude = int(ops[i+1])
                next(song_iter)
            else:
                print(f"Error: Invalid op `{ops[i]}`.")

    def run(self) -> None:
        try:
            f = open(self.filename)
        except FileNotFoundError:
            print("Error: File not found.")
            return
        ops = f.read().split()
        self.parse(ops)
        self.song = np.concatenate(self.song)
        self.song = self.song.astype(np.int16)
        try:
            write(f'{sys.argv[1]}.wav', self.sampleRate, self.song.astype(np.int16))
        except:
            print("Error: Could not write file.")
            sys.exit()

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Usage: muse.py <filename> <sampleRate (optional)>")
        exit(1)
    elif(len(sys.argv) == 2):
        muse = Musepp(sys.argv[1], 44100)
    elif(len(sys.argv) == 3):
        try:
            muse = Musepp(sys.argv[1], int(sys.argv[2]))
        except:
            print("Error: Sample rate must be an integer.")
            exit(1)
    else:
        print("Usage: muse.py <filename> <sampleRate (optional)>")
        exit(1)
    muse.run()