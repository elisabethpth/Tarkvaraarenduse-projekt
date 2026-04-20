# MÄNG - PING PONG

import pygame  # Impordib PyGame'i mooduli
import random # Impordib Random mooduli
import sys  # Impordib süsteemifunktsioonid

pygame.init()  # Käivitab PyGame'i


# EKRAANI SEADED
screenx, screeny = 640, 480  # Ekraani mõõtmed (x ja y koordinaadid)
screen = pygame.display.set_mode((screenx, screeny))  # Loob akna koordinaatide järgi
pygame.display.set_caption("Ping Pong")  # Akna pealkiri
clock = pygame.time.Clock()  # Kell FPS-i kontrollimiseks
roosa = (255, 102, 204)  # Taustavärv, roosa RGB value

# TEKSTI FONT EKRAANIL
font = pygame.font.SysFont("Arial", 30)  # Teksti font ja suurus

# TAUSTAHELI FAILID
sounds = ["tune1.wav", "tune2.wav", "tune3.wav", "tune4.wav", "tune5.wav"]
pygame.mixer.music.load(random.choice(sounds)) # Valib juhuslikult ühe helifaili ja laeb selle PyGame'i moodulisse
pygame.mixer.music.play() # Aalustab taustamuusika esitamist


# OBJEKTIDE ÜLESLAADIMINE

# PALL
ball = pygame.Rect(10, 10, 20, 20)  # Loon ristküliku kuhu palli paigutan
ballImage = pygame.image.load("pall.png")  # Palli pilt
ballImage = pygame.transform.scale(ballImage, (20, 20))  # Pildi suurus
speedx, speedy = 4, 5  # Palli liikumiskiirus x- ja y- suunas

# ALUS
alus = pygame.Rect([100, screeny / 1.5], (120, 20))  # Loon ristküliku kuhu aluse paigutan
alusImage = pygame.image.load("alus.png")  # Aluse pilt
alusImage = pygame.transform.scale(alusImage, (120, 20))  # Pildi suurus

# BOONUS (SKOORILUGEMISSÜSTEEM)
skoor = 0  # Alustab skoori lugemist nullist
gameover = False  # Mängu olek

# PEAMINE MÄNGUTSÜKKEL
while not gameover:  # Töötab kuni gameover = True
    clock.tick(60)  # Piirab kiiruse 60 FPS-ni sekundis

# SÜNDMUSED
    for event in pygame.event.get():  # Loeb ja läbib kõik sündmused
        if event.type == pygame.QUIT:  # Kui kasutaja vajutab X, sulgeb mängu
            pygame.quit()  # Sulgeb PyGame'i
            sys.exit()  # Lõpetab programmi


# OBJEKTIDE LIIKUMINE

# Palli liikumine
    ball.x += speedx  # Pall liigub horisontaalsuunas
    ball.y += speedy  # Pall liigub vertikaalsuunas

    if ball.left <= 0 or ball.right >= screenx:  # Kui pall puudutab vasakut või paremat äärt
        speedx = -speedx  # Pall põrkab tagasi
    if ball.top <= 0:  # Kui pall puudutab ülemist või alumist äärt
        speedy = -speedy  # Pall põrkab tagasi

# Aluse liikumine
    keys = pygame.key.get_pressed() # Loeb klahvide hetkeseisundit

    if keys[pygame.K_LEFT]: # Kui vajutatakse vasakut noolt
        alus.x -= 5 # Liigutab alust vasakule 5 pikslit

    if keys[pygame.K_RIGHT]: # Kui vajutatakse paremat noolt
        alus.x += 5 # Liigutab alust paremale 5 pikslit

    alus.x = max(0, min(alus.x, screenx - alus.width))  # Piirab aluse liikumist ekraani piires


# KOKKUPÕRGETE TUVASTAMINE
    if ball.colliderect(alus):  # Kui pall puudutab alust

        if speedy > 0:  # Kontrollib palli kiirust
            ball.bottom = alus.top  # Kui pall puudutab alust pealt
            hit_sound = pygame.mixer.Sound("Hit.wav") # Heli, mida mängitakse
            pygame.mixer.Sound.play(hit_sound) # Mängib heli, kui pall puutub alust
            skoor += 1  # Saab +1 punkti
        else:
            ball.top = alus.bottom  # Kui pall puudutab alust alt poolt

        speedy = -speedy  # Pall põrkab mõlemal juhul tagasi

    if ball.bottom >= screeny:  # Kui pall puudutab ekraani alumist äärt
        hit_sound = pygame.mixer.Sound("PowerUp.wav")  # Heli, mida mängitakse
        pygame.mixer.Sound.play(hit_sound)  # Mängib heli, kui pall puutub alumist äärt
        gameover = True # Lõpetab mängu

# EKRAANILE PILTIDE KUVAMINE
    screen.fill(roosa)  # Taustavärvi värskendamine

    screen.blit(alusImage, alus)  # Aluse kuvamine ekraanile
    screen.blit(ballImage, ball)  # Palli kuvamine ekraanile

# SKOORI KUVAMINE
    tekst = font.render("Skoor: " + str(skoor), True, (255, 255, 255))  # Tekst, mida kuvatakse
    screen.blit(tekst, (10, 10))  # Kuvab skoori ekraanile antud koordinaatides

    pygame.display.flip()  # Uuendab ekraani

screen.fill(roosa) # Roosa taust
tekst = font.render("GAME OVER", True, (255, 255, 255)) # Kuvab teksti "Game over"
screen.blit(tekst, (240, 200)) # Kuhu tekst kuvatakse
pygame.display.flip() # Uuendab ekraani
pygame.time.wait(3000) # Hoiab ekraani avatuna

pygame.quit()  # Sulgeb PyGame'i
sys.exit()  # Programmi lõpetamine