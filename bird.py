import pygame
import random


class Bird(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.speed = random.randint(1, 3)
        self.attack = 20
        self.image = pygame.image.load("bird.png")
        self.image = pygame.transform.scale(self.image, (960 / 12, 570 / 12))
        self.rect = self.image.get_rect()
        self.rect.x = 1200 + random.randint(0, 300)
        self.rect.y = 370

    def damage(self):
        self.game.player.health -= self.attack
        self.rect.x = 1200 + random.randint(0, 300)
        self.speed = random.randint(1, 4)
        self.game.player.ulti()

    def sortie(self):
        if self.rect.x < 0:
            self.rect.x = 1200 + random.randint(0, 300)
            self.speed = random.randint(1, 4)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.speed
            self.sortie()
        else:
            self.damage()


