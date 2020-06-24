import matplotlib.pyplot as plt
import numpy as np
import wave
from pydub import AudioSegment

def makeGraph(wavPath):
    sound = AudioSegment.from_file(wavPath)
    sound = sound.set_channels(1)
    sound.export("temp.wav", format="wav")

    spf = wave.open('temp.wav', 'r')

    signal = spf.readframes(-1)
    signal = np.fromstring(signal, dtype=np.int16)

    plt.title('signal')
    plt.plot(signal)
    plt.show()