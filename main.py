import pygame
from game import Game

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Runner Game")

background = pygame.image.load("bg.jpg")
background = pygame.transform.scale(background, (1080, 720))

play_button = pygame.image.load("button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = 350
play_button_rect.y = 300


game = Game()

running = True

while running:

    screen.blit(background, (0, 0))
    screen.blit(play_button, play_button_rect)

    if game.is_playing == True:
        game.run()
    else:
        screen.blit(play_button, play_button_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

pygame.init()


