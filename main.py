import pygame
import sys
import math
import random
from constants import *
from board import create_board, drop_piece, is_valid_location, get_next_open_row, winning_move, print_board
from ai import minimax
from gui import draw_board, display_winner

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Connect 4 AI")
    
    board = create_board()
    print_board(board)
    game_over = False
    turn = random.randint(PLAYER, AI)
    
    myfont = pygame.font.SysFont("monospace", 75)
    
    draw_board(board, screen, myfont)
    pygame.display.update()
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                pygame.display.update()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                if turn == PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))
    
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_PIECE)
    
                        if winning_move(board, PLAYER_PIECE):
                            display_winner(screen, "Player 1 Wins!!", myfont)
                            game_over = True
    
                        turn += 1
                        turn = turn % 2
    
                        print_board(board)
                        draw_board(board, screen, myfont)
    
        if turn == AI and not game_over:
            col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
    
            if is_valid_location(board, col):
                pygame.time.wait(500)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)
    
                if winning_move(board, AI_PIECE):
                    display_winner(screen, "Player 2 Wins!!", myfont)
                    game_over = True
    
                print_board(board)
                draw_board(board, screen, myfont)
    
                turn += 1
                turn = turn % 2
    
    if game_over:
        pygame.time.wait(3000)

if __name__ == "__main__":
    main()
