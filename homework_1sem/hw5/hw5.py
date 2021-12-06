import pygame

pygame.init()

def fon():
    surface2 = pygame.Surface((800, 1100), pygame.SRCALPHA, 32)

    gora =  [(0, 595), (0, 342), (95, 107), (165, 272), (271, 146), (475, 451), (617, 140), (667, 193), (792, 41), (790, 665), (469, 666), (444, 657), (446, 599), (439, 596), (440, 577), (433, 566), (414, 562), (179, 562), (97, 575), (76, 571), (41, 578)]
    for i in range(len(gora)):
        gora[i] = tuple([gora[i][0] * alp, gora[i][1] * alp])
    pygame.draw.polygon(surface2, (179, 179, 179), gora)
    pygame.draw.polygon(surface2, (0, 0, 0), gora, 1)
    
    trava = [(790, 665), (469, 666), (444, 657), (446, 599), (439, 596), (440, 577), (433, 566), (414, 562), (179, 562), (97, 575), (76, 571), (41, 578), (0, 592), (0, 1100), (800, 1100)]
    for i in range(len(trava)):
        trava[i] = tuple([trava[i][0] * alp, trava[i][1] * alp])
    pygame.draw.polygon(surface2, (170, 222, 135), trava)
    pygame.draw.polygon(surface2, (0, 0, 0), trava, 1)
    return surface2


def full_ellipse(surface, RGB, koords):
    pygame.draw.ellipse(surface, RGB, koords, 0)
    pygame.draw.ellipse(surface, (153, 162, 148), koords, 1)


def noga(x, y, size):
    surface1 = pygame.Surface((800, 1100), pygame.SRCALPHA, 32)
    pygame.draw.ellipse(surface1, white, (x + 20 * size, y + 40 * size, 25 * size, 55 * size))
    pygame.draw.ellipse(surface1, white, (x + 20 * size, y + 90 * size, 25 * size, 55 * size))
    pygame.draw.ellipse(surface1, white, (x + 25 * size, y + 144 * size, 25 * size, 16 * size))
    return surface1
    

def lama(x, y, size):
    surface1 = pygame.Surface((800, 1100), pygame.SRCALPHA, 32)
    pygame.draw.ellipse(surface1, white, (x, y, 180 * size, 80 * size))     # TyJIoBuwe
    # Horu:
    legs_koords = [(0, 0), (35, 20), (85, -8), (120, 20)]
    for leg in legs_koords:
        surface1.blit(noga(x + leg[0]*size, y + leg[1]*size, size), (0, 0))

    pygame.draw.ellipse(surface1, white, (x + 145 * size, y - 105 * size, 40 * size, 130 * size))           # we9I
    pygame.draw.ellipse(surface1, white, (x + 150 * size, y - 128 * size, 48 * size, 30 * size))            # roJIoBa
    pygame.draw.circle(surface1, (229, 128, 255), (x + 172 * size, y - 116 * size), 9 * size)               # pagyjka
    pygame.draw.circle(surface1, (0, 0, 0), (x + 175 * size, y - 117 * size), 4 * size)                     # 3pa4ok
    # 6JIuk:
    pygame.draw.polygon(surface1, white, [(x + 172 * size, y - 122 * size), (x + 168 * size, y - 123 * size),  (x + 172 * size, y - 122 * size)], 4)
    # ywu:
    pygame.draw.polygon(surface1, white, [(x + 154 * size, y - 118 * size), (x + 154 * size, y - 112 * size), (x + 142 * size, y - 133 * size)])
    pygame.draw.polygon(surface1, white, [(x + 161 * size, y - 113 * size), (x + 164 * size, y - 122 * size), (x + 152 * size, y - 136 * size)])
    return surface1


def romashka(x, y, size):
    surface = pygame.Surface((800, 1100), pygame.SRCALPHA, 32)
    # this rect is border of ellipses:
    flower_border = pygame.Rect(x, y, 32 * size, 12 * size)
    # centre:
    pygame.draw.ellipse(surface, (255, 255, 0), flower_border)
    # JIenecTku:
    lepest_koords = [(-15, -8), (-1, -10), (12, -8), (23, 0), (15, 8), (-7, 7), (-23, 1)]
    for list in lepest_koords:
        full_ellipse(surface, white, flower_border.move(list[0] * size, list[1] * size))
    return surface


def KycT(x, y, size):
    surfaces = pygame.Surface((800, 1100), pygame.SRCALPHA, 32)
    pygame.draw.circle(surfaces, (113, 200, 55), (150, 150), 150)   # ground
    surfaces.blit(romashka(x, y, size), (150, 20))
    romashka_plases = [(30, 1, (30, -350)), (-20, 1.2, (-240, 60)), (-15, 1, (-250, 90)), (-8, 1, (60, 150)), (8, 0.8, (130, 20))]
    for flower in romashka_plases:
        surfacewrong = pygame.transform.rotozoom(romashka(x, y, size), flower[0], flower[1])
        surfaces.blit(surfacewrong, flower[2])
    return surfaces
    
white = (255, 255, 255)
FPS = 30
alp = 0.5
screen = pygame.display.set_mode((int(790 * alp), int(1100 * alp)))
screen.fill ([175, 221, 233])


def main():
    surface2 = fon()

    KycTbl_koords = [(0.1, (0, 280)), (0.18, (360, 310)), (0.1, (260, 330)), (0.22, (320, 410)), (0.1, (330, 520)), (0.22, (240, 480))]
    for KycTbl in KycTbl_koords:
        surface2.blit(pygame.transform.rotozoom(KycT(25, 25, 1), 0, KycTbl[0]), KycTbl[1])

    # MaJIeHbka9I B cepeguHe:
    surface2.blit(pygame.transform.rotozoom(lama(0, 140, 1), 0, 0.3), (140, 220))
    # MaJIeHbka9I JIeBa9I:
    surface2.blit(pygame.transform.rotozoom(lama(0, 140, 1), 0, 0.3), (70, 300))
    # MaJIeHbka9I npaBa9I nepeBepHyTa:
    surface2.blit(pygame.transform.rotozoom(pygame.transform.flip(lama(0, 140, 1), True, False), 0, 0.3), (20, 340))
    # caMa9I 6oJIwa9I:
    surface2.blit(pygame.transform.rotozoom(lama(25, 300, 2), 0, 1), (-300, 360))
    # 6oJIbwa9I cnpaBa nepeBepHyTa:
    surface2.blit(pygame.transform.rotozoom(pygame.transform.flip(lama(15, 200, 1), True, False), 0, 0.8), (-140, 260))
    # finally:
    screen.blit(surface2, (0, 0))
    return screen

# Pagu 4ero Mbl npogeJIaJIu eToT nyTb:
print('ABOBA')
main()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
