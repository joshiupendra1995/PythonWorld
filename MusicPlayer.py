import pygame
from pygame import mixer
from tkinter import *
import os


def play_song():
    current_song = playlist.get(ACTIVE)
    print(current_song)
    mixer.music.load(current_song)
    song_status.set("Playing")
    mixer.music.play()


def pause_song():
    song_status.set("Paused")
    mixer.music.pause()


def stop_song():
    song_status.set("Stopped")
    mixer.music.stop()


def resume_song():
    song_status.set("Resuming")
    mixer.music.unpause()


root = Tk()
root.title('UJ Music Player')

mixer.init()
song_status = StringVar()
song_status.set("choosing")

playlist = Listbox(root, selectmode=SINGLE, bg="Red", fg="white", font=('arial', 15), width=40)
playlist.grid(columnspan=5)

os.chdir(r'D:\songs')
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

play_btn = Button(root, text="play", command=play_song)
play_btn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
play_btn.grid(row=1, column=0)

pause_btn = Button(root, text="Pause", command=pause_song)
pause_btn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
pause_btn.grid(row=1, column=1)

stop_btn = Button(root, text="Stop", command=stop_song)
stop_btn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
stop_btn.grid(row=1, column=2)

Resume_btn = Button(root, text="Resume", command=resume_song)
Resume_btn.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
Resume_btn.grid(row=1, column=3)

mainloop()
