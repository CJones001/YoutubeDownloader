from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        # yt.streams accesses all available YouTube streams that match the url
        # progressive=True filters streams with both audio and video
        # file_extension="mp4" ensures the video format is MP4
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        # Retrieve the highest-quality resolution video
        highest_res_stream = streams.get_highest_resolution()
        # Download the selected video stream to the file save_path
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


if _name_ == "_main_":
    # Initialize the new application window using tkinter
    root = tk.Tk()
    # Keeps the application running in the background
    root.withdraw()

    video_url = input("Please enter a YouTube url:")