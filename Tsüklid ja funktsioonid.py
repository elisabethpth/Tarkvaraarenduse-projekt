# Tsüklid ja funktsioonid

import pygame # Impordib PyGame mooduli
import sys # Impordib Sys mooduli

pygame.init() # Käivitab PyGame mooduli

# Värvid, mida kasutan
red = (255, 0, 0) # Punase värvi RGB value
pink = (255, 105, 180) # Roosa värvi RGB value

# Ekraani seaded
width = 640 # Laius
height = 480 # Kõrgus
square = 10 # Ruudu küljepikkus

screen = pygame.display.set_mode((width, height)) # Akna suurus
pygame.display.set_caption("Ülesanne 3") # Määrab mängule nime

running = True # Loob muutuja, mis hoiab mängutsükli aktiivsena

while running: # Peamine mängutsükkel
    screen.fill(pink)  # Värvib tausta roosaks

    for event in pygame.event.get(): # Käib läbi kõik sündmused (nt. klikk, klahvivajutus, akna sulgemine)
        if event.type == pygame.QUIT: # Kontrollib, kas kasutaja sulges mänguakna (X)
            running = False # Lõpetab mängutsükli

    # Ruudustiku joonistamine
    for y in range(0, height, square): # Käib läbi kõik y-koordinaadid 0 + samm "square" ehk 10
        for x in range(0, width, square): # Käib läbi kõik x-koordinaadid 0 + samm "square" ehk 10
            rect = pygame.Rect(x, y, square, square)# Loob ristküliku
            pygame.draw.rect(screen, (red), rect, 1)  # Joonistab ruudu ekraanile (1 = joonistab ainult ääre)

    pygame.display.flip() # Uuendab ekraani

pygame.quit() # Sulgeb PyGame'i
sys.exit() # Programmi lõpetamine