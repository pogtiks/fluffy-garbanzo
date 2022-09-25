import pygame
import time
import os


#
file=r'C:\SHUTDOWN\SUCK\phonk (2).mp3'
# Инициализация
pygame.mixer.init()
#
track = pygame.mixer.music.load(file)
# Начать играть в музыкальный поток
pygame.mixer.music.play()

timer = 55
for k in range(timer):
    time.sleep(1)
    print(timer)
    timer -= 1
    if timer == 0:
        break

os.system('shutdown -s')