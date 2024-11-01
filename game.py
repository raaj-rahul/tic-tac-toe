# Tic Tac Toe Game in Python

# Initialize the board
board = [' ' for _ in range(9)]

# Display the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a winner
def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
                      (0, 4, 8), (2, 4, 6)]              # diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check for a draw
def check_draw():
    return ' ' not in board

# Main game loop
def tic_tac_toe():
    current_player = 'X'
    
    while True:
        print_board()
        print(f"\nPlayer {current_player}'s turn.")
        
        # Get valid input from the player
        while True:
            try:
                move = int(input("Enter a position (1-9): ")) - 1
                if board[move] == ' ':
                    board[move] = current_player
                    break
                else:
                    print("This position is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")
        
        # Check for a win or a draw
        if check_winner(current_player):
            print_board()
            print(f"\nPlayer {current_player} wins!")
            break
        elif check_draw():
            print_board()
            print("\nIt's a draw!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
