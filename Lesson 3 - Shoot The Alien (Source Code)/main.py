import pgzrun
from random import randint

TITLE = "Shoot The Alien"
WIDTH = 800
HEIGHT = 600

message = ""

alien = Actor("alien")


def draw():
    screen.clear()
    screen.fill(color=(128, 0, 0))
    alien.draw()
    screen.draw.text(message, center=(400, 40), fontsize=60)


def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)


def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot!"
        place_alien()
    else:
        message = "You missed!"


place_alien()
pgzrun.go()
