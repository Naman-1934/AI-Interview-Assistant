import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(AI, duration=10):
    fs = 44100

    print("Recording...")

    audio = sd.record(int(duration * fs),samplerate = fs,channels=1)
    
    sd.wait()

    write(AI, fs, audio)

    print("Saved")