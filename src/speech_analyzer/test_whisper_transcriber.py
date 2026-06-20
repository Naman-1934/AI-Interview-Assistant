from src.speech_analyzer.record_audio import record_audio
from src.speech_analyzer.whisper_transcriber import transcribe_audio

def test_transcriber_audio():
    print("Speak Something when recording starts...")

    audio_files = record_audio(filename="audio//test_whisper_audio.wav", duration=10)

    text = transcribe_audio(audio_files)

    assert isinstance(text, str)
    assert len(text) > 0

    print("Transcribed Text:", text)