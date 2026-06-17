from record_audio import record_audio
from speech_to_text import speech_to_text

record_audio("answer.wav", duration=10)

text = speech_to_text("answer.wav")

print(text)