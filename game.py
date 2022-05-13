from pygame import *
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
    def update_L(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if key_pressed[K_DOWN] and self.rect.y < 600:
            self.rect.y += 10
    def update_R(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_W] and self.rect.y > 0:
            self.rect.y -= 10
        if key_pressed[K_S] and self.rect.y < 600:
            self.rect.y += 10
    
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('background.jpg'), (700, 500))
rocket_L = Player('rocket_L.png', 2, 250, 3, 10, 100)

game = True
while game:
    window.blit(background, (0, 0))
    rocket_L.rest()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()



