import sounddevice as sd
import wavio as wv
import numpy as np
freq = 44100
duration = 5

duration = 10.5  # seconds
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()
wv.write("recording.wav", recording, freq, sampwidth=2)