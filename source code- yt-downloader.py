import re
import pytube
import urllib.request
from pytube import extract
from pytube import *

def down_as_vids():
    url = input("Enter a YouTube URL: ")
    dir = input("Enter download PATH: ")

    video_id = extract.video_id(url)
    if video_id:
        print("This is a YouTube video URL.")
        print('Downloading the video...')
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path= dir)
        input('The video has been downloaded !!!, Press enter to exit...')
    else:
        playlist_id = extract.playlist_id(url)
        if playlist_id:
            print("This is a YouTube playlist URL.")
            print("This is a YouTube playlist.")
            playlist = pytube.Playlist(url)
            video_urls = playlist.video_urls
            for i, url in enumerate(video_urls):
                downloaded1 = False
                for a in range(3):
                    try:
                        for i, url in enumerate(video_urls):
                            video = pytube.YouTube(url)
                            stream = video.streams.get_highest_resolution()
                            filename = re.sub('[^A-Za-z0-9]+', '_', video.title)
                            stream.download(output_path=dir, filename_prefix=f'{i+1}_')
                            print(f"Video {i+1}: {filename} downloaded successfully !!!")
                            input('press enter to exit...')
                            downloaded1 = True
                            break
                    except Exception as e :
                        print (e)            
        else:
            print("Unsupported URL.")

def down_as_audio():
    url = input("Enter a YouTube URL: ")
    dir = input("Enter download PATH: ")

    video_id = extract.video_id(url)
    if video_id:
        print("This is a YouTube video URL.")
        print('Downloading the video...')
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path= dir)
        input('The video has been downloaded !!!, Press enter to exit...')

    else:
        playlist_id = extract.playlist_id(url)
        if playlist_id:
            print("This is a YouTube playlist.")
            playlist = pytube.Playlist(url)
            video_urls = playlist.video_urls
            for i, url in enumerate(video_urls):
                downloaded1 = False
                for a in range(3):
                    try:
                        for i, url in enumerate(video_urls):
                            video = pytube.YouTube(url)
                            stream = video.streams.filter(only_audio=True).first()
                            filename = re.sub('[^A-Za-z0-9]+', '_', video.title)
                            stream.download(output_path=dir, filename_prefix=f'{i+1}_')
                            print(f"Video {i+1}: {filename} downloaded successfully as an audio file !!!")
                            input('press enter to exit...')
                            downloaded1 = True
                            break
                    except Exception as e :
                        print (e)
        else:
            print("Unsupported URL.")

def check_internet():
    try:
        urllib.request.urlopen('https://www.google.com')
        return True
    except:
        return False

if check_internet():
    print("PC is connected to the internet")
    answer_1 = input('''

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓─────────────────────────▄▀█▀█▀▄      ▓▓
▓▓────────────────────────▀▀▀▀▀▀▀▀▀     ▓▓
▓▓─────────█──────────────▄─░░░░░▄      ▓▓
▓▓─▄─█────▐▌▌───█──▄─▄───▐▌▌░░░░░▌▌     ▓▓
▓▓▐█▐▐▌█▌▌█▌█▌▄█▐▌▐█▐▐▌█▌█▌█░░░░░▌▌     ▓▓
▓▓█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█     ▓▓
▓▓█░█░░░█ █▀▀ █░░ █▀▀ █▀▀█ █▀▄▀█ █▀▀ ░█ ▓▓
▓▓█░█▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ ░█ ▓▓
▓▓█░░▀░▀░ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ ░█ ▓▓
▓▓▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀     ▓▓ 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
______▒_______________▒▒▒▒▒▒▒▒
____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
___▒
__▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
_▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒
▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒
▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒
▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒

do you want to continue (y/n) >>>''')
    if answer_1 == 'y':
        answer2 = input('''
what dow you want to download your youtube video/playlist file as
a) video file
b) audio file

for your answer enter the option (a/b) >>>''')
        if answer2 == 'a':
            down_as_vids()
        elif answer2 == 'b':
            down_as_audio()
        else:
            input('''please select a valid option (restart this program now) 
press enter to close this window.''')
    else:
        input('press enter to close this window')    
else:
    print("PC is not connected to the internet")

# from pytube import extract

# url = input("Enter a YouTube URL: ")

# video_id = extract.video_id(url)
# if video_id:
#     print("This is a YouTube video.")
#     # do something with the video ID
# else:
#     playlist_id = extract.playlist_id(url)
#     if playlist_id:
#         print("This is a YouTube playlist URL.")
#         # do something with the playlist ID
#     else:
#         print("Unsupported URL.")
#         # handle unsupported URL
# def playlist_as_vid():
#     playlist_link = input("Enter YouTube playlist link: ")
#     download_dir = input("Enter download directory: ")

#     video_id = extract.video_id(playlist_link)
#     if video_id:
#         print("This is a YouTube video URL.")y

#     else:
#         playlist_id = extract.playlist_id(playlist_link)
#         if playlist_id:

#             print("This is a YouTube playlist.")
#             playlist = pytube.Playlist(playlist_link)
#             video_urls = playlist.video_urls
#             for i, url in enumerate(video_urls):
#                 downloaded1 = False
#                 for a in range(3):
#                     try:
#                         for i, url in enumerate(video_urls):
#                             video = pytube.YouTube(url)
#                             stream = video.streams.get_highest_resolution()
#                             filename = re.sub('[^A-Za-z0-9]+', '_', video.title)
#                             stream.download(output_path=download_dir, filename_prefix=f'{i+1}_')
#                             print(f"Video {i+1}: {filename} downloaded successfully !!!")
#                             downloaded1 = True
#                             break
#                     except Exception as e :
#                         print (e)
#         else:
#             print("Unsupported URL.")
# def playlist_as_audio_file():
#     playlist_link = input("Enter YouTube playlist link: ")
#     download_dir = input("Enter download directory: ")
#     video_id = extract.video_id(playlist_link)
#     if video_id:
#         print("This is a YouTube video URL.")
#     else:
#         playlist_id = extract.playlist_id(playlist_link)
#         if playlist_id:

#             print("This is a YouTube playlist.")
#             playlist = pytube.Playlist(playlist_link)
#             video_urls = playlist.video_urls
#             for i, url in enumerate(video_urls):
#                 downloaded1 = False
#                 for a in range(3):
#                     try:
#                         for i, url in enumerate(video_urls):
#                             video = pytube.YouTube(url)
#                             stream = video.streams.filter(only_audio=True).first()
#                             filename = re.sub('[^A-Za-z0-9]+', '_', video.title)
#                             stream.download(output_path=download_dir, filename_prefix=f'{i+1}_')
#                             print(f"Video {i+1}: {filename} downloaded successfully as an audio file !!!")
#                             downloaded1 = True
#                             break
#                     except Exception as e :
#                         print (e)

#         else:
#             print("Unsupported URL.")
