import tkinter as tk
import numpy as np
import random
import pygame  # Import pygame for music

# Initialize pygame mixer
pygame.mixer.init()

def start_game():
    global board
    board = create_board()
    update_board()
    for button in buttons:
        button.config(state=tk.NORMAL)
    result_label.config(text="")  # Clear the result label on restart
    show_game_frame()
    play_music()  # Start playing music when the game starts

def create_board():
    return np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])

def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

def random_place(board, player):
    selection = possibilities(board)
    if selection:
        current_loc = random.choice(selection)
        board[current_loc] = player
    return board

def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                break
        if win:
            return True
    return False

def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y, x] != player:
                win = False
                break
        if win:
            return True
    return False

def diag_win(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
            break
    if win:
        return True
    win = True
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x, y] != player:
            win = False
            break
    return win

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def update_board():
    for i in range(3):
        for j in range(3):
            if board[i, j] == 1:
                buttons[i*3+j].config(text="X")
            elif board[i, j] == 2:
                buttons[i*3+j].config(text="O")
            else:
                buttons[i*3+j].config(text="")

def play_move(i, j):
    global board
    if board[i, j] == 0:
        board[i, j] = 1
        update_board()
        if evaluate(board) == 1:
            end_game("Player X wins!")
        elif evaluate(board) == -1:
            end_game("It's a tie!")
        else:
            board = random_place(board, 2)
            update_board()
            if evaluate(board) == 2:
                end_game("Player O wins!")
            elif evaluate(board) == -1:
                end_game("It's a tie!")

def end_game(message):
    for button in buttons:
        button.config(state=tk.DISABLED)
    result_label.config(text=message)
    show_result_frame()
    stop_music()  # Stop the music when the game ends

def restart_game():
    result_frame.pack_forget()
    start_game()

def show_game_frame():
    opening_frame.pack_forget()
    result_frame.pack_forget()
    game_frame.pack()

def show_result_frame():
    game_frame.pack_forget()
    result_frame.pack()

def play_music():
    pygame.mixer.music.load("/mnt/data/Winter Reflections.mp3")
    pygame.mixer.music.play(loops=-1)  # Play the music in a loop

def stop_music():
    pygame.mixer.music.stop()

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the opening screen frame
opening_frame = tk.Frame(root)
opening_frame.pack()

# Create a label for the title
title_label = tk.Label(opening_frame, text="Tic Tac Toe", font=("Arial", 24))
title_label.pack(pady=20)

# Create a button to start the game
start_button = tk.Button(opening_frame, text="Start Game", font=("Arial", 18), command=start_game)
start_button.pack(pady=10)

# Create the main game frame
game_frame = tk.Frame(root)

# Create the Tic-Tac-Toe board buttons
buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(game_frame, text="", font=("Arial", 36), width=5, height=2, 
                           command=lambda i=i, j=j: play_move(i, j))
        button.grid(row=i, column=j)
        buttons.append(button)

# Create the result frame
result_frame = tk.Frame(root)
result_label = tk.Label(result_frame, text="", font=("Arial", 24))
result_label.pack(pady=20)

# Create buttons to restart or exit the game
restart_button = tk.Button(result_frame, text="Restart Game", font=("Arial", 18), command=restart_game)
restart_button.pack(pady=10)

exit_button = tk.Button(result_frame, text="Exit", font=("Arial", 18), command=root.quit)
exit_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

    
       
 





