from src.speech_analyzer.whisper_transcriber import transcribe_audio

text = transcribe_audio("answer.wav")

print(text)