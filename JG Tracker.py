import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time
import pygame
import shutil
import random
import tkinter as tk
from tkinter import *
from os import path
from PIL import ImageTk, Image

#-----------------------------Initialize Time for Each Camp---------------------------------
#develop timer + tracker

def top():
    top.blue = '05:00'
    top.gromp = '02:00'
    top.wolves = '02:00'
    top.chickens = '02:00'
    top.red = '05:00'
    top.krugs = '02:00'
    top.scuttle = '05:40'
top()

def bot():
    bot.blue = '05:00'
    bot.gromp = '02:00'
    bot.wolves = '02:00'
    bot.chickens = '02:00'
    bot.red = '05:00'
    bot.krugs = '02:00'
    bot.scuttle = '05:40'
bot()

def epicMonsters():
    epicMonsters.drag = '05:00'
    epicMonsters.herald = '06:00'
    epicMonsters.baron = '06:00'
epicMonsters()

#-----------------------------JG Camp Spawn Timers-------------------------------
root = Tk()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open("SR.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=-250, y=0)

        loadJG = Image.open("kharesized.png")
        renderJG = ImageTk.PhotoImage(loadJG)
        global imgJG
        imgJG = Label(self, image=renderJG, width=45, height =45)
        imgJG.image = renderJG

    def top_grompPosition(self):
        monsterTimer = top.gromp

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)
        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        topGromp = Label(root, text="Top Gromp\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=205, y=370)
        topGromp.place(x=180, y=350)

    def bot_grompPosition(self):
        monsterTimer = bot.gromp

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)
        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        botGromp = Label(root, text="Bot Gromp\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=925, y=590)
        botGromp.place(x=900, y=570)

    def top_wolvesPosition(self):
        monsterTimer = top.wolves

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)
        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        topWolves = Label(root, text="Top Wolves\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=825, y=370)
        topWolves.place(x=800, y=350)

    def bot_wolvesPosition(self):
        monsterTimer = bot.wolves

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)
        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        botWolves = Label(root, text="Bot Wolves\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=325, y=600)
        botWolves.place(x=300, y=580)

    def top_redPosition(self):
        monsterTimer = top.red

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)
        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        topRed = Label(root, text="Top Red\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=610, y=270)
        topRed.place(x=600, y=250)

    def bot_redPosition(self):
        monsterTimer = bot.red

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)

        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        botRed = Label(root, text="Bot Red\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=510, y=670)
        botRed.place(x=500, y=650)

    def top_bluePosition(self):
        monsterTimer = top.blue

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)
        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        topBlue = Label(root, text="Top Blue\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=310, y=425)
        topBlue.place(x=300, y=400)

    def bot_bluePosition(self):
        monsterTimer = bot.blue

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)

        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        botBlue = Label(root, text="Bot Blue\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=770, y=520)
        botBlue.place(x=760, y=500)

    def top_chickensPosition(self):
        monsterTimer = top.chickens

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)
        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        topChickens = Label(root, text="Top Chickens\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=525, y=390)
        topChickens.place(x=500, y=370)

    def bot_chickensPosition(self):
        monsterTimer = bot.chickens

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)

        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        botChickens = Label(root, text="Bot Chickens\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=575, y=570)
        botChickens.place(x=550, y=550)

    def top_krugsPosition(self):
        monsterTimer = top.krugs

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)
        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        topKrugs = Label(root, text="Top Krugs\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=510, y=170)
        topKrugs.place(x=500, y=145)

    def bot_krugsPosition(self):
        monsterTimer = bot.krugs

        def converter(sec):
            m, s = map(int, sec.split(":"))
            sec = m * 60 + s
            sec -= 1
            m, s = divmod(sec, 60)
            sec = (f'{m:02d}:{s:02d}')
            if sec == '00:00':
                sec = 'RESPAWNED'
            btn_text.set(sec)
            if sec != "RESPAWNED":
                root.after(1000, converter, sec)

        btn_text = tk.StringVar()
        btn_text.set(monsterTimer)
        botKrugs = Label(root, text="Bot Krugs\n")
        btn = tk.Button(root, textvariable=btn_text, command=lambda: converter(monsterTimer))
        btn.place(x=655, y=815)
        botKrugs.place(x=645, y=790)

    #Baron, Herald, Drag have built in timers so don't need

#------------------------------Predicting JG Position----------------------------
    #Start bot blue start top red
    def blueJG(self):
        imgJG.place(x=600, y=660)
        imgJG.place(x=700, y=860)



    #def redJG(self):
    #    imgJG.place(x=820, y=500)


#add function to show/ dont show timers




app = Window(root)
#app.campPosition()
app.top_grompPosition()
app.bot_grompPosition()
app.top_wolvesPosition()
app.bot_wolvesPosition()
app.top_redPosition()
app.bot_redPosition()
app.top_bluePosition()
app.bot_bluePosition()
app.top_chickensPosition()
app.bot_chickensPosition()
app.top_krugsPosition()
app.bot_krugsPosition()

app.blueJG()
#app.redJG()


#def hideButtons():
#    hideButtons = tk.Button(root, text='Click to hide Label', command=lambda: app.bot_krugsPosition().botKrugs.pack_forget())
#    hideButtons.pack()
#
#
#
#hideButtons()
root.wm_title("JG Tracker")
root.geometry("1125x950")
root.mainloop()








