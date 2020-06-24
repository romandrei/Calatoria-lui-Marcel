import pygame, random
pygame.init()

frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption("Calatoria lui Marcel")

marcelpng = pygame.image.load("Img/marcel.png")
inamicpng = pygame.image.load("Img/inamic.png")
glontpng = pygame.image.load("Img/glont.png")
pygame.mixer.music.load("Aud/melodie.mp3")
pygame.mixer.music.play(-1)

ceas = pygame.time.Clock()

lungime_latura = 32
scor = 0
marcel_viu = True
inamic_vit = 1

font = pygame.font.SysFont("arial", 16)

def scor_text():
    text = font.render("Scor:" + str(scor), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (50, 50)
    frstr.blit(text, textRect)

class marcel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(marcelpng, (lungime_latura, lungime_latura))
        self.rect = self.image.get_rect()
        self.rect.x = 400 - lungime_latura
        self.rect.y = 700
        self.vit = 2
    def update(self):
        self.taste = pygame.key.get_pressed()
        if self.taste[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.vit
        if self.taste[pygame.K_DOWN] and self.rect.y < 800 - lungime_latura:
            self.rect.y += self.vit
        if self.taste[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.vit
        if self.taste[pygame.K_RIGHT] and self.rect.x < 800 - lungime_latura:
            self.rect.x += self.vit

class inamic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(inamicpng, (lungime_latura, lungime_latura))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800 - lungime_latura)
        self.rect.y = random.randrange(0 - lungime_latura, 0 - lungime_latura * 4, -1)
        self.vit = inamic_vit
    def update(self):
        self.rect.y += self.vit
        if self.rect.y > 800 + lungime_latura:
            self.rect.x = random.randrange(0, 800 - lungime_latura)
            self.rect.y = 0 - lungime_latura


class glont(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(glontpng, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.x = mrc.rect.x
        self.rect.y = mrc.rect.y
        self.vit = 6
    def update(self):
        self.rect.y -= self.vit
        if self.rect.y < 0 - 16:
            self.kill()

toate = pygame.sprite.Group()
inamici = pygame.sprite.Group()
jucatori = pygame.sprite.Group()
gloante = pygame.sprite.Group()
mrc = marcel()
toate.add(mrc)
jucatori.add(mrc)

for i in range(30):
    inm = inamic()
    toate.add(inm)
    inamici.add(inm)

rulare = True
while rulare:
    ceas.tick(120)
    frstr.fill((0, 0, 0))
    taste = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or taste[pygame.K_ESCAPE]:
            rulare = False
        elif taste[pygame.K_F4]:
            frstr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        elif taste[pygame.K_F3]:
            frstr = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
        elif taste[pygame.K_SPACE] and marcel_viu:
            glt = glont()
            toate.add(glt)
            gloante.add(glt)

    lovit = pygame.sprite.groupcollide(jucatori, inamici, True, False)
    lovit_glont = pygame.sprite.groupcollide(gloante, inamici, False, True)

    if lovit:
        marcel_viu = False

    if lovit_glont:
        scor += 1
        inamic_vit += 0.1
        inm = inamic()
        toate.add(inm)
        inamici.add(inm)
    
    toate.update()
    toate.draw(frstr)
    scor_text()
    pygame.display.flip()

pygame.quit()
