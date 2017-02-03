# importing modules
import pygame
from pygame.locals import *
from copter import Copter


def font_render(font, text):
    return font.render(text, True, (0, 0, 0))

copter = Copter('QuadCop', 4)
Rotors = copter.get_propellers()

# initializing variables
pygame.init()
screen = pygame.display.set_mode((1000, 650), 0, 24)
screen.fill((255, 255, 255))
pygame.display.set_caption("Motor Key Press Test")
titleFont = pygame.font.SysFont("Copperplate Gothic", 20)
titleFont.set_bold(1)
descriptionFont = pygame.font.SysFont("Copperplate Gothic", 20)

motor1_titles = ["Left Motor", "Top Motor", "Right Motor", "Bottom Motor"]
y = 20
for title in motor1_titles:
    titleFont.set_underline(1)
    screen.blit(font_render(titleFont, title), (y, 20))
    y += 200

arrowSubSurface = screen.subsurface(pygame.Rect(0, 100, 900, 350))
pygame.key.set_repeat(500, 30)
# main loop which displays the pressed keys on the screen
going = True
accelerate = True
keys = copter.get_keys()

while going:
    events = pygame.event.get()
    for e in events:
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                going = False
            elif e.key == K_a:
                accelerate = False
            elif e.key == K_s:
                accelerate = True
            elif e.key == K_r:
                copter.reset_acceleration()
            elif e.key == K_UP:
                copter.change_propeller_rotation_speed(0, accelerate)
            elif e.key == K_DOWN:
                copter.change_propeller_rotation_speed(1, accelerate)
            elif e.key == K_LEFT:
                copter.change_propeller_rotation_speed(2, accelerate)
            elif e.key == K_RIGHT:
                copter.change_propeller_rotation_speed(3, accelerate)
            elif e.key == K_LCTRL:
                copter.gain_altitude()
            elif e.key == K_LALT:
                copter.decline_altitude()

            arrowSubSurface.fill((255, 255, 255))
            x = 20
            for key in keys.keys():
                renderedText = font_render(titleFont, keys[key])
                arrowSubSurface.blit(renderedText, (x, 20))
                x += 200
        elif e.type == QUIT:
            going = False

        pygame.display.update()
