# Valgusfoor

import pygame # Impordib PyGame mooduli
pygame.init() # Käivitab mooduli

screen = pygame.display.set_mode((300, 300)) # Loon akna
pygame.display.set_caption("Valgusfoor-Elis Poolak") # Akna pealkiri

# Värvid, mida kasutan

red = (255, 0, 0) # Valgusfoori punane
yellow = (255, 255, 0) # Valgusfoori kollane
green = (0, 255, 0) # Valgusfoori roheline
blue = (0, 0, 255) # Eesti lipu tegemiseks
black = (0, 0, 0) # Eesti lipu tegemiseks
white = (255, 255, 255) # Eesti lipu tegemiseks
pink = (255, 0, 255) #Taustavärv

work = True  # Näitab, kas programm töötab veel

while work:  # Peamine mängutsükkel - töötab, kuni too_kaib on True
    for event in pygame.event.get():  # Loeb sündmusi nagu klikk, klaviatuur, akna sulgemine jne
        if event.type == pygame.QUIT:  # Kontrollib, kas kasutaja vajutas akna sulgemise nuppu
            work = False  # Kui jah, siis lõpetab tsükli ja mäng sulgub

# Taustavärv
    screen.fill(pink) # Roosa taust

# Valgusfoori korpus
    pygame.draw.rect(screen, black, (120, 30, 60, 160)) # Must ristkülik
# Valgusfoori tuled
    pygame.draw.circle(screen, red, (150, 60), 19) # Punane tuli
    pygame.draw.circle(screen, yellow, (150, 105), 19) # Kollane tuli
    pygame.draw.circle(screen, green, (150, 150), 19) # Roheline tuli

# Valgusfoori post
    pygame.draw.rect(screen, black, (145, 190, 10, 60))

# Must trapets (postialus)
    polygon = [(90, 287.5), (210, 287.5), (165, 242.5), (135, 242.5)]
    pygame.draw.polygon(screen, black, polygon)
# Sinine trapets (postialus)
    polygon_2 = [(135, 242.5), (165, 242.5), (180, 257.5), (120, 257.5)]
    pygame.draw.polygon(screen, blue, polygon_2)
# Valge trapets (postialus)
    polygon_3 = [(105, 272.5), (195, 272.5), (210, 287.5), (90, 287.5)]
    pygame.draw.polygon(screen, white, polygon_3)

    pygame.display.flip() # Uuendab ekraani, et kõik elemendid ilmuks
pygame.quit() # Sulgeb PyGame'i
