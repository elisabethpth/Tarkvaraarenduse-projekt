# Lumememm

import pygame # Improdib PyGame mooduli
pygame.init() # Käivitab mooduli

screen = pygame.display.set_mode((300, 300)) # Loob ekraani
pygame.display.set_caption("Lumememm-Elis Poolak") # Ekraani pealkiri

# Värvid, mida kasutan
white = (255, 255, 255) # Lumememm (keha)
black = (0, 0, 0) # Silmad ja nööbid
brown = (70, 40, 20) # Käed, hari, müts
orange = (255, 165, 0) # Nina
blue = (135, 206, 235)  # Taust
grey = (191, 205, 219) # Pilved
yellow = (255, 255, 0) # Päike

work = True  # Näitab, kas programm töötab veel

while work:  # Peamine mängutsükkel - töötab, kuni too_kaib on True
    for event in pygame.event.get():  # Loeb sündmusi nagu klikk, klaviatuur, akna sulgemine jne
        if event.type == pygame.QUIT:  # Kontrollib, kas kasutaja vajutas akna sulgemise nuppu
            work = False  # Kui jah, siis lõpetab tsükli ja mäng sulgub

# Taustavärv
    screen.fill(blue)

# Lumememme keha
    pygame.draw.circle(screen, white, [150, 100], 30) # Pea, ülemine pall
    pygame.draw.circle(screen, white, [150, 160], 40) # Keha, keskmine pall
    pygame.draw.circle(screen, white, [150, 240], 50) # Keha, alumine pall

# Silmad
    pygame.draw.circle(screen, black, [140, 95], 4)
    pygame.draw.circle(screen, black, [160, 95], 4)

# Nina
    pygame.draw.polygon(screen, orange, [(150, 115), (145, 100), (155, 100)])

# Nööbid (3)
    pygame.draw.circle(screen, black, (150, 145), 3)
    pygame.draw.circle(screen, black, (150, 160), 3)
    pygame.draw.circle(screen, black, (150, 175), 3)

# Käed
    pygame.draw.line(screen, brown, (185,150), (220, 145),4)
    pygame.draw.line(screen, brown, (115,150), (80, 145),4)

# Harja vars
    pygame.draw.line(screen, brown, (218, 200), (218, 125),6)
# Harja ots
    pygame.draw.line(screen, brown, (218, 126), (218, 95), 4)
    pygame.draw.line(screen, brown, (218, 126), (230, 95), 4)
    pygame.draw.line(screen, brown, (218, 126), (206, 95), 4)

# Mütsi äär
    pygame.draw.rect(screen, brown, (120, 70, 60, 9))
# Mütsi ülemine osa
    pygame.draw.rect(screen, brown, (130, 35, 40, 40))

# Päike
    pygame.draw.circle(screen, yellow, (65, 50), 25)

# Päikesekiired
    pygame.draw.line(screen, yellow, (65, 95), (65,5),2) # Vertikaalsed kiired
    pygame.draw.line(screen, yellow, (110, 50), (20, 50), 2)  # Horisontaalsed kiired
# Diagonaalsed päikesekiired
    step = 32 # Kiirte pikkus
    pygame.draw.line(screen, yellow,(65 - step, 50 - step), (65 + step, 50 + step), 2)
    pygame.draw.line(screen, yellow,(65 + step, 50 - step),(65 - step, 50 + step),2)

# Funktsioon ühe pilve joonistamiseks, neli omavahel ühendatud ringi
    def draw_cloud(surface, x, y):
        pygame.draw.circle(surface, grey, (x, y), 13)
        pygame.draw.circle(surface, grey, (x + 20, y + 5), 15)
        pygame.draw.circle(surface, grey, (x - 20, y + 5), 15)
        pygame.draw.circle(surface, grey, (x, y + 12), 13)

# Pilved
    draw_cloud(screen, 250, 47) # Pilv 1
    draw_cloud(screen, 280, 12) # Pilv 2
    draw_cloud(screen, 200, 14) # Pilv 3

# Uuendab ekraani, et kõik elemendid ilmuks
    pygame.display.flip()
pygame.quit() # Sulgeb PyGame'i