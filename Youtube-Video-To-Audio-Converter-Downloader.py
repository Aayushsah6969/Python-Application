import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import threading

class YouTubeConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Video to Audio Converter")
        master.geometry("500x300")

        self.label = tk.Label(master, text="Enter YouTube Video URL:")
        self.label.pack()

        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert_video)
        self.convert_button.pack()

        self.progress_label = tk.Label(master, text="")
        self.progress_label.pack()

    def download_progress(self, stream, chunk, remaining):
        progress = (1 - remaining / stream.filesize) * 100
        self.progress_label.config(text=f"Downloading... {progress:.2f}%")

    def convert_video(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube video URL.")
            return

        try:
            yt = YouTube(url, on_progress_callback=self.download_progress)
            audio_stream = yt.streams.filter(only_audio=True).first()
            filename = audio_stream.default_filename
            # Get the directory of the Python file
            directory = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(directory, filename)
            download_thread = threading.Thread(target=audio_stream.download, kwargs={'output_path': directory})
            download_thread.start()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return

        messagebox.showinfo("Success", "Download completed successfully!")

def main():
    root = tk.Tk()
    app = YouTubeConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
