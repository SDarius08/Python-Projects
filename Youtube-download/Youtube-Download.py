from pytube import YouTube
from moviepy.editor import *
from time import sleep
from progressbar import progressbar
 
youtube_link = input("Introduceti video-ul: ")
yt = YouTube(youtube_link)

#Showing details
print("Title: "+ yt.title)

for i in progressbar(range(100)):
    sleep(0.02)
    t = yt.streams.filter(only_audio=True).all()
    t[0].download(output_path="E:\Music")  

print("Download completed!!")

input("Press Enter to exit")