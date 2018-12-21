##  Disassembles stereo wave file into its
##  left and right tracks and saves them




from scipy.io import wavfile ## for reading
import wave ## for writing
import struct ## for writing
import numpy as np ## useless as of now

## Load .wav file
FILENAME = 'crop2.wav'
fs, stereo = wavfile.read(FILENAME)

if not isinstance(stereo[0], np.ndarray):
    
    raise ValueError(FILENAME + ' is not a stereo wave file.')

#### Tried averaging the values of L and R, however when they are out of sync it gets quite messy
##mono = [i for i in range(len(stereo))]
##for i in mono:
##    mono[i] = (stereo[i][0] + stereo[i][1]) / 2.0
##
####Save to .wav file
##sampleRate = fs
##wavef = wave.open('crop_mono.wav', 'w')
##wavef.setnchannels(1)
##wavef.setsampwidth(2)
##wavef.setframerate(sampleRate)
##
##for i in range(len(mono)):
##    data = struct.pack('<h', mono[i])
##    wavef.writeframesraw(data)
##wavef.writeframes('')
##wavef.close()
##print 'Saved'



## Save as two separate tracks (left and right) and listen to them to hear the better one
sampleRate = fs
mono1 = [stereo[i][0] for i in range(len(stereo))]
mono2 = [stereo[i][1] for i in range(len(stereo))]
wavef1 = wave.open(FILENAME.split('.')[0]+'.left.wav', 'w')
wavef2 = wave.open(FILENAME.split('.')[0]+'.right.wav', 'w')
wavef1.setnchannels(1)
wavef1.setsampwidth(2)
wavef1.setframerate(sampleRate)
wavef2.setnchannels(1)
wavef2.setsampwidth(2)
wavef2.setframerate(sampleRate)

for i in range(len(mono1)):
    data = struct.pack('<h', mono1[i])
    wavef1.writeframesraw(data)
    data = struct.pack('<h', mono2[i])
    wavef2.writeframesraw(data)
wavef1.writeframes('')
wavef2.writeframes('')
wavef1.close()
wavef2.close()
print 'Saved'
    

#### Display the wave you actually have so you're not disappointed that much in yourself just from the fact that this does'nt work in the slightest
##import pygame
##import m
##
##size = WIDTH, HEIGHT = (800, 480)
##surf = m.pygame_init(size, 'Stereo to mono')
##mx = 32768.0
##for x in range(WIDTH-1):
##    pygame.draw.line(surf, (255, 255, 255), (x, HEIGHT//2-mono[x]/mx*HEIGHT), (x+1, HEIGHT//2-mono[x+1]/mx*HEIGHT))
##
##while True:
##    m.pygame_exit()
##    pygame.display.update()
