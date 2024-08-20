import os, pygame

WIN_WIDTH = 700
WIN_HEIGHT = 600

Script_Path = os.path.dirname(os.path.abspath(__file__))
BOARD_IMG = pygame.transform.scale(pygame.image.load(os.path.join(Script_Path,"imgs\\Board.png")),(WIN_WIDTH,WIN_HEIGHT))


Green_Arrow = pygame.transform.scale(pygame.image.load(os.path.join(Script_Path,"imgs\\Green_Arrow.png")),(int(WIN_WIDTH*0.07),int(WIN_HEIGHT*0.07)))



PIECE_WIDTH = WIN_WIDTH/7
PIECE_HEIGHT = WIN_HEIGHT / 6
Win_Value = 250

YELLOW = (200, 210, 35)
RED = (240, 0, 0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (0, 230, 60)
LEAF_GREEN = (70, 190, 90)
ORANGE = (245, 75, 0)
PURPLE = (145, 85, 185)
DARK_PURPLE = (100, 50, 130)
LIGHT_BLUE = (50, 35, 220)
LIGHT_BLUE_V2 = (50, 140, 255)
DARK_BLUE = (0, 85, 185)
DARK_BLUE_V2 = (65, 65, 135)
PINK = (240, 40, 125)
CYAN = (40, 200, 145)
GRAY = (170,170,170)
GOLD = (255, 215, 0)
BRONZE = ("#cd7f32")

