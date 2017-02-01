#importing modules
import pygame
from pygame.locals import *
from sys import exit
  
  
#initializing variables
pygame.init()
screen=pygame.display.set_mode((640,480),0,24)
pygame.display.set_caption("Motor Key Press Test")
f1=pygame.font.SysFont("comicsansms",24)
incrementCounter = 0
  
#main loop which displays the pressed keys on the screen
while True:
 for i in pygame.event.get():
  if i.type==QUIT:
   exit()
  a=100
  screen.fill((255,255,255))
  if pygame.key.get_focused():
   press=pygame.key.get_pressed()
   for i in xrange(0,len(press)): 
    if press[i]==1:
     name=pygame.key.name(i)
     if name ==  "numlock":
        text=f1.render("H",True,(0,0,0))
        screen.blit(text,(100,a))
        a=a+100
        continue
     if name == "up":
        incrementCounter = incrementCounter + 1
        incrementText = "Increasing........ %s" % (incrementCounter)
        text = f1.render(incrementText,True,(0,0,0))        
        screen.blit(text,(200,a))        
        a=a+100
     if name == "down":
        incrementCounter = incrementCounter - 1
        incrementText = "Decreasing........ %s" % (incrementCounter)
        text = f1.render(incrementText,True,(0,0,0))        
        screen.blit(text,(200,a))        
        a=a+100
     if name == "q":
        break
     pygame.display.update()
  delay,seconds = pygame.key.get_repeat()
  delayTxt = "Delay........ %s" % (delay)
  delayTxtA = f1.render(delayTxt,True,(0,0,0))
  screen.blit(delayTxtA,(100,a))
  a=a+100
  secondsTxt = "Seconds........ %s" % (seconds)
  secondsTxtA = f1.render(secondsTxt,True,(0,0,0))
  screen.blit(secondsTxtA,(100,a))
  a=a+100








#     #! /usr/bin/env python
#############################################################################
## File name : keyinput.py
## Purpose : A Small Demo Practice Prgram using Pygame API
## Usages : Displays the pressed keys on the screen
## Start date : 17/12/2011
## End date : 17/12/2011
## Author : Ankur Aggarwal
## License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
## Dependency  : None
#############################################################################
  
##importing modules
#import pygame
#from pygame.locals import *
#from sys import exit
  
  
##initializing variables
#pygame.init()
#screen=pygame.display.set_mode((640,480),0,24)
#pygame.display.set_caption("Motor Key Press Test")
#f1=pygame.font.SysFont("comicsansms",24)
  
##main loop which displays the pressed keys on the screen
#while True:
# for i in pygame.event.get():
#  if i.type==QUIT:
#   exit()
#  a=100
#  screen.fill((255,255,255))
#  if pygame.key.get_focused():
#   press=pygame.key.get_pressed()
#   for i in xrange(0,len(press)): 
#    if press[i]==1:
#     name=pygame.key.name(i)
#     text=f1.render(name,True,(0,0,0))
#     screen.blit(text,(100,a))
#     a=a+100
#   pygame.display.update()