from tkinter import *
from tkinter import filedialog
from pygame import mixer

import pygame.mixer_music
import os
import random


class PlayerMusic:
    def __init__(self):
        self.root = Tk()
        self.root.title("Music Player")
        self.root.geometry("500x400")
        mixer.init()

        self.musiclist = Listbox(self.root, bg="black", fg="white", width=100, height=15)
        self.musiclist.pack()

        self.songs = []
        self.currentsong = ""
        self.paused = False
    def buttons(self):
        self.play_img = PhotoImage(file="./icons/play.png", width=50, height=50)
        self.pause_img = PhotoImage(file="./icons/pause.png", width=50, height=50)
        self.stop_img = PhotoImage(file="./icons/stop.png", width=50, height=50)
        self.back_img = PhotoImage(file="./icons/back.png", width=50, height=50)
        self.next_img = PhotoImage(file="./icons/next.png", width=50, height=50)
        self.volup_img = PhotoImage(file="./icons/vol_up.png", width=50, height=50)
        self.voldown_img = PhotoImage(file="./icons/vol_down.png", width=50, height=50)

        frame = Frame(self.root, bg="white")
        frame.pack()

        self.play_btn = Button(frame, image=self.play_img, borderwidth=0, command=self.play_music)
        pause_btn = Button(frame, image=self.pause_img, borderwidth=0, command=self.pause_music)
        stop_btn = Button(frame, image=self.stop_img, borderwidth=0)
        back_btn = Button(frame, image=self.back_img, borderwidth=0, command=self.back_music)
        next_btn = Button(frame, image=self.next_img, borderwidth=0, command=self.next_music)
        volup_btn = Button(frame, image=self.volup_img, borderwidth=0)
        voldown_btn = Button(frame, image=self.voldown_img, borderwidth=0)

        self.play_btn.grid(row=0, column=1, padx=7, pady=10)
        pause_btn.grid(row=0, column=2, padx=7, pady=10)
        back_btn.grid(row=0, column=0, padx=7, pady=10)
        next_btn.grid(row=0, column=3, padx=7, pady=10)

    def menu(self):
        menu_choice = Menu(self.root)
        self.root.config(menu=menu_choice)
        organize_menu = Menu(menu_choice, tearoff=False)
        organize_menu.add_command(label="Ajouter dossier musique", command=self.add_song)
        organize_menu.add_command(label="Supprimer des musiques")
        menu_choice.add_cascade(label="File", menu=organize_menu)

    def add_song(self):
        try:
            ext_list = ['.mp3', '.flac', '.aac']
            self.root.directory = filedialog.askdirectory()
            for song in os.listdir(self.root.directory):
                name, ext = os.path.splitext(song)
                if ext in ext_list:
                    self.songs.append(song)
            for song in self.songs:
                self.musiclist.insert(END, song)
            self.musiclist.selection_set(0)
            self.currentsong = self.songs[self.musiclist.curselection()[0]]
        except:
            print("You did not select a good folder")

    def play_music(self):
        if not self.paused:
            mixer.music.load(os.path.join(self.root.directory, self.currentsong))
            mixer.music.play()
        else:
            pygame.mixer.music.unpause()
            self.paused = False
        pass

    def pause_music(self):
        mixer.music.pause()
        self.paused = True
        pass

    def next_music(self):
        try:
            self.musiclist.select_clear(0, END)
            self.musiclist.selection_set(self.songs.index(self.currentsong) + 1)
            self.currentsong = self.songs[self.musiclist.curselection()[0]]
            self.play_music()
        except:
            pass

    def back_music(self):
        try:
            self.musiclist.select_clear(0, END)
            self.musiclist.selection_set(self.songs.index(self.currentsong) - 1)
            self.currentsong = self.songs[self.musiclist.curselection()[0]]
            self.play_music()
        except:
            pass

    def volup(self):
        try:

        except:
            pass

    def run(self):
        self.menu()
        self.buttons()
        self.root.mainloop()

if __name__ == "__main__":
    app = PlayerMusic()
    app.run()
