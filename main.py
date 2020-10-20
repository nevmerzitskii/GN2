import pygame
import random

num = random.randint(0, 100)
print(num)

W = 480
H = 360
SILVER = (192, 192, 192)
BLACK = (0, 0, 0,)
numeral = ''
move = 1
block = 0
start = 1
OUTSIZE_BG = (0, -100)

pygame.init()
pygame.display.set_caption('Угадай число')
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((W, H))

bg = pygame.image.load('image/room.png')
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load('image/cat.png')
cat_rect = cat.get_rect(center=(70, 220))
dog = pygame.image.load('image/dog.png')
dog_rect = dog.get_rect(center=(410, 220))
owl = pygame.image.load('image/owl.png')
owl_rect = owl.get_rect(center=(210, 120))
dialog = pygame.image.load('image/dialog.png')
dialog_rect = dialog.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_owl_pos = (owl_rect.x, owl_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w// 2, dog_rect.y - dialog_rect.h)

font = pygame.font.SysFont('Arial', 28, True, False)
font2 = pygame.font.SysFont('Arial', 14, True, False)
font_box = pygame.Surface((W - 30, font.get_height()))
font_box_rect = font_box.get_rect(center=(W // 2, H - 30))


def dialogs(text, pos, owl_text)
    screen.blit(dialog, pos)
    screen.blit(font2.render(text. True, BLACK), (pos[0] + 5, pos[1] + 5))
    screen.blit(dialog_owl_pos)
    screen.blit(font2.render(owl_text, True, BLACK), (dialog_owl_pos[0] + 5, dialog_owl_pos[1] + 5))
    pygame.display.update()
    pygame.time.wait(2000)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
               run = False


    if block == 0:
        screen.blit(bg, bg_rect)
        screen.blit(cat, cat_rect)
        screen.blit(dog, dog_rect)
        screen.blit(owl, owl_rect)
        screen.blit(font_box, font_box_rect)
    font_box.fill(SILVER)
