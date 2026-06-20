import sounddevice as sd 
from scipy.io.wavfile import write


SAMPLE_RATE = 44100

def record_audio(filename="audio//answer.wav", duration=10):
    print(f"Recording for {duration} seconds... Speak now!")

    # sd.rec() starts recording. We multiply duration * SAMPLE_RATE to get the total number of samples needed
    # channels=1 means mono audio — one channel is enough for speech and keeps the file size small
    audio = sd.rec(int(duration * SAMPLE_RATE), samplerate = SAMPLE_RATE, channels=1)

    #  it makes Python pause and wait until the recording is completely finished before moving to the next line.
    sd.wait()

    # write() from scipy saves the recorded audio as a proper .wav file
    write(filename, SAMPLE_RATE, audio)

    print(f"Recording saved to {filename}")

    return filename