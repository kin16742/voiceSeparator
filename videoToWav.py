import moviepy.editor as mp

def videoToWav(videoPath):
    resPath = "./sample/" + videoPath.split('/')[-1].split('.')[0] + ".wav"

    video = mp.VideoFileClip(videoPath)
    video.audio.write_audiofile(resPath)

    return resPath