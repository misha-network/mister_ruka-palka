## Basic Game on GiveAGame

# Import basic libs
from tkinter import * 
import random
import time

# Import game engine libs
from giveagame.Coords import *
from giveagame.GUI import *
from giveagame.sprites.DoorSprite import *
from giveagame.sprites.MovingPlatformSprite import *
from giveagame.sprites.PlatformSprite import *
from giveagame.sprites.Sprite import *
from giveagame.sprites.StickFigureSprite import * 
from giveagame.Game import *

g = Game("Мистер Рука-Палка бежит до выхода", 500, 500, "imgs/background.gif")
gui = GUI(g.tk, g)

platform1 = PlatformSprite(g, PhotoImage(file="imgs/platform1.gif"), \
                           0, 480, 100, 10)
platform2 = MovingPlatformSprite(g, PhotoImage(file="imgs/platform1.gif"), \
                           150, 440, 100, 10)
platform3 = PlatformSprite(g, PhotoImage(file="imgs/platform1.gif"), \
                           300, 400, 100, 10)
platform4 = PlatformSprite(g, PhotoImage(file="imgs/platform1.gif"), \
                           300, 160, 100, 10)
platform5 = PlatformSprite(g, PhotoImage(file="imgs/platform2.gif"), \
                           175, 350, 66, 10)
platform6 = PlatformSprite(g, PhotoImage(file="imgs/platform2.gif"), \
                           50, 300, 66, 10)
platform7 = PlatformSprite(g, PhotoImage(file="imgs/platform2.gif"), \
                           170, 120, 66, 10)
platform8 = PlatformSprite(g, PhotoImage(file="imgs/platform2.gif"), \
                           45, 60, 66, 10)
platform9 = PlatformSprite(g, PhotoImage(file="imgs/platform3.gif"), \
                           170, 250, 32, 10)
platform10 = PlatformSprite(g, PhotoImage(file="imgs/platform3.gif"), \
                           240, 500, 42, 10)
door = DoorSprite(g, 45, 30, 40, 35)
sf = StickFigureSprite(g)
g.sprites.append(platform1)
g.sprites.append(platform2)
g.sprites.append(platform3)
g.sprites.append(platform4)
g.sprites.append(platform5)
g.sprites.append(platform6)
g.sprites.append(platform7)
g.sprites.append(platform8)
g.sprites.append(platform9)
g.sprites.append(platform10)
g.sprites.append(door)
g.sprites.append(sf)

if __name__ == "__main__":
    g.mainloop()
