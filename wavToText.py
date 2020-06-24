import speech_recognition as sr

from graph import makeGraph


def wavToText(wavPath):
    resPath = './' + wavPath.split('/')[-1].split('.')[0] + '.txt'
    file = open(resPath, 'w')

    print('wav 파일의 음성을 text로 추출 중')
    print(wavPath + ' to ' + resPath)

    rec = sr.Recognizer()
    af = sr.AudioFile(wavPath)

    with af as source:
        audio = rec.record(source)

    file.write(rec.recognize_google(audio, language="en-US"))

    file.close()

    makeGraph(wavPath)

    return resPath