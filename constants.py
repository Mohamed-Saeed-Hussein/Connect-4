
# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Board Dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7

# Player Identity
PLAYER = 0
AI = 1

# Piece Identity
PLAYER_PIECE = 1
AI_PIECE = 2
EMPTY = 0

# Window Dimensions
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE # 700px
height = (ROW_COUNT + 1) * SQUARESIZE # 700px
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)
