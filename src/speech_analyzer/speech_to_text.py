import speech_recognition as sr

def speech_to_text(audio_file):

    # sr.Recognizer() will Creates the speech recognition engine.
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        
        # Reads the entire audio.
        audio = recognizer.record(source)

    # .recognize_google will uses Google's free speech engine to convert speech into text.
    text = recognizer.recognize_google(audio)

    return text