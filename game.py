from pygame import* 
font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36)
#классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, heigh):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, heigh))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def rest(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_R(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if key_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += 10
    def update_L(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if key_pressed[K_s] and self.rect.y < 400:
            self.rect.y += 10
    
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.jpg'), (700, 500))
rocket_L = Player('rocket_L.png', 2, 250, 3, 10, 100)
rocket_R = Player('rocket_R.png', 688, 250, 3, 10, 100)
ball = GameSprite('ball.png', 350, 250, 2, 30, 30)
speed_x = 3
speed_y = 3
finish = False
game = True
height = 500
weight = 700
lose_L = font1.render('PALYER 1 LOSE!', True, (180, 0, 0))
lose_R = font2.render('PALYER 2 LOSE!', True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(background, (0, 0))
        if ball.rect.y > height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(rocket_L, ball) or sprite.collide_rect(rocket_R, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_L, (200, 200))
        if ball.rect.x > 670:
            finish = True
            window.blit(lose_R, (200, 200))
        rocket_L.rest()
        rocket_L.update_L()
        rocket_R.rest()
        rocket_R.update_R()
        ball.rest()
    
    
    
    display.update()
    


