from tkinter import *
fen = Tk()

import pygame
pygame.init()
son_touche_a = pygame.mixer.Sound("C:/laragon/www/py-keyboard/sons/crash.wav")
son_touche_z = pygame.mixer.Sound("C:/laragon/www/py-keyboard/sons/miaou.wav")


def press(event):
    print(event.keysym)
    if event.keysym == 'a':
        son_touche_a.play()
    if event.keysym == 'Return':
        son_touche_z.play()
        
# def release(event):
#     print(event.keysym)
# test
fen.bind_all('<KeyPress>', press)
# fen.bind_all('<KeyRelease>', release)
fen.mainloop()


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             print("Touche enfoncée : ", event.key)
#             if event.key == pygame.K_a:
#                 print("Touche 'a' détectée")
#                 son_touche_a.play()
#                 pygame.time.delay(100)
#             elif event.key == pygame.K_z:
#                 print("Touche 'z' détectée")
#                 son_touche_b.play()
#                 pygame.time.delay(100)