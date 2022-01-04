import pygame
import random


class Medkit(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.health_give = 0
        self.game = game
        self.speed = 1
        self.health = 40
        self.image = pygame.image.load("medkit.png")
        self.image = pygame.transform.scale(self.image, (960 / 12, 570 / 12))
        self.rect = self.image.get_rect()
        self.rect.x = 1500 + random.randint(0, 1000)
        self.rect.y = 370 + random.randint(0, 200)

    def use(self):
        if self.game.player.health <= 60:
            self.game.player.health += self.health

        else:
            self.health_give = self.game.player.health_max - self.game.player.health
            self.game.player.health += self.health_give


    def sortie(self):
        if self.rect.x < 0:
            self.rect.x = 1200 + random.randint(0, 300)
            self.speed = 1

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.speed
            self.sortie()
        else:
            self.rect.x = 1200 + random.randint(0, 300)
            self.rect.y = 370 + random.randint(0, 200)
            self.use()
