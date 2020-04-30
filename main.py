import speech_recognition as sr
import mimetypes as mt

# 파일 입력받기
print(mt.guess_type('./sample/device_connected.wav'))
# 오디오 파일 : wav로 변환

# 비디오 파일 : 음성 추출해 wav로

# 음성 분리

# 음성 인식
rec = sr.Recognizer()
af = sr.AudioFile('./sample/device_connected.wav')
with af as source:
    audio = rec.record(source)


# 음성 텍스트화
print(rec.recognize_google(audio))