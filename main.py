from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os


class PlayerMusic:
    def __init__(self):

        self.root = Tk()
        self.root.title("Music Player")
        self.root.geometry("650x550")
        mixer.init()

        self.musiclist = Listbox(self.root, bg="purple", fg="white", width=100, height=15)
        self.musiclist.pack()
        self.frame = Frame(self.root, bg="white")
        self.frame.pack()
        self.vol = DoubleVar()
        self.songs = []
        self.currentsong = ""
        self.paused = self.random = self.ticked = False
    def buttons(self):
        #  Frames
        self.btn_frame = Frame(self.frame)
        self.btn_frame.grid(row=0, column=0, pady=178)
        self.slider_frame = Frame(self.root)
        self.slider_frame.place(x=530, y=320)
        #  Buttons Icons
        self.play_img = PhotoImage(file="./icons/play.png", width=50, height=50)
        self.pause_img = PhotoImage(file="./icons/pause.png", width=50, height=50)
        self.stop_img = PhotoImage(file="./icons/stop.png", width=50, height=50)
        self.back_img = PhotoImage(file="./icons/back.png", width=50, height=50)
        self.next_img = PhotoImage(file="./icons/next.png", width=50, height=50)
        self.volup_img = PhotoImage(file="./icons/vol_up.png", width=50, height=50)
        self.voldown_img = PhotoImage(file="./icons/vol_down.png", width=50, height=50)
        self.loopoff_img = PhotoImage(file="./icons/loop-off.png", width=50, height=50)
        self.loopon_img = PhotoImage(file="./icons/loop-on.png", width=50, height=50)
        #  Buttons
        self.play_btn = Button(self.btn_frame, image=self.play_img, borderwidth=0, command=self.play_music)
        self.pause_btn = Button(self.btn_frame, image=self.pause_img, borderwidth=0, command=self.pause_music)
        self.stop_btn = Button(self.btn_frame, image=self.stop_img, borderwidth=0, command=self.stop_music)
        self.back_btn = Button(self.btn_frame, image=self.back_img, borderwidth=0, command=self.back_music)
        self.next_btn = Button(self.btn_frame, image=self.next_img, borderwidth=0, command=self.next_music)
        self.loop_btn = Button(self.btn_frame, image=self.loopoff_img, borderwidth=0, command=self.loop)

        self.play_btn.grid(row=0, column=1, padx=7, pady=10)
        self.pause_btn.grid(row=0, column=2, padx=7, pady=10)
        self.stop_btn.grid(row=0, column=4, padx=7, pady=10)
        self.back_btn.grid(row=0, column=0, padx=7, pady=10)
        self.next_btn.grid(row=0, column=3, padx=7, pady=10)
        self.loop_btn.grid(row=0, column=5, padx=7, pady=10)
    # Soundbar
        self.label_up = Label(self.slider_frame, image=self.volup_img)
        self.label_down = Label(self.slider_frame, image=self.voldown_img)
        self.label_up.grid(row=0, column=0)
        self.label_down.grid(row=2, column=0)
        self.slider_volume = Scale(self.slider_frame, from_=100, to=0, orient=VERTICAL, resolution=2, length=120,
                                   command=self.volume, variable=self.vol, label="Volume")
        self.slider_volume.set(100)
        self.slider_volume.grid(row=1, column=0)

    def volume(self, p):
        self.track = self.slider_volume.get()/100
        mixer.music.set_volume(self.track)

    def menu(self):
        #  Menu
        menu_choice = Menu(self.root)
        self.root.config(menu=menu_choice)

        organize_menu = Menu(menu_choice, tearoff=False)
        menu_choice.add_cascade(label="File Managing", menu=organize_menu)
        organize_menu.add_command(label="Ajouter des musiques", command=self.add_songs)
        organize_menu.add_command(label="Supprimer des musiques", command=self.del_song)

    def add_songs(self):
        try:
            ext_list = ['.mp3', '.flac', '.aac']  # List used to check file extension
            self.root.directory = filedialog.askopenfilenames(initialdir='./')
            for song in self.root.directory:
                name, ext = os.path.splitext(song)
                if ext in ext_list:
                    self.songs.append(song)
            for song in self.songs:
                song_name = os.path.basename(song)  # Get the filename
                self.directory_name = song.replace(song_name, "")  # Get path of filename
                self.musiclist.insert(END, song_name)
            self.musiclist.selection_set(0)
            self.currentsong = self.songs[self.musiclist.curselection()[0]]
        except:
            pass

    def del_song(self):
        #  Getting selected sound
        self.currentsong = self.musiclist.index('active')
        if self.musiclist.size() > 1:
            if self.currentsong == self.musiclist.size() - 1:
                self.musiclist.selection_set(self.musiclist.size() - 2)
                self.musiclist.activate(self.musiclist.size() - 2)
            else:
                self.musiclist.selection_set(self.currentsong + 1)
                self.musiclist.activate(self.currentsong + 1)

        self.musiclist.delete(self.currentsong)
        mixer.music.stop()

    def play_music(self):
        try:
            if not self.paused:
                #  Plays concatenated path of file
                self.currentsong = self.directory_name + self.musiclist.get(ACTIVE)
                mixer.music.load(self.currentsong)
                if self.ticked is True:  # Checked if loop button is on, then play the looped file
                    mixer.music.play(-1)
                else:
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
        try:  # Set the next index of musisclist as currentsong

            self.musiclist.selection_clear(0, END)
            self.musiclist.selection_set(self.songs.index(self.currentsong) + 1)
            self.currentsong = self.songs[self.musiclist.curselection()[0]]
            mixer.music.load(self.currentsong)
            mixer.music.play()
        except:
            pass

    def back_music(self):
        try:  # Set the previous index of musisclist as currentsong
            self.musiclist.selection_clear(0, END)
            self.musiclist.selection_set(self.songs.index(self.currentsong) - 1)
            self.currentsong = self.songs[self.musiclist.curselection()[0]]
            mixer.music.load(self.currentsong)
            mixer.music.play()
        except:
            pass

    def loop(self):
        if not self.ticked:  # Change picture loop button if ticked or not
            self.ticked = True
            self.loop_btn.config(image=self.loopon_img)
        else:
            self.ticked = False
            self.loop_btn.config(image=self.loopoff_img)

    def run(self):  # Running function
        self.menu()
        self.buttons()
        self.root.mainloop()

if __name__ == "__main__":  # Create an object which uses run()
    app = PlayerMusic()
    app.run()
