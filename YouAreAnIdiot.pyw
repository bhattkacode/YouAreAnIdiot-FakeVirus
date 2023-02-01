from tkinter import *
from tkinter import ttk
from pygame import mixer
from time import sleep
from random import randrange
from math import pi, sin, cos, radians
import pygame

mixer.init()


class newWin():
    def __init__(self):
        self.velx = randrange(5, 100, 5)
        self.vely = randrange(5, 100, 5)
        self.win = Toplevel()
        self.win.resizable(False, False)
        self.win.title("You Are An Idiot")
        self.width = randrange(75, 350, 25)
        self.height = randrange(75, 350, 25)
        self.x = randrange(10, 1000-self.width)
        self.y = randrange(10, 800-self.height)
        self.win.geometry(
            f"{str(self.width)}x{str(self.height)}")
        self.win.geometry(f"+{self.x}+{self.y}")
        self.pos = (self.x, self.y)
        self.win.wm_attributes("-topmost", 1)
        # self.win.overrideredirect(True)
        self.win.iconbitmap(iconpath)

    def move(self):
        sWidth = self.win.winfo_screenwidth()
        sHeight = self.win.winfo_screenheight()
        x = self.pos[0]+self.velx
        y = self.pos[1]+self.vely
        self.win.geometry(f"+{str(x + self.velx)}+{str(y + self.vely)}")
        downx, downy = x+self.width, y+self.height
        if x < 0 or downx >= sWidth-20:
            self.velx = -self.velx
        if y < 0 or downy >= sHeight-75:
            self.vely = -self.vely
        self.pos = (x, y)

    def makeImg(self):
        imgbtn = Button(self.win, image=smily)
        imgbtn.pack()

    def close(self):
        self.win.destroy()


def lol():
    kekw = Toplevel()
    sWidthKek = kekw.winfo_screenwidth()
    sHeightKek = kekw.winfo_screenheight()
    kekw.geometry(
        f"250x250+{randrange(0,sWidthKek-300,100)}+{randrange(0,sHeightKek-300,75)}")
    kekw.title("kek")
    kekw.overrideredirect(1)
    Bkekw = Button(kekw, image=Kidiot)
    Bkekw.pack()
    kekList.append(kekw)


def anotherOne():
    global winList
    winList.append(newWin())


def nothing():
    pass


def start_crazy():
    # CIRCLE
    start.withdraw()
    CORx = 550
    CORy = 200
    radius = 275
    angle = radians(45)
    omega = 0.4
    x = CORx + radius * cos(angle)
    y = CORy - radius * sin(angle)
    # others
    for k in kekList:
        k.destroy()
    nope.destroy()
    yes.destroy()
    idk.destroy()
    pygame.mixer.music.load(crazySongPath)
    pygame.mixer.music.play()
    winList.extend([newWin(), newWin(), newWin()])
    t = 0
    c = 0
    crazy = False
    cirkleMade = False
    while True:
        if crazy == False:
            if pygame.mixer.music.get_pos() > 11000:
                crazy = True
        if not cirkleMade:
            if crazy:
                BBidiot.destroy()
                BWidiot.destroy()
                circle = Toplevel()
                circle.geometry("250x250")
                circle.title("kek")
                circle.overrideredirect(1)
                Bckekw = Button(circle, image=Kidiot)
                Bckekw.pack()
                circle.wm_attributes("-topmost", 1)
                winList.extend([newWin(), newWin(), newWin()])
                cirkleMade = True
        start.protocol("WM_DELETE_WINDOW", anotherOne)
        for w in winList:
            w.move()
            w.makeImg()
            w.win.update()
        if t == 200:
            winList.extend([newWin()])
            t = 0
        t += 2
        c += 1
        if crazy:
            circle.geometry(f"+{int(x)}+{int(y)}")
            angle = angle + omega
            x = x + radius * omega * cos(angle + pi / 2)
            y = y - radius * omega * sin(angle + pi / 2)
            circle.update()
        start.update()
        sleep(1/fps)


songPath = "resources/youAreAnIdiot.mp3"
crazySongPath = "resources/you are an idiot.mp3"
Wpath = "resources/white idiot.png"
Bpath = "resources/black idiot.png"
Kpath = "resources/kekw.png"
iconpath = "resources/YAAIicon.ico"
smilypath = "resources/YAAIicon.png"
fps = 40
mixer.music.load(songPath)
winList = []
start = Tk()
start.title("You Are An Idiot")
start.resizable(False, False)
width = 520
height = 480
start.geometry(f"{str(width)}x{str(height)}")
start.geometry("+400+100")
start.wm_attributes("-topmost", 1)
start.overrideredirect(True)
start.iconbitmap()
Widiot = PhotoImage(file=Wpath)
Bidiot = PhotoImage(file=Bpath)
Kidiot = PhotoImage(file=Kpath)
smily = PhotoImage(file=smilypath)
BWidiot = Button(start, image=Widiot)
BBidiot = Button(start, image=Bidiot)
a = 1
b = 0
kekList = []
nope = ttk.Button(start, text="No I am not",
                  command=start_crazy, width=15)
idk = ttk.Button(start, text="IDK", command=start_crazy, width=15)
yes = ttk.Button(start, text="Yes I am", command=lol, width=15)
nope.place(x=15, y=450)
idk.place(x=180, y=450)
yes.place(x=365, y=450)
mixer.music.play(-1)
start.protocol("WM_DELETE_WINDOW", nothing)
while True:
    if a == 1:
        BBidiot.pack_forget()
        BWidiot.pack()
        a = 1
    if a == 2:
        BWidiot.pack_forget()
        BBidiot.pack()
        a = 0
    a += 1
    start.update()
    sleep(0.42)
