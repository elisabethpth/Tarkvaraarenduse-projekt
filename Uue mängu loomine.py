# --- UUE MÄNGU LOOMINE ---

import pygame # Impordib PyGame'i mooduli
import random # Impordib Random mooduli

pygame.init() # Käivitab PyGame'i mooduli

# --- MÄNGU TAUSTAPILT ---
space = pygame.image.load("space.png") # Faili path
space = pygame.transform.smoothscale(space, (800, 600)) # Faili suurus

# --- FUNKTSIOON | RANDOM VÄRVI KUVAMISEKS ---
def random_color():
    return (random.randint(50, 255), # R
            random.randint(50, 255), # G
            random.randint(50, 255)) # B
# Tagastab tuple'i kujul (R, G, B) juhuslike täisarvudena
# Vahemik 50 - 255, et vältida liiga tumedaid värve

# --- EKRAANI SEADED ---
screenx, screeny = 800, 600 # Mänguakna mõõdud (laius ja kõrgus)
screen = pygame.display.set_mode((screenx, screeny)) # Loob akna
pygame.display.set_caption("Uue mängu loomine") # Pealkiri mänguaknale

# --- MÄNGU SEADED ---
clock = pygame.time.Clock() # Kell FPS-i kontrollimiseks
circles = []  # List loodud ringide jaoks
max_circles = 10 # Maksimum 10 ringi

# MÄNGU PÕHITSÜKKEL
running = True # Tsükkel töötab
while running: # Kuniks tsükkel töötab:
    screen.blit(space, (0,0)) # Kuvab taustapildi

    for event in pygame.event.get(): # Käib läbi mängu kõik sündmused
        if event.type == pygame.QUIT: # Kui kasutaja vajutab (X)
            running = False # Lõpetab mängutsükli
        if event.type == pygame.MOUSEBUTTONDOWN: # Kui kasutaja vajutab hiireklahvi
            x, y = event.pos # Salvestab hiire kursori x- ja y- koordinaadid

        # RINGI (RAADIUSE) SUURENDAMINE
            for i in range(len(circles)): # Käib läbi kõik ringid
                cx, cy, r, col, bonus = circles[i] # Võtab ringi kõik andmed
                if bonus: # Kui on boonusring
                    r += 10  # Ring kasvab kiiremini
                else: # Kui on tavaline ring
                    r += 5 # Ring kasvab aeglasemalt

            # Salvestab uuendatud ringi tagasi listi
                circles[i] = (cx, cy, r, col, bonus)

        # 15% TÕENÄOSUS, ET TEKIB BOONUSRING
            is_bonus = random.random() < 0.15
        # BOONUSRINGI VÄRV - KULDNE | TAVALINE RING - JUHUSLIK VÄRV
            color = (245, 189, 2) if is_bonus else random_color()

            circles.append((x, y, 10, color, is_bonus)) # Lisab uue ringi listi
            if len(circles) > max_circles: # Kui ringe on listis rohkem kui 10
                circles.pop(0) # Kustutab kõige vanema (esimesena) lisatud ringi

# RINGIDE JOONISTAMINE
    for x, y, r, color, bonus in circles:
        pygame.draw.circle(screen, color, (x, y), r)

# ÄÄRE JOONISTAMINE BOONUSRINGILE
        if bonus: # Kui on boonusring, kuvab ringile ääre
            pygame.draw.circle(screen, (0, 0, 0), (x, y), r, 3)

    pygame.display.flip() # Uuendab ekraani
    clock.tick(60) # Piirab tsükli kiiruse

pygame.quit() # Sulgeb PyGame'i
quit () # Lõpetab programmi