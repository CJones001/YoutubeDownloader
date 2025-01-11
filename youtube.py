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


if __name__ == "__main__":
    # Initialize the new application window using tkinter
    root = tk.Tk()
    # Keeps the application running in the background
    root.withdraw()

    # Prompt user for youtube url
    video_url = input("Please enter a YouTube url:")
    # Open the file explorer so you can pick the save location
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location")