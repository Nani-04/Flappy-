import pygame
import sys
from pygame.locals import *
from pptx import Presentation
from pptx.util import Inches, Pt

# Global Variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'C:\\Users\\thall\\OneDrive\\Desktop\\Flappy\\gallery\\sprites\\bird.png'
BACKGROUND = 'C:\\Users\\thall\\OneDrive\\Desktop\\Flappy\\gallery\\sprites\\background.png'
PIPE = 'C:\\Users\\thall\\OneDrive\\Desktop\\Flappy\\gallery\\sprites\\pipe.png'

# Initialize pygame
pygame.init()

# ... (rest of the code remains unchanged)

if __name__ == "__main__":
    prs = Presentation()

    # Welcome Screen Slide
    welcomeScreen(prs)

    # Game Slides
    score = mainGame()
    addGameSlide(prs, score)
