# importing modules
from collections import OrderedDict

import pygame
from pygame.locals import *
from motor import motor
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

arrowSubSurface = screen.subsurface(pygame.Rect(0, 100, 800, 350))

upArrowCounter = 0
downArrowCounter = 0
leftArrowCounter = 0
rightArrowCounter = 0

pygame.key.set_repeat(500, 30)
# main loop which displays the pressed keys on the screen
going = True
increase = True
counter = 0

keys = OrderedDict([('Left', ''), ('Up', ''), ('Right', ''), ('Down', '')])

while going:
    events = pygame.event.get()
    for e in events:
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                going = False
            elif e.key == K_a:
                increase = False
            elif e.key == K_s:
                increase = True
            elif e.key == K_UP and increase:
                upArrowCounter += 1
                keys['Up'] = "Top........ %s" % upArrowCounter
                Rotors[0].increaseW()
            elif e.key == K_UP and not increase:
                upArrowCounter -= 1
                keys['Up'] = "Top........ %s" % upArrowCounter
                Rotors[0].decreaseW()
            elif e.key == K_DOWN and increase:
                downArrowCounter += 1
                keys['Down'] = "Down........ %s" % downArrowCounter
                Rotors[1].increaseW()
            elif e.key == K_DOWN and not increase:
                downArrowCounter -= 1
                keys['Down'] = "Down........ %s" % downArrowCounter
                Rotors[1].decreaseW()
            elif e.key == K_LEFT and increase:
                leftArrowCounter += 1
                keys['Left'] = "Left........ %s" % leftArrowCounter
                Rotors[2].increaseW()
            elif e.key == K_LEFT and not increase:
                leftArrowCounter -= 1
                keys['Left'] = "Left........ %s" % leftArrowCounter
                Rotors[2].decreaseW()
            elif e.key == K_RIGHT and increase:
                rightArrowCounter += 1
                keys['Right'] = "Right........ %s" % rightArrowCounter
                Rotors[3].increaseW()
            elif e.key == K_RIGHT and not increase:
                rightArrowCounter -= 1
                keys['Right'] = "Right........ %s" % rightArrowCounter
                Rotors[3].decreaseW()
            elif e.key == K_LCTRL:
                Copter.gain_altitude()
                for key in keys:
                    keys[key] = key + "........ %s" % counter
                counter += 1
            elif e.key == K_LALT:
                Copter.decline_altitude()
                for key in keys:
                    keys[key] = key + "........ %s" % counter
                counter -= 1

            arrowSubSurface.fill((255, 255, 255))
            x = 20
            for key in keys.keys():
                renderedText = font_render(titleFont, keys[key])
                arrowSubSurface.blit(renderedText, (x, 20))
                x += 200
        elif e.type == QUIT:
            going = False
        pygame.display.update()