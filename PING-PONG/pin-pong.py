#Імпорти
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

#window
background = (200,235,200)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

run = True
finish = False
clock = time.Clock()
FPS = 60


#GameSprite + класи
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

#Об'єкти
racket1 = Player('racket.png', 30, 200, 4, 20, 150)
racket2 = Player('racket.png', 520, 200, 4, 20, 150)


ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 25)

lose1 = font.render('Player 1 LOSE', True, (225,0,0))
lose2 = font.render('Player 2 LOSE', True, (225,0,0))

speed_x = 4
speed_y = 4


#Ігровий цикл
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    if not finish:
        window.blit(background,(0, 0    ))

        racket1.update()
        racket2.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_x *= 1


        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1


        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True


        racket1.reset()
        racket2.reset()

        ball.reset()

    














    display.update()
    clock.tick(FPS)





