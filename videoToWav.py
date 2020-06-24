import moviepy.editor as mp


def videoToWav(videoPath):
    resPath = "./sample/" + videoPath.split('/')[-1].split('.')[0] + ".wav"

    print('mp4 파일을 wav 파일로 변환합니다.')
    print(videoPath + ' to ' + resPath)

    video = mp.VideoFileClip(videoPath)
    video.audio.write_audiofile(resPath)

    return resPath
