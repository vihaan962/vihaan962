# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:02:05 2022

@author: VIHAAN KATHURIA
"""

from tkinter import *
from PIL import ImageTk,Image
import random

root = Tk()
root.title("Endless Pokemon card game") 
root.geometry("800x600")
root.config(bg = "dark orange")

img = ImageTk.PhotoImage(Image.open("button.jpg"))
p1 = ImageTk.PhotoImage(Image.open("abra.jpg"))
p2 = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
p3 = ImageTk.PhotoImage(Image.open("charmender.jpg"))
p4 = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
p5 = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
p6 = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
p7 = ImageTk.PhotoImage(Image.open("meowth.jpg"))
p8 = ImageTk.PhotoImage(Image.open("paras.jpg"))
p9 = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
p10 = ImageTk.PhotoImage(Image.open("ratata.jpg"))
p11 = ImageTk.PhotoImage(Image.open("persion.jpg"))
p12 = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
p13 = ImageTk.PhotoImage(Image.open("squirtle.jpg"))

pokemon = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]
power = [30, 60, 50, 70, 70, 100, 60, 40, 200, 40, 70, 90, 50]

player1_label = Label(root, text = "Player 1", bg = "blue", fg = "white")
player1_label.place(relx = 0.1 ,rely = 0.3, anchor = CENTER)

player1_score = Label(root, text =  "")
player1_score.place(relx = 0.1, rely = 0.5, anchor = CENTER)

player2_label = Label(root, text = "Player 2", bg = "blue", fg = "white")
player2_label.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player2_score = Label(root, text = "")
player2_score.place(relx = 0.9, rely = 0.5, anchor = CENTER)

label = Label(root)
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

pl1_score = 0
def pl1():
    print("Player1 button")
    global pl1_score
    random_no1 = random.randint(0,12)
    random_pokemon1 = pokemon[random_no1]
    label["image"] = random_pokemon1    
    
    pl1_score = pl1_score + power[random_no1]
    player1_score["text"] = str(pl1_score)

player1_btn = Button(root, image = img, command = pl1)
player1_btn.place(relx = 0.1, rely = 0.8, anchor = CENTER)

pl2_score = 0
def pl2():
    print("Player2 button")
    global pl2_score
    random_no2 = random.randint(0,12)
    random_pokemon2 = pokemon[random_no2]
    label["image"] = random_pokemon2   
    
    pl2_score = pl2_score + power[random_no2]
    player2_score["text"] = str(pl2_score)
   

player2_btn = Button(root, image = img, command = pl2)
player2_btn.place(relx = 0.9, rely = 0.8, anchor = CENTER)


root.mainloop()

root.mainloop()