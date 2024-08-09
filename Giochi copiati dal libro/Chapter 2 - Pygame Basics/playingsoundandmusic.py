import pygame

pygame.init()

soundObj = pygame.mixer.Sound('badswap.wav')
soundObj.play()

# Loading and playing background music:
pygame.mixer.music.load('night_detective.mp3')
pygame.mixer.music.play(-1, 0.0)
# ...some more of your code goes here...
import time
time.sleep(10)

pygame.mixer.music.stop()