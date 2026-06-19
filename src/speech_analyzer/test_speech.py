from src.speech_analyzer.reccord_audio import record_audio
from src.speech_analyzer.speech_to_text import speech_to_text

record_audio("answer.wav", duration=10)

text = speech_to_text("answer.wav")

print(text)