import speech_recognition as sr


def wavToText(wavPath):
    rec = sr.Recognizer()
    af = sr.AudioFile(wavPath)

    with af as source:
        audio = rec.record(source)

    return rec.recognize_google(audio)
