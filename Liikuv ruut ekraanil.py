# Liikuv ruut ekraanil

import pygame # Impordib pygame mooduli

pygame.init() # Käivitab mooduli

laius = 800 # Akna laius
korgus = 600 # Akna kõrgus
ekraan = pygame.display.set_mode((laius, korgus)) # Loob akna
pygame.display.set_caption("Liikuv ruut") # Akna pealkiri

lilla = (255, 0, 255) # Taustavärv
roosa = (227, 61, 148) # Ruudu värv

x = laius // 2 # Ruut algab ekraani keskel (x)
y = korgus // 2 # Ruut alganb ekraani keskel (y)
ruudu_suurus = 50 # Ruudu suurus
kiirus = 1 # Liikumise kiirus pikslites

too_kaib = True # Tsükkel töötab, kuni on True

while too_kaib: # Tsükkel klahvide liigutamiseks
    for sundmus in pygame.event.get(): # Loeb toimuvaid sündmusi
        if sundmus.type == pygame.QUIT: # Kui vajutatakse X
            too_kaib = False # Tsükkel lõpeb

# Kontrollib klahvide olekut
    klahvid = pygame.key.get_pressed()

# Liikumine vastavalt nooleklahvidele
    if klahvid[pygame.K_LEFT]: # Vasakule
        x -= kiirus
    if klahvid[pygame.K_RIGHT]: # Paremale
        x += kiirus
    if klahvid[pygame.K_UP]: # Üles
        y -= kiirus
    if klahvid[pygame.K_DOWN]: # Alla
        y += kiirus

    ekraan.fill(lilla) # Värvib tausta
# Joonistab ruudu
    pygame.draw.rect(ekraan, roosa, (x, y, ruudu_suurus, ruudu_suurus))

    pygame.display.flip() # Uuendab ekraani
pygame.quit() # Sulgeb PyGame'i