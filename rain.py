import sys
import pygame
import random
import time
from pygame.sprite import Group
from pygame.sprite import Sprite

class Drop(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('drop1.png')
        self.rect = self.image.get_rect()
        self.y = float (self.rect.y)
        self.rect.top = 0
        self.rect.x = random.randrange(-30, 400, 60)

    def update (self):
        self.y += 1
        self.rect.y = self.y

def create_drops (drops, screen):
    new_drop = Drop (screen)
    if all(new_drop.rect.bottom <= drop.rect.top for drop in drops):
        drops.add (new_drop)
    for drop in drops.copy():
        if drop.rect.top >= 300:
            drops.remove (drop)



def raining ():
    pygame.init()
    screen = pygame.display.set_mode ((400,300))
    pygame.display.set_caption("Rain")
    drops = Group()
    drop = Drop (screen)
    drops.add (drop)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill ((52, 181, 215))
        create_drops (drops, screen)
        drops.draw(screen)
        drops.update()
        pygame.display.flip()
raining ()
