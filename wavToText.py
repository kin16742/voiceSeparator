import speech_recognition as sr


def wavToText(wavPath):
    resPath = './' + wavPath.split("/")[-1] + '.txt'
    file = open(resPath, 'w')

    rec = sr.Recognizer()
    af = sr.AudioFile(wavPath)

    with af as source:
        audio = rec.record(source)

    file.write(rec.recognize_google(audio))

    file.close()

    return resPath