#! /usr/bin/python3

# chrome dino game
# pygame

import pygame
import sys
import os
import random

frame_size_x = 1200
frame_size_y = 630

dynamic_area_x = 800
dynamic_area_y = 400

# colors
white = pygame.Color(248, 248, 242)
black = pygame.Color(40, 42, 54)
grey = pygame.Color(68, 78, 90, 10)
yellow = pygame.Color(241, 250, 140)
pink = pygame.Color(255, 121, 198)
greeen = pygame.Color(80, 250, 123)
orange = pygame.Color(255, 184, 108)

# for gameplay
first_game = False
status = "RUN"
total_distance = 0
total_score = 0
speed = 0
High_score = 0
m = 1000
z = 0


# gamearea inside the game_window
class DynamicArea:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


class DinoArea:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


class TrackArea:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


class SkyArea:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


class ScoreArea:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


# initialize the game window
pygame.display.set_caption("chrome://dino")
game_window = pygame.display.set_mode([frame_size_x, frame_size_y])

# objects
rect = DynamicArea(200, 100, 800, 400, grey)
dino = DinoArea(250, 330, 100, 100, orange)
track = TrackArea(200, 400, 800, 100, greeen)
sky = SkyArea(200, 250, 800, 100, yellow)
score = ScoreArea(700, 200, 200, 100, black)

fps_controller = pygame.time.Clock()

game_window.fill(white)

# cactus images
cactusSmall1_img = pygame.image.load(os.path.join('asset/Cactus',
                                                  'SmallCactus1.png'))
cactusSmall2_img = pygame.image.load(os.path.join('asset/Cactus',
                                                  'SmallCactus2.png'))
cactusSmall3_img = pygame.image.load(os.path.join('asset/Cactus',
                                                  'SmallCactus3.png'))

cactusLarge1_img = pygame.image.load(os.path.join('asset/Cactus',
                                                  'LargeCactus1.png'))
cactusLarge2_img = pygame.image.load(os.path.join('asset/Cactus',
                                                  'LargeCactus2.png'))
cactusLarge3_img = pygame.image.load(os.path.join('asset/Cactus',
                                                  'LargeCactus3.png'))

# Bird images
bird1_img = pygame.image.load(os.path.join('asset/Birds', 'Bird1.png'))
bird2_img = pygame.image.load(os.path.join('asset/Birds', 'Bird2.png'))

# dino images
dinoStart_img = pygame.image.load(os.path.join('asset/Dino', 'DinoStart.png'))
dinoJump_img = pygame.image.load(os.path.join('asset/Dino', 'DinoJump.png'))
dinoRun1_img = pygame.image.load(os.path.join('asset/Dino', 'DinoRun1.png'))
dinoRun2_img = pygame.image.load(os.path.join('asset/Dino', 'DinoRun2.png'))
dinoDead_img = pygame.image.load(os.path.join('asset/Dino', 'DinoDead.png'))
dinoDuck1_img = pygame.image.load(os.path.join('asset/Dino', 'DinoDuck1.png'))
dinoDuck2_img = pygame.image.load(os.path.join('asset/Dino', 'DinoDuck2.png'))

# dino start image
game_window.blit(dinoStart_img, (dino.x, dino.y, dino.width, dino.height))

# track images
track_img = pygame.image.load(os.path.join('asset/Others', 'Track.png'))

# sky images
sky_img = pygame.image.load(os.path.join('asset/Others', 'Cloud.png'))
game_window.blit(sky_img, (sky.x, sky.y, sky.width, sky.height))

# restart and gameover image
restart_img = pygame.image.load(os.path.join('asset/Others', 'Reset.png'))
game_over_img = pygame.image.load(os.path.join('asset/Others', 'GameOver.png'))

dino_frames = [dinoRun1_img, dinoRun2_img]
current_frame = 0
dino_duck_frames = [dinoDuck1_img, dinoDuck2_img]
cactus_frames = [cactusLarge1_img, cactusLarge2_img, cactusLarge3_img,
                 cactusSmall1_img, cactusSmall2_img, cactusSmall3_img]

birds_frames = [bird1_img, bird2_img]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_UP or event.key == ord("w"):
                status = "JUMP"
            elif event.key == pygame.K_DOWN or event.key == ord("s"):
                status = "DUCK"

    game_window.fill(white)
    if status == "JUMP":
        game_window.blit(dinoJump_img,
                         (dino.x, dino.y-100, dino.width, dino.height))
        pygame.time.delay(150)
        status = "RUN"

    elif status == "RUN":
        current_frame = (current_frame + 1) % len(dino_frames)
        game_window.blit(dino_frames[current_frame],
                         (dino.x, dino.y, dino.width, dino.height))
        pygame.time.delay(150)

    elif status == "DUCK":
        current_frame = (current_frame + 1) % len(dino_frames)
        game_window.blit(dino_duck_frames[current_frame],
                         (dino.x, dino.y+30, dino.width, dino.height))
        pygame.time.delay(150)
        status = "RUN"

    game_window.blit(track_img, (track.x - total_distance,
                                 track.y, track.width, track.height))
    game_window.blit(sky_img, (sky.x, sky.y, sky.width, sky.height))

    if not first_game:
        keys = pygame.key.get_pressed()
        if any(keys):
            first_game = True

    # to move the sky and track
    if first_game:
        sky.x -= 2
        track.x -= 5
        total_distance += 1
        if track.x <= -1300:
            track.x = 0
            total_distance = 0
        if sky.x == -70:
            sky.x = 1200

    # to randomily generate cactus
    # Get the dimensions of the image
    image_rect = cactus_frames[z].get_rect()
    cactus_width = image_rect.width
    cactus_height = image_rect.height
    game_window.blit(cactus_frames[z], (m, dino.y, dino.width, dino.height))

    dino_rect = pygame.Rect(dino.x, dino.y, dino.width, dino.height)
    cactus_rect = pygame.Rect(m, dino.y, cactus_width, cactus_height)

    game_window.blit(game_over_img, (score.x, score.y, score.width, score.height))

    if dino_rect.colliderect(cactus_rect):
        # Handle the collision, for example:
        game_over = True
        print('gameover')
        keys = pygame.key.get_pressed()
#        game_window.blit(game_over, (score.x, score.y, score.width, score.height, 1))
#        game_window.blit(restart_img, (score.x, score.y+50, score.width, score.height, 1))
        if any(keys):
            if High_score < total_score:
                High_score = total_score
                total_score = 0
                first_game = False
            else:
                total_score = 0
                first_game = False

    m -= 5
    if m == 0:
        m = 1000
        z = random.randrange(1, len(cactus_frames))

   # current_frame = (current_frame + 1) % len(birds_frames)
   # game_window.blit(birds_frames[current_frame],
    #                     (2000, dino.y+30, dino.width, dino.height))
   # pygame.time.delay(150)

    total_score += (1 + (total_score % 100))
    total_score = total_score % 100
    pygame.display.update()
    fps_controller.tick(30 + speed)
