import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 400, 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the font
font = pygame.font.Font(None, 40)

# Set up the game variables
grid_size = 3
cell_size = width // grid_size
board = [[None] * grid_size for _ in range(grid_size)]
current_player = "X"
game_over = False
winner = None
total_moves = 0

# Function to check if a player has won
def check_winner():
    # Check rows
    for row in board:
        if all(cell == current_player for cell in row):
            return True

    # Check columns
    for col in range(grid_size):
        if all(row[col] == current_player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == current_player for i in range(grid_size)):
        return True
    if all(board[i][grid_size - 1 - i] == current_player for i in range(grid_size)):
        return True

    return False

# Function to check if it's a tie
def check_tie():
    return total_moves == grid_size ** 2

# Function to reset the game
def reset_game():
    global board, current_player, game_over, winner, total_moves
    board = [[None] * grid_size for _ in range(grid_size)]
    current_player = "X"
    game_over = False
    winner = None
    total_moves = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                cell_x = mouse_pos[0] // cell_size
                cell_y = mouse_pos[1] // cell_size
                if board[cell_y][cell_x] is None:
                    board[cell_y][cell_x] = current_player
                    total_moves += 1
                    if check_winner():
                        game_over = True
                        winner = current_player
                    elif check_tie():
                        game_over = True
                    else:
                        # Switch players
                        current_player = "O" if current_player == "X" else "X"

        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                reset_game()

    # Draw the board
    display.fill(BLACK)
    for row in range(grid_size):
        for col in range(grid_size):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(display, WHITE, rect, 1)
            if board[row][col] is not None:
                text = font.render(board[row][col], True, BLUE)
                text_rect = text.get_rect(center=rect.center)
                display.blit(text, text_rect)

    if game_over:
        # Game over message
        if winner:
            winner_text = font.render(f"Player {winner} wins!", True, WHITE)
        else:
            winner_text = font.render("It's a tie!", True, WHITE)
        winner_rect = winner_text.get_rect(center=(width // 2, height // 2 - 20))
        display.blit(winner_text, winner_rect)

        # Restart message
        restart_text = font.render("Press Enter to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(width // 2, height // 2 + 20))
        display.blit(restart_text, restart_rect)

    # Update the display
    pygame.display.flip()
