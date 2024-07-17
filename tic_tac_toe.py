def print_board(board):
    # This function prints the current state of the board
    for row in board:
        print(" | ".join(row))  # Print each row separated by "|"
        print("-" * 5)  # Print a line to separate the rows

def check_winner(board, player):
    # This function checks if the specified player has won the game
    # Check all rows for a win
    for row in board:
        if all(s == player for s in row):
            return True
    # Check all columns for a win
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Check the main diagonal for a win
    if all(board[i][i] == player for i in range(3)):
        return True
    # Check the anti-diagonal for a win
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Start with player "X"
    
    # Play up to 9 turns (the maximum number of moves in a tic-tac-toe game)
    for _ in range(9):
        print_board(board)  # Print the current state of the board
        
        # Get the row and column from the current player
        row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))
        
        # Check if the chosen cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player  # Place the player's mark on the board
            
            # Check if the current player has won
            if check_winner(board, current_player):
                print_board(board)  # Print the final state of the board
                print(f"Player {current_player} wins!")  # Announce the winner
                return  # End the game
            
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken, try again.")  # Ask the player to choose a different cell
    
    # If all 9 moves are played and no one wins, it's a tie
    print_board(board)  # Print the final state of the board
    print("It's a tie!")  # Announce the tie

def play_game():
    # This function handles the main game loop with the option to restart
    while True:
        tic_tac_toe()  # Start a new game
        choice = input("Do you want to play again? (yes/no): ").lower()  # Ask if the players want to play again
        if choice != 'yes':
            print("Thanks for playing!")  # Thank the players
            break  # Exit the loop and end the game

if __name__ == "__main__":
    play_game()  # Start the game with the option to restart

