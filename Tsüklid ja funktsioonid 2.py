# Tsüklid ja funktsioonid

import pygame # Impordib PyGame mooduli
import sys # Impordib Sys mooduli

# Sisend kasutajalt andmete küsimiseks
square_size = int(input("Ruudu suurus: ")) # Küsib ruudu suurust
rows = int(input("Ridade arv: ")) # Küsib ridade arvu
cols = int(input("Veergude arv: ")) # Küsib veergude arvu

print("Vali joone värv:") # Küsib kasutajalt joone värvi
print("1 - Sinine") # Sinine
print("2 - Fuksia") # Fuksia
print("3 - Tumelilla") # Tumelilla
print("4 - Pastellroosa") # Pastellroosa
choice = input("Sisesta number 1-4: ") # Küsib värvi numbrit 1-4

# Värvivalik
if choice == "1": # Kui valik on 1
    line_color = (64, 224, 208) # Sinine
elif choice == "2": # Kui valik on 2
    line_color = (255, 0, 128)  # Fuksia
elif choice == "3": # Kui valik on 3
    line_color = (75, 0, 130) # Tumelilla
else: # Kui valik on muu (4)
    line_color = (255, 209, 220) # Pastellroosa

pygame.init() # Käivitab kõik PyGame'i moodulid

screen = pygame.display.set_mode((cols * square_size, rows * square_size)) # Akna suurus vastavalt ruudu suurusele
pygame.display.set_caption("Ülesanne 3") # Määrab aknale nime
background = (255, 105, 180) # Taustavärv, roosa

def draw_grid(surface, size, r, c, color): # Funktioon ruudustiku joonistamiseks
    for row in range(r): # Käib läbi kõik read
        for col in range(c): # Käib läbi kõik veerud
            rect = pygame.Rect(col * size, row * size, size, size) # Loob ruudu õigesse asukohta
            pygame.draw.rect(surface, color, rect, 1) # Joonistab ruudu ekraanile

def main_loop(surface, size, r, c, color): # Funktsioon, mis juhib programmi peamist tsüklit
    running = True  # Muutuja, mis määrab. kas tsükkel töötab
    while running: # Peamine mängutsükkel - töötab kuni running on True
        surface.fill(background) # Värvib tausta
        draw_grid(surface, size, r, c, color) # Joonistab ruudustiku ekraanile

        pygame.display.flip() # Uuendab ekraani

        for event in pygame.event.get():  # Käib läbi kõik sündmused (nt. klikk, klahvivajutus, akna sulgemine)
            if event.type == pygame.QUIT:  # Kontrollib, kas kasutaja sulges mänguakna (X)
                running = False  # Lõpetab mängutsükli

    pygame.quit() # Sulgeb PyGame'i
    sys.exit() # Programmi lõpetamine

# Käivitab peamise tsükli ja joonistab ruudustiku ekraanile
main_loop(screen, square_size, rows, cols, line_color)