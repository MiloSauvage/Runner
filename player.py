import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.health = 100
        self.health_max = 100
        self.velocity = [0, 0]
        self.speed = 3
        self.image_origin = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image_origin, (1065 / 12, 3151 / 12))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 360
        self.scale_down = 0
        self.scale_down_max = 600
        self.scale_up = 0
        self.scale_up_max = 600
        self.ulti_power = 0
        self.ulti_power_give = 20
        self.ulti_power_max = 100
        self.scale_center = 0
        self.scale_center_max = 600
        self.xp = 0
        self.xp_max = 300
        self.xp_give = 3
        self.niveau = 0

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.image_origin, 90, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def scale_full(self):
        if self.scale_up >= self.scale_up_max:
            self.image = pygame.transform.scale(self.image_origin, (1065 / 12, 3151 / 12))
            self.rect.y = 360
        elif self.scale_down >= self.scale_down_max:
            self.image = pygame.transform.scale(self.image_origin, (1065 / 12, 3151 / 12))
            self.rect.y = 360
        elif self.scale_center >= self.scale_center_max:
            self.image = pygame.transform.scale(self.image_origin, (1065 / 12, 3151 / 12))
            self.rect.y = 360
            self.ulti_power = 0
        elif self.xp >= self.xp_max:
            if self.xp_give >= 0:
                self.niveau += 1
                print("niveau suivant " + str(self.niveau))
                self.game.level_up()
                self.xp_give -= 1
                self.xp = 0


    def ulti(self):
        if self.ulti_power <= self.ulti_power_max - self.ulti_power_give:
            self.ulti_power += self.ulti_power_give
        else:
            self.ulti_power_give = self.ulti_power_max - self.ulti_power
            self.ulti_power += self.ulti_power_give

    def life(self):
        if self.health <= 0:
            self.game.game_over()

    def update_center_bar(self, screen):
        pygame.draw.rect(screen, (60, 63, 60), [100, 670, self.scale_center_max, 8])
        pygame.draw.rect(screen, (255, 112, 112), [100, 670, self.scale_center, 8])

    def update_up_bar(self, screen):
        pygame.draw.rect(screen, (60, 63, 60), [100, 690, self.scale_up_max, 8])
        pygame.draw.rect(screen, (255, 112, 112), [100, 690, self.scale_up, 8])

    def update_down_bar(self, screen):
        pygame.draw.rect(screen, (60, 63, 60), [100, 710, self.scale_down_max, 8])
        pygame.draw.rect(screen, (0, 193, 255), [100, 710, self.scale_down, 8])

    def update_health_bar(self, screen):
        pygame.draw.rect(screen, (60, 63, 60), [self.rect.x - 13, self.rect.y - 20, self.health_max, 8])
        pygame.draw.rect(screen, (111, 206, 46), [self.rect.x - 13, self.rect.y - 20, self.health, 8])

    def update_ulti_bar(self, screen):
        pygame.draw.rect(screen, (60, 63, 60), [self.rect.x - 13, self.rect.y - 29, self.ulti_power_max, 8])
        pygame.draw.rect(screen, (254, 181, 0), [self.rect.x - 13, self.rect.y - 29, self.ulti_power, 8])

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_Level_up_bar(self, screen):
        pygame.draw.rect(screen, (60, 63, 60), [750, 670, self.xp_max, 40])
        pygame.draw.rect(screen, (255, 0, 0), [750, 670, self.xp, 40])
