from pytube import YouTube
import subprocess
import os

def save_to_mp3():
    """Save a YouTube video URL to mp3.

    Args:
        url (str): A YouTube video URL.

    Returns:
        str: The filename of the mp3 file.
    """

    url = input("Enter the YouTube video URL: ")

    # create YouTube object
    video = YouTube(url)

    # get the best audio stream
    audio_stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()

    # download the audio stream as mp4
    audio_stream.download(filename=audio_stream.default_filename.replace('.webm', '.mp4'))

    # get the filename of the downloaded mp4
    mp4_filename = audio_stream.default_filename.replace('.webm', '.mp4')

    # convert the mp4 to mp3 using ffmpeg
    mp3_filename = mp4_filename.replace('.mp4', '.mp3')
    ffmpeg_cmd = f'ffmpeg -i "{mp4_filename}" "{mp3_filename}"'
    subprocess.call(ffmpeg_cmd, shell=True)

    # remove the intermediate mp4 file
    os.remove(mp4_filename)

    return mp3_filename

filename = save_to_mp3()
print(f"Saved MP3 file as {filename}")
