import pygame

pygame.init()

soundObj = pygame.mixer.Sound('beep1.ogg')
soundObj.play()

import time

time.sleep(5) # wait and let the sound play for 1 second

soundObj.stop()