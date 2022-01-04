import pygame
from player import Player
from bird import Bird
from turtle import Turtle
from medkit import Medkit


screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Runner Game")


class Game:
    def __init__(self):
        self.is_playing = False
        self.medkit = Medkit(self)
        self.all_medkits = pygame.sprite.Group()
        self.turtle = Turtle(self)
        self.all_turtles = pygame.sprite.Group()
        self.player = Player(self)
        self.bird = Bird(self)
        self.all_birds = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.screen = screen
        self.background = pygame.image.load("bg.jpg")
        self.background = pygame.transform.scale(self.background, (1080, 720))
        self.clock = pygame.time.Clock()
        self.spawn_bird()
        self.spawn_turtle()
        self.spawn_medkit()

    def reset(self):
        self.all_players = pygame.sprite.Group()
        self.all_birds = pygame.sprite.Group()
        self.all_turtles = pygame.sprite.Group()
        self.all_medkits = pygame .sprite.Group()

    def game_over(self):
        self.is_playing = False

    def start(self):
        self.is_playing = True
        self.player.health = self.player.health_max

    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d] and self.player.rect.x <= 990:
            self.player.velocity[0] = 1
        elif pressed[pygame.K_q] and self.player.rect.x >= 0:
            self.player.velocity[0] = -1
        else:
            self.player.velocity[0] = 0

        if pressed[pygame.K_s]:
            self.player.image = pygame.transform.scale(self.player.image_origin, (1065 / 20, 3151 / 20))
            self.player.rect.y = 470
            if self.player.scale_down <= self.player.scale_down_max:
                self.player.scale_down += 3
            if self.player.scale_down >= self.player.scale_down_max:
                self.player.scale_full()

        elif pressed[pygame.K_z]:
            self.player.image = pygame.transform.scale(self.player.image_origin, (1065 / 20, 3151 / 20))
            self.player.rect.y = 360
            if self.player.scale_up <= self.player.scale_up_max:
                self.player.scale_up += 3
            if self.player.scale_up >= self.player.scale_up_max:
                self.player.scale_full()
        elif pressed[pygame.K_e]:
            if self.player.ulti_power >= self.player.ulti_power_max:
                self.player.image = pygame.transform.scale(self.player.image_origin, (1065 / 20, 3151 / 23))
                self.player.rect.y = 430
                if self.player.scale_center <= self.player.scale_center_max:
                    self.player.scale_center += 2
                if self.player.scale_center >= self.player.scale_center_max:
                    self.player.scale_full()
        else:
            self.player.image = pygame.transform.scale(self.player.image_origin, (1065 / 12, 3151 / 12))
            self.player.rect.y = 360
            self.player.scale_up = 0
            self.player.scale_down = 0
            self.player.scale_center = 0

        if pressed[pygame.K_SPACE]:
            self.player.xp += self.player.xp_give
            self.player.scale_full()
        else:
            self.player.xp = 0

    def update(self):
        if self.is_playing == False :
            self.reset()
        self.player.move()
        self.player.life()
        for bird in self.all_birds:
            bird.forward()
        for turtle in self.all_turtles:
            turtle.forward()
        for medkit in self.all_medkits:
            medkit.forward()

    def display(self):
        screen.blit(self.background, (0, 0))
        self.all_players.draw(screen)
        self.player.update_health_bar(screen)
        self.player.update_down_bar(screen)
        self.player.update_up_bar(screen)
        self.player.update_ulti_bar(screen)
        self.player.update_center_bar(screen)
        self.player.update_Level_up_bar(screen)
        self.all_birds.draw(screen)
        self.all_turtles.draw(screen)
        self.all_medkits.draw(screen)
        #print(len(self.all_birds))

        pygame.display.flip()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_bird(self):
        self.all_birds.add(Bird(self))

    def spawn_turtle(self):
        self.all_turtles.add(Turtle(self))

    def spawn_medkit(self):
        self.all_medkits.add(Medkit(self))

    def level_up(self):
        self.spawn_bird()
        self.spawn_turtle()
        self.spawn_medkit()


    def run(self):
        self.handling_event()
        self.update()
        self.display()
        self.clock.tick(120)
