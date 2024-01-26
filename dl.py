from tkinter import *
from tkinter import messagebox as mb
from pytube import YouTube
from pytube import Stream

def downloader(link, directory, filename):
    yt_link = link.get()
    save_path = directory.get()
    aftersave_filename = filename.get()

    try:
        yt = YouTube(yt_link)
        video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        video.download(save_path, aftersave_filename)
    except Exception as e:
        mb.showerror("Error", f"Something went wrong, please try again. Error: {str(e)}")

def merge_audio_video(video_file, audio_file, output_file):
    import os
    os.system(f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac "{output_file}"')
    os.remove(video_file)
    os.remove(audio_file)

def reset(l_strvar, d_strvar, fn_strvar):
    l_strvar.set("")
    d_strvar.set("")
    fn_strvar.set("")

root = Tk()
root.title("YouTube Downloader")
root.geometry("700x300")
root.resizable(False, False)
root.config(bg = "Coral")

Label(root, text="YouTube Downloader", bg="Coral", font=("Times New Roman", 24)).pack()

Label(root, text = "YouTube Link", font = ("Times New Roman", 13), bg = "Coral").place(relx = 0.3, rely = 0.2)

link_strvar = StringVar(root)
link_entry = Entry(root, width = 50, textvariable = link_strvar)
link_entry.place(relx = 0.5, rely = 0.2)

Label(root, text = "Save Path", font = ("Times New Roman", 13), bg = "Coral").place(relx = 0.3, rely = 0.4)

dir_strvar = StringVar(root)
dir_entry = Entry(root, width = 50, textvariable = dir_strvar)
dir_entry.place(relx = 0.5, rely = 0.4)

Label(root, text = "File Name", font = ("Times New Roman", 13), bg = "Coral").place(relx = 0.3, rely = 0.6)

filename_strvar = StringVar(root)
filename_entry = Entry(root, width = 50, textvariable = filename_strvar)
filename_entry.place(relx = 0.5, rely = 0.6)

download_btn = Button(root, text = "Download", font = 7, bg = "Aquamarine", command = lambda: downloader(link_entry, dir_entry, filename_entry)).place(relx = 0.3, rely = 0.75)

reset_btn = Button(root, text = "Reset", font = 7, bg = "Aquamarine", command = lambda: reset(link_strvar, dir_strvar, filename_strvar)).place(relx = 0.5, rely = 0.75)

root.update()
root.mainloop()