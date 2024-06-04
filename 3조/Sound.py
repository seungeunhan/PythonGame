import pygame

pygame.init()

def BGM():
    test=pygame.mixer.Sound("LSMBG0705_신나는 명절.mp3")
    test.play(-1)

def sound():
    bgm=pygame.mixer.Sound("윷 효과음.mp3")
    bgm.play()

