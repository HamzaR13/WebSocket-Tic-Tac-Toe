from flask import Flask, render_template
from flask_sock import Sock
import json

# initialize a Flask application
app = Flask(__name__)
# using Flask-Sock <- WebSocket extension for flask
sock = Sock(app)    # initialize WebSockets for this app



# ===========
# GAME DATA
# ===========

# empty tic-tac-toe board:
board = [["" for _ in range(3)] for _ in range(3)]

# track connected users
users = {}

# player markers
player_symbols = ["X", "O"]

# track whose turn it is, so  0 <- P1, 1 <- P2, ...
curr_turn = 0


def check_winner(board):
    """Check if there's a winner in the Tic-Tac-Toe board."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]  # Return "X" or "O" as the winner

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]  # Return "X" or "O"

    # Check main diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]  # Return "X" or "O"

    # Check anti-diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]  # Return "X" or "O"

    return None  # No winner yet


def reset_game():
    """Reset the board and clear player assignments."""
    global board, curr_turn
    board = [["" for _ in range(3)] for _ in range(3)]
    curr_turn = 0  # Reset to player "X" turn
    print("Game has been reset!")



# ===========
# ROUTES
# ===========

# route, serves the main page
# this function handles requests to '/' and serves the index.html page
@app.route("/")
def home():
    return render_template("index.html")    # loading HTML file for the frontend

# create a new socket
# socket route
@sock.route('/receiver')    # setting up WebSocket endpoint at '/receiver'
def receiver(connection):

    global curr_turn

    # assigning player markers
    if connection not in users:
        if len(users) < 2:  # limit of 2 players
            users[connection] = player_symbols[len(users)]  # new player is symbol from player_symbols
            print(f"New player has joined as {users[connection]}")
        # handle extra player
        else:
            connection.send(json.dumps({"error": "Game is full"}))
            connection.close()
            return

    symbol_player = users[connection]

    # listening for messages
    while True:
        # message for whenever someone moves
        try:
            # receive data from client
            message = connection.receive()  # listens for incoming messages
            data = json.loads(message)  # parse JSON message
            row, col = data.get("row"), data.get("col") # extracting move coordinates

            # validate move
            if board[row][col] == "":   # checking if cell is empty
                board[row][col] = symbol_player # place player's symbol
                winner = check_winner(board)  # Check if this move wins the game

                # send updated board to all players
                # If there's a winner, notify all players and reset the game
                if winner:
                    for conn in users.keys():
                        conn.send(json.dumps({"winner": winner, "board": board}))

                    # Reset game state after win
                    reset_game()

                else:
                    # No winner yet, just update the board
                    curr_turn = 1 - curr_turn  # Switch turns (0 ↔ 1)
                    for conn in users.keys():
                        conn.send(json.dumps({"board": board, "turn": player_symbols[curr_turn]}))

            else:
                connection.send(json.dumps({"error": "Invalid move"}))

        # if an error occurs (such as user disconnects), the connection is removed from users
        except Exception as e:
            print(f"Player {users[connection]} disconnected: {e}")
            del users[connection]
            break


# running Flask app when executing: python main.py
if __name__ == "__main__":
    app.run()
