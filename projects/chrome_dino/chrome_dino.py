#! /usr/bin/python3

# chrome dino game
# pygame

import pygame
import os
import random


gamewindow_y = 600
gamewindow_x = 1100
gamewindow = pygame.display.set_mode([gamewindow_x, gamewindow_y])

# cactus images
cactusSmall = [pygame.image.load(os.path.join('asset/Cactus','SmallCactus1.png')),
               pygame.image.load(os.path.join('asset/Cactus','SmallCactus2.png')),
               pygame.image.load(os.path.join('asset/Cactus','SmallCactus3.png'))]

cactusLarge = [pygame.image.load(os.path.join('asset/Cactus','LargeCactus1.png')),
               pygame.image.load(os.path.join('asset/Cactus','LargeCactus2.png')),
               pygame.image.load(os.path.join('asset/Cactus','LargeCactus3.png'))]

# Bird images
birds = [pygame.image.load(os.path.join('asset/Birds', 'Bird1.png')),
         pygame.image.load(os.path.join('asset/Birds', 'Bird2.png'))]

# dino images
dinoStart = pygame.image.load(os.path.join('asset/Dino', 'DinoStart.png'))
dinoJump = pygame.image.load(os.path.join('asset/Dino', 'DinoJump.png'))

dinoRun = [pygame.image.load(os.path.join('asset/Dino', 'DinoRun1.png')),
           pygame.image.load(os.path.join('asset/Dino', 'DinoRun2.png'))]

dinoDead = pygame.image.load(os.path.join('asset/Dino', 'DinoDead.png'))

dinoDuck = [pygame.image.load(os.path.join('asset/Dino', 'DinoDuck1.png')),
            pygame.image.load(os.path.join('asset/Dino', 'DinoDuck2.png'))]

# track images
track = pygame.image.load(os.path.join('asset/Others', 'Track.png'))

# sky images
sky = pygame.image.load(os.path.join('asset/Others', 'Cloud.png'))

# restart and gameover image
restart = pygame.image.load(os.path.join('asset/Others', 'Reset.png'))
game_over = pygame.image.load(os.path.join('asset/Others', 'GameOver.png'))


class Dino:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5              # velocity of dino

    def __init__(self):
        self.duck_img = dinoDuck
        self.run_img = dinoRun
        self.jump_img = dinoJump

        self.dino_duck = False
        self.dino_jump = False
        self.dino_run = True

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, gamewindow):
        gamewindow.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstracles
    run = True
    clock = pygame.time.Clock()
    player = Dino()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        gamewindow.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(gamewindow)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


main()
