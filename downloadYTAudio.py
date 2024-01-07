#import youtube library
from pytube import YouTube


#download audio function
def download_audio(video_url,output_path = 'audio.mp3'):
    try:
        yt = YouTube(video_url)
        #set filter to only download audio
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        print("Audio downloaded")
    except Exception as e:
        #ouput fail
        print(f"an error occured: {e}")
#download video function
def download_video(video_url,output_path = 'video.mp4'):
    try:
        yt = YouTube(video_url)
        #set filter to only download video
        audio_stream = yt.streams.filter(only_video=True).first()
        audio_stream.download(output_path)
        print("Video downloaded")
    except Exception as e:
        #output fail
        print(f"an error occured: {e}")
#get video link    
video_url = input("paste your youtube link: ")
download_audio(video_url)
download_video(video_url)
