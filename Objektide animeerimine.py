# Skoorilugejaga astutulevate autode animatsioon


# MOODULITE IMPORTIMINE
import sys  # Impordib Sys mooduli
import pygame  # Impordib PyGame mooduli

pygame.init()  # Käivitab PyGame mooduli


# EKRAAN
screenx, screeny = 640, 480  # Ekraani x ja y koordinaadid
screen = pygame.display.set_mode((screenx, screeny))  # Loob ekraani etteantud suurusega
pygame.display.set_caption("Ülesanne 4. Objektide animeerimine")  # Määran ekraanile pealkirja
clock = pygame.time.Clock()  # Kell FPS-i kontrollimiseks


# TEKSTI FONT EKRAANIL
font = pygame.font.Font(None, 30) # Määrab teksti ja fondi suuruse


# PILTIDE ÜLESLAADIMINE (kasutan üleslaadimiseks failinimesid)

# Taustapilt, laeb failist
taust = pygame.image.load("C:\\Users\\elis.poolak\\Desktop\\Tarkvaraarenduse-projekt\\Objektide animeerimine\\rally.jpg")
taust = pygame.transform.scale(taust, (screenx, screeny))  # Määran pildi suuruse sama suureks kui ekraan

# Punane auto
punane_auto = pygame.image.load("C:\\Users\\elis.poolak\\Desktop\\Tarkvaraarenduse-projekt\\Objektide animeerimine\\red.png")
punane_auto = pygame.transform.scale(punane_auto, (45, 90)) # Määran pildi suuruse

# Sinised autod
sinine_auto = pygame.image.load("C:\\Users\\elis.poolak\\Desktop\\Tarkvaraarenduse-projekt\\Objektide animeerimine\\blue.png")
sinine_auto = pygame.transform.scale(sinine_auto, (45, 90)) # Sinise auto pildi suurus
sinine_auto2 = pygame.transform.scale(sinine_auto, (45, 90))


# AUTODE ALGPOSITSIOONID
punane_x, punane_y = (320, 380)  # Punase auto algasukoht ekraanil, x ja y koordinaadid
sinine_x, sinine_y = (390, -50)  # Esimese sinise auto algpositsioon ekraanil
sinine2_x, sinine2_y = (150, 0) # Teise sinise auto algpositsioon ekraanil


# MÄÄRAN IGALE AUTOLE LIIKUMISKIIRUSE
speed_sinine, speed_sinine2 = (2, 3)


# SKOORILUGEMISSÜSTEEM
skoor = 0  # Alustab skoori lugemist nullist
gameover = False  # Mäng käima


# MÄNGU TSÜKKEL
while not gameover:  # Peamine, mängutsükkel, töötab kuni gameover = True
    clock.tick(60)  # Piirab kiiruse 60 FPS-ni sekundis
    for event in pygame.event.get():  # Loeb kõiki sündmusi ja läbib kõik sündmused ükshaaval
        if event.type == pygame.QUIT:  # Sulgeb mängu kui kasutaja vajutab X
            gameover = True  # Sulgeb programmi


# AUTODE LIIKUMINE

    # Esimese sinise auto liikumine:
    sinine_y += speed_sinine # Liikumise suund ja kiirus
    if sinine_y > screeny: # Kui esimene sinine auto jõuab akna lõppu
        sinine_y = 0 # Alustab uuesti ülevalt
        skoor += 1 # Skoor kasvab 1 võrra

    # Teise sinise auto liikumine:
    sinine2_y += speed_sinine2
    if sinine2_y > screeny:  # Kui teine sinine auto jõuab ekraani lõppu
        sinine2_y = 0  # Alustab uuesti ülevalt
        skoor += 1  # Skoor kasvab 1 võrra


# EKRAANILE PILTIDE KUVAMINE
    screen.blit(taust, (0, 0)) # Tausta kuvamine
    screen.blit(sinine_auto,(sinine_x, sinine_y)) # Sinise auto kuvamine
    screen.blit(sinine_auto2, (sinine2_x, sinine2_y)) # Teise sinise auto kuvamine
    screen.blit(punane_auto, (punane_x, punane_y)) # Punase auto kuvamine


# SKOORI KUVAMINE
    tekst = font.render("Skoor: " + str(skoor), True, (255, 255, 255)) # tekst, mida kuvatakse
    screen.blit(tekst, (10, 10))  # Kuvab teksti

    pygame.display.flip() # Uuendab ekraani

pygame.quit()  # Sulgeb PyGame'i
sys.exit()  # Prgrammi lõpetamine