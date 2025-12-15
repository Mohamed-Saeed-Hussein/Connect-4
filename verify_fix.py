import numpy as np
import math
from board import create_board, drop_piece, print_board
from ai import minimax
from constants import *

def test_refactor_and_logic():
    print("Testing refactored code and logic...")
    board = create_board()
    
    # Setup winning condition: AI has 3 in a row
    # Row 0: AI AI AI Empty ...
    drop_piece(board, 0, 0, AI_PIECE)
    drop_piece(board, 0, 1, AI_PIECE)
    drop_piece(board, 0, 2, AI_PIECE)
    
    # Dummy moves for player
    drop_piece(board, 1, 0, PLAYER_PIECE)
    drop_piece(board, 1, 1, PLAYER_PIECE)
    drop_piece(board, 1, 2, PLAYER_PIECE)

    print("Board State:")
    print_board(board)
    
    try:
        # Check depth 2 just to be quick
        col, score = minimax(board, 4, -math.inf, math.inf, True)
        print(f"AI chose column: {col} with score: {score}")
        
        # Expected score: 100000000000000 + depth.
        # Winning move is immediate, so recursion should handle it.
        # If depth start is 4. depth=4 -> calls depth=3...?
        # Actually usually it finds it at the current depth call if it's immediate?
        # No, minimax checks valid_locations.
        # 'minimax' calls 'winning_move' at start? No, it calls is_terminal_node.
        # If it's not terminal, it recurses.
        # If we drop a piece, is it terminal?
        # The loop drops a piece, then calls minimax(depth-1).
        # Inside that call, is_terminal_node checks if the *previous* move won.
        # So: Recursion 4 -> Drop winning piece -> Recursion 3 (sees win) -> Returns score.
        # So score should be around 100000000000000 + 3.
        
        if col == 3:
            print("PASS: AI chose winning move.")
        else:
            print(f"FAIL: AI missed winning move (got {col}).")
            
        if score > 100000000000000:
             print("PASS: Score indicates winning move detected.")
        else:
             print(f"FAIL: Score {score} too low for win.")

    except Exception as e:
        print(f"FAIL: Exception occurred: {e}")

if __name__ == "__main__":
    test_refactor_and_logic()
