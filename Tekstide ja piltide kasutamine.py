import pygame # Impordib PyGame mooduli
import math # Imporidb math mooduli

pygame.init() # Käivitab PyGame mooduli

# Ekraani loomine
screen = pygame.display.set_mode((640, 480)) # Ekraani suurus
pygame.display.set_caption("Ülesanne 2") # Ekraani pealkiri

# Fondi määramine
font = pygame.font.SysFont("Arial", 40) # Tavalise fondi suurus

# PILDID

shop = pygame.image.load("C:\\Users\\elis.poolak\\Desktop\\Tarkvaraarenduse-projekt\\pood.jpg") # Pildi path

man = pygame.image.load("C:\\Users\\elis.poolak\\Desktop\\Tarkvaraarenduse-projekt\\mees.png") # Pildi path
man = pygame.transform.scale(man, (233, 275)) # Pildi suurus

textbox = pygame.image.load("C:\\Users\\elis.poolak\\Desktop\\Tarkvaraarenduse-projekt\\tekstkast.png") # Pildi path
textbox = pygame.transform.scale(textbox, (285, 226)) # Pildi suurus

sword = pygame.image.load("C:\\Users\\elis.poolak\\Desktop\\Tarkvaraarenduse-projekt\\Mõõk.png") # Pildi path
sword = pygame.transform.scale(sword, (157, 130)) # Pildi suurus

cake = pygame.image.load("C:\\Users\\elis.poolak\\Desktop\\Tarkvaraarenduse-projekt\\cake.png") # Pildi path
cake = pygame.transform.scale(cake, (107, 127)) # Pildi suurus

logo = pygame.image.load("C:\\Users\\elis.poolak\\Desktop\\Tarkvaraarenduse-projekt\\vikklogo.png") # Pildi path
logo = pygame.transform.scale(logo, (640, 480)) # Pildi suurus

# Tsükkel
work = True # Näitab kas tsükkel töötab
clock = pygame.time.Clock() # Loob kella FPS-i kontrollimiseks

while work:  # Tsükkel töötab seni, kuni work on True
    for event in pygame.event.get():  # Võtab kõik Pygame sündmused (klikk, klaviatuur, akna tegevused)
        if event.type == pygame.QUIT: # X vajutamisel PyGame sulgub
            work = False # Lõpetab while-tsükli ja sulgeb mängu

# Taust
    screen.blit(shop, (0, 0))

# Objektide asetus ekraanil
    screen.blit(man, (110, 185)) # x ja y koordinaadid
    screen.blit(textbox, (235, 50))
    screen.blit(sword, (510, 100))
    screen.blit(cake, (400, 170))
    screen.blit(logo, (10, 10))

# Tekst "Tere olen Elis" tekstikasti
    text = font.render("Tere, olen Elis", True, (255, 255, 255))
    screen.blit(text, (270, 120)) # Teksti asetus

    pygame.display.flip() # Uuendab kogu ekraani sisu
    clock.tick(60) # Määrab mägutsükli 60 FPS peale

pygame.quit() # Sulgeb PyGame akna