import os
from src.speech_analyzer.reccord_audio import record_audio

def test_record_audio():

    # We use 5 seconds duration in test so you don't have to wait long
    filename = record_audio(filename="audio//test_answer.wav", duration=10)

    # os.path.exists() confirms the file was actually created on disk
    assert os.path.exists(filename)

    # os.path.getsize() confirms the file is not empty — greater than 0 bytes means real audio was captured
    assert os.path.getsize(filename) > 0

    print(f"Audio Saved: {filename}")
    print(f"File SIze: {os.path.getsize(filename)} bytes")


################################## Run Command ##################################
#-s flag: It shows your print() statements in the terminal so you can see the file size and confirm it worked.

# python -m pytest src/speech_analyzer/test_record_audio.py -v -s
