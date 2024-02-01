import sounddevice as sd
from scipy.io.wavfile import write

freq = 44100
duration = 10

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

sd.wait()

write("recording.wav", freq, recording)
