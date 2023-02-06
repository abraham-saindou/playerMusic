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
        self.frame = Frame(self.root, bg="white")
        self.frame.pack()
        self.slider_volume = None
        self.songs = []
        self.currentsong = ""
        self.paused = False
        self.random = False
        self.ticked = False
    def buttons(self):
        self.play_img = PhotoImage(file="./icons/play.png", width=50, height=50)
        self.pause_img = PhotoImage(file="./icons/pause.png", width=50, height=50)
        self.stop_img = PhotoImage(file="./icons/stop.png", width=50, height=50)
        self.back_img = PhotoImage(file="./icons/back.png", width=50, height=50)
        self.next_img = PhotoImage(file="./icons/next.png", width=50, height=50)
        self.volup_img = PhotoImage(file="./icons/vol_up.png", width=50, height=50)
        self.voldown_img = PhotoImage(file="./icons/vol_down.png", width=50, height=50)
        self.loopoff_img = PhotoImage(file="./icons/loop-off.png", width=50, height=50)
        self.loopon_img = PhotoImage(file="./icons/loop-on.png", width=50, height=50)



        self.play_btn = Button(self.frame, image=self.play_img, borderwidth=0, command=self.play_music)
        self.pause_btn = Button(self.frame, image=self.pause_img, borderwidth=0, command=self.pause_music)
        self.stop_btn = Button(self.frame, image=self.stop_img, borderwidth=0, command=self.stop_music)
        self.back_btn = Button(self.frame, image=self.back_img, borderwidth=0, command=self.back_music)
        self.next_btn = Button(self.frame, image=self.next_img, borderwidth=0, command=self.next_music)
        self.volup_btn = Button(self.frame, image=self.volup_img, borderwidth=0)
        self.voldown_btn = Button(self.frame, image=self.voldown_img, borderwidth=0)
        self.loop_btn = Button(self.frame, image=self.loopoff_img, borderwidth=0, command=self.loop)
        self.random_btn = Button(self.frame, text="random", borderwidth=0, command=self.randomizer)

        self.play_btn.grid(row=0, column=1, padx=7, pady=10)
        self.pause_btn.grid(row=0, column=2, padx=7, pady=10)
        self.stop_btn.grid(row=0, column=4, padx=7, pady=10)
        self.back_btn.grid(row=0, column=0, padx=7, pady=10)
        self.next_btn.grid(row=0, column=3, padx=7, pady=10)
        self.loop_btn.grid(row=0, column=5, padx=7, pady=10)
        self.random_btn.grid(row=1, column=0, padx=7, pady=10)
# Barre de son
        self.slider_volume = Scale(self.frame, from_=0, to=100, orient=VERTICAL, resolution=5, length=120,
                                   command=self.volume, label="Volume")
        self.slider_volume.grid(row=0, column=6)

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
        try:
            if not self.paused:
                if self.ticked is True:
                    mixer.music.load(os.path.join(self.root.directory, self.currentsong))
                    mixer.music.play(-1)
                else:
                    mixer.music.load(os.path.join(self.root.directory, self.currentsong))
                    mixer.music.play()
            else:
                mixer.music.unpause()
                self.paused = False
        except:
            pass

    def pause_music(self):
        mixer.music.pause()
        self.paused = True
        pass
    def stop_music(self):
        mixer.music.stop()
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
    def loop(self):
        if not self.ticked:
            self.ticked = True
            self.loop_btn.config(image=self.loopon_img)
        else:
            self.ticked = False
            self.loop_btn.config(image=self.loopoff_img)

    def randomizer(self):
        random.shuffle(self.songs)
        self.currentsong = self.songs[0]
        mixer.music.load(os.path.join(self.root.directory, self.currentsong))
        mixer.music.play()
    def volume(self):
        vol_current = self.slider_volume.get()
        mixer.music.set_volume(vol_current)


    def run(self):
        self.menu()
        self.buttons()
        self.root.mainloop()

if __name__ == "__main__":
    app = PlayerMusic()
    app.run()
