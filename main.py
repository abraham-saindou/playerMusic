from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os


class PlayerMusic:
    def __init__(self):
        self.root = Tk()
        self.root.title("Music Player")
        self.root.geometry("500x300")
        mixer.init()

        self.musiclist = Listbox(self.root, bg="black", fg="white", width=100, height=15)
        self.musiclist.pack()

        self.songs = []
        self.currentsong = ""
        pause = False
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

        self.play_btn = Button(frame, image=self.play_img, borderwidth=0)
        pause_btn = Button(frame, image=self.pause_img, borderwidth=0)
        stop_btn = Button(frame, image=self.stop_img, borderwidth=0)
        back_btn = Button(frame, image=self.back_img, borderwidth=0)
        next_btn = Button(frame, image=self.next_img, borderwidth=0)
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
        organize_menu.add_command(label="Selectionner un Dossier", command=self.play_song())
        menu_choice.add_cascade(label="Organize", menu=organize_menu)

    def play_song(self):
        self.root.directory = filedialog.askdirectory()
        for song in os.listdir(self.root.directory):
            name, ext = os.path.splitext(song)
            if ext == '.mp3':
                self.songs.append(song)
        for song in songs:
            self.musiclist.insert(END, song)
        self.musiclist.selection_set(0)
        self.currentsong = self.songs[self.musiclist.curselection()[0]]
    def run(self):
        self.menu()
        self.buttons()
        self.root.mainloop()

if __name__ == "__main__":
    app = PlayerMusic()
    app.run()
