WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32

FPS = 60

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

PLAYER_LAYER = 2
# layer our walls and barriers are on
BLOCK_LAYER = 1

PLAYER_SPEED = 3

# create the tilemap, map the player moves on
# tilemap is a list [ ] with rows and columns like a grid
# height is 480 pixels each tile is 32 pixels, 480 divided by 32 is 15, so we have 15 rows on map, each row is a string
# width is 640 pixels divided by 32 so we get 20 columns
tilemap = [
    # B stands for block and are walls or other unpassable objects
    # . stand for grass or areas the player can move on
    # P stands for player
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B........BBB.......B',
    'B..................B',
    'B........P.........B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B........BBB.......B',
    'B..................B',
    'B...BB.............B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
]