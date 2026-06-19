import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path):

    # fp16=False: Whisper by default tries to use GPU float16 precision. On most Windows machines without a proper GPU setup this 
    # causes an error. Setting it to False forces CPU mode which works everywhere.
    result = model.transcribe(audio_path, fp16 = False)

    return result["text"]