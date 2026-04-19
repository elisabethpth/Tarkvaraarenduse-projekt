# MÄNG - PING PONG

import pygame # Impordib PyGame'i mooduli
import sys # Impordib süsteemifunktsioonid

pygame.init() # Käivitab PyGame'i


# EKRAANI SEADED
screenx, screeny = 640, 480 # Ekraani mõõtmed (x ja y koordinaadid)
screen = pygame.display.set_mode((screenx, screeny)) # Loob akna koordinaatide järgi
pygame.display.set_caption("Ping Pong") # Akna pealkiri
clock = pygame.time.Clock() # Kell FPS-i kontrollimiseks
roosa = (255, 102, 204) # Taustavärv, roosa RGB value

# TEKSTI FONT EKRAANIL
font = pygame.font.SysFont("Arial", 30) # Teksti font ja suurus


# OBJEKTIDE ÜLESLAADIMINE

# PALL
ball = pygame.Rect(10, 10, 20, 20) # Loon ristküliku kuhu palli paigutan
ballImage = pygame.image.load("pall.png") # Palli pilt
ballImage = pygame.transform.scale(ballImage, (20, 20)) # Pildi suurus
speedx, speedy = 4, 5 # Palli liikumiskiirus x- ja y- suunas

# ALUS
alus = pygame.Rect([100, screeny/1.5], (120,20)) # Loon ristküliku kuhu aluse paigutan
alusImage = pygame.image.load("alus.png") # Aluse pilt
alusImage = pygame.transform.scale(alusImage, (120, 20)) # Pildi suurus


# BOONUS (SKOORILUGEMISSÜSTEEM)
skoor = 0 # Alustab skoori lugemist nullist
gameover = False # Mängu olek


# PEAMINE MÄNGUTSÜKKEL
while not gameover: # Töötab kuni gameover = True

    clock.tick(60) # Piirab kiiruse 60 FPS-ni sekundis

# SÜNDMUSED
    for event in pygame.event.get(): # Loeb ja läbib kõik sündmused
        if event.type == pygame.QUIT: # Kui kasutaja vajutab X, sulgeb mängu
            pygame.quit()  # Sulgeb PyGame'i
            sys.exit() # Lõpetab programmi


# OBJEKTIDE LIIKUMINE

# Palli liikumine
    ball.x += speedx # Pall liigub horisontaalsuunas
    ball.y+= speedy # Pall liigub vertikaalsuunas

    if ball.left <= 0 or ball.right >= screenx: # Kui pall puudutab vasakut või paremat äärt
        speedx = -speedx # Pall põrkab tagasi
    if ball.top <= 0: # Kui pall puudutab ülemist või alumist äärt
        speedy = -speedy # Pall põrkab tagasi

# Aluse liikumine
    if alus.centerx < ball.centerx:  # Kui aluse keskpunkt on pallist vasakul
        alus.x += 3 # Liiguta alust paremale palli suunas
    elif alus.centerx > ball.centerx:  # Kui aluse keskpunkt on pallist paremal
        alus.x -= 3 # Liiguta alust vasakule palli suunas
        
    alus.x = max(0, min(alus.x, screenx - alus.width)) # Piirab aluse liikumise

# KOKKUPÕRGETE TUVASTAMINE
    if ball.colliderect(alus): # Kui pall puudutab alust
        if speedy > 0: # Kontrollib palli kiirust
            ball.bottom = alus.top # Kui pall puudutab alust pealt
            skoor += 1 # Saab +1 punkti
        else:
            ball.top = alus.bottom # Kui pall puudutab alust alt poolt

        speedy = -speedy # Pall põrkab mõlemal juhul tagasi

    if ball.bottom >= screeny: # Kui pall puudutab ekraani alumist äärt
        speedy = -speedy # Pall põrkab tagasi
        skoor -= 1 # Kaotab ühe punkti


# EKRAANILE PILTIDE KUVAMINE
    screen.fill(roosa) # Taustavärvi värskendamine

    screen.blit(alusImage, alus) # Aluse kuvamine ekraanile
    screen.blit(ballImage, ball) # Palli kuvamine ekraanile

# SKOORI KUVAMINE
    tekst = font.render("Skoor: " + str(skoor), True, (255, 255, 255)) # Tekst, mida kuvatakse
    screen.blit(tekst, (10, 10)) # Kuvab skoori ekraanile antud koordinaatides

    pygame.display.flip() # Uuendab ekraani

pygame.quit() # Sulgeb PyGame'i
sys.exit() # Programmi lõpetamine