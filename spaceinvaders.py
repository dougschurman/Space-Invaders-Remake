import pygame
import random
import time

pygame.mixer.init()
pygame.init()

clock = pygame.time.Clock()
display_width = 736
display_height = 720

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Shooter')
clock = pygame.time.Clock()
ship_width = 28
ship_height = 40
stars = pygame.image.load('stars.png')
icon = pygame.image.load('shipicon.png')
pygame.display.set_icon(icon)

lasersound = pygame.mixer.Sound('lasersound.wav')
movesound1 = pygame.mixer.Sound('fastinvader1.wav')
killsound = pygame.mixer.Sound('invaderkilled.wav')


class spaceship(pygame.sprite.Sprite):
    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()
        self.speed = 6
        self.rect.x = startx
        self.rect.y = starty

    def move_right(self):
        if self.rect.x < 704:
            self.rect.x += self.speed

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed


class laser(pygame.sprite.Sprite):
    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('laser.png')
        self.rect = self.image.get_rect()
        self.speed = 10
        self.rect.x = startx
        self.rect.y = starty

    def update(self):
        self.rect.y -= self.speed


class level1alien(pygame.sprite.Sprite):
    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('level1alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = starty
        self.points = 100

    def update(self, direct):
        if direct == 'right':
            self.rect.x += 1
        elif direct == 'left':
            self.rect.x -= 1
        else:
            self.rect.y += 36


class level2alien(pygame.sprite.Sprite):
    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('level2alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = starty
        self.points = 200

    def update(self, direct):
        if direct == 'right':
            self.rect.x += 1
        elif direct == 'left':
            self.rect.x -= 1
        else:
            self.rect.y += 36


class level3alien(pygame.sprite.Sprite):
    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('level3alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = starty
        self.points = 400

    def update(self, direct):
        if direct == 'right':
            self.rect.x += 1
        elif direct == 'left':
            self.rect.x -= 1
        else:
            self.rect.y += 36


class level4alien(pygame.sprite.Sprite):
    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('level4alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = startx
        self.rect.y = starty
        self.points = 700

    def update(self, direct):
        if direct == 'right':
            self.rect.x += 1
        elif direct == 'left':
            self.rect.x -= 1
        else:
            self.rect.y += 36


def moving_alien(aliens, flip):
    for i in aliens:
        if flip == 0:
            if i.rect.x <= 696:
                aliens.update('right')
            else:
                aliens.update(2)
                flip = 1
        if flip == 1:
            if i.rect.x >= 0:
                aliens.update('left')
            else:
                aliens.update(2)
                flip = 0
    return flip


def check_collide(group1, group2):
    collisions = pygame.sprite.groupcollide(group1, group2, True, True)


def game_loop():
    x = 382
    y = 660
    ship = spaceship(x, y)
    ships = pygame.sprite.Group()
    ships.add(ship)
    lasers = pygame.sprite.Group()
    levelones = pygame.sprite.Group()
    leveltwos = pygame.sprite.Group()
    levelthrees = pygame.sprite.Group()
    levelfours = pygame.sprite.Group()
    allones = [level1alien(0, 200), level1alien(46, 200), level1alien(92, 200), level1alien(
        138, 200), level1alien(184, 200), level1alien(230, 200), level1alien(276, 200), level1alien(322, 200), level1alien(368, 200), level1alien(414, 200)]
    alltwos = [level2alien(0, 154), level2alien(46, 154), level2alien(92, 154), level2alien(
        138, 154), level2alien(184, 154), level2alien(230, 154), level2alien(276, 154), level2alien(322, 154), level2alien(368, 154), level2alien(414, 154)]
    allthrees = [level3alien(0, 108), level3alien(46, 108), level3alien(92, 108), level3alien(138, 108), level3alien(184, 108),
                 level3alien(230, 108), level3alien(276, 108), level3alien(322, 108), level3alien(368, 108), level3alien(414, 108)]
    allfours = [level4alien(0, 62), level4alien(46, 62), level4alien(92, 62), level4alien(138, 62), level4alien(184, 62),
                level4alien(230, 62), level4alien(276, 62), level4alien(322, 62), level4alien(368, 62), level4alien(414, 62)]
    levelones.add(allones)
    leveltwos.add(alltwos)
    levelthrees.add(allthrees)
    levelfours.add(allfours)
    laser_time = 800
    alien_time = 400
    flipper = 0

    while True:
        dt = clock.tick(60)
        laser_time += dt
        alien_time += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ship.move_left()
        if keys[pygame.K_RIGHT]:
            ship.move_right()
        if laser_time > 800:
            if keys[pygame.K_SPACE]:
                lasersound.play()
                lasers.add(laser(ship.rect.x + 14, ship.rect.y - 10))
                laser_time = 0
                lasersound.play()

        game_display.blit(stars, (0, 0))
        lasers.draw(game_display)
        ships.draw(game_display)
        levelones.draw(game_display)
        leveltwos.draw(game_display)
        levelthrees.draw(game_display)
        levelfours.draw(game_display)
        lasers.update()
        if alien_time > 600:
            movesound1.play()
            moving_alien(levelones, flipper)
            moving_alien(leveltwos, flipper)
            moving_alien(levelthrees, flipper)
            flipper = moving_alien(levelfours, flipper)

            alien_time = 0

        check_collide(lasers, levelones)
        check_collide(lasers, leveltwos)
        check_collide(lasers, levelthrees)
        check_collide(lasers, levelfours)

        pygame.display.flip()


game_loop()
pygame.quit()
quit()
