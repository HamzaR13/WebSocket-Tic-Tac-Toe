# WebSocket-Tic-Tac-Toe

This is a real-time, multiplayer Tic-Tac-Toe game built using Flask, Flask-Sock (WebSockets), and JavaScript. The game allows two players to connect, take turns making moves, and updates the board dynamically through WebSockets.

🔹 Tech Stack:
- Backend: Flask, Flask-Sock (WebSockets)
- Frontend: HTML, CSS, JavaScript
- Game Logic: Server maintains a 3×3 board and tracks player turns.
- Communication: WebSockets enable instant updates between players.

🔹 Features:
- Live updates via WebSockets (no page refresh required).
- Turn-based logic with player assignment ("X" and "O").
- Win detection (checks rows, columns, and diagonals).
- Game reset after a win to allow replay.
- Error handling (e.g., invalid moves, full game slots).

SETUP INSTRUCTIONS:
# Clone the repository
git clone https://github.com/yourusername/websocket-tic-tac-toe.git
cd websocket-tic-tac-toe

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

# Install dependencies
pip install flask flask-sock

# Run the game
python main.py

![Player Connection](https://raw.githubusercontent.com/HamzaR13/WebSocket-Tic-Tac-Toe/main/images/Capture.PNG)
![Player Connection](https://raw.githubusercontent.com/HamzaR13/WebSocket-Tic-Tac-Toe/main/images/Capture2.PNG)
![Player Connection](https://raw.githubusercontent.com/HamzaR13/WebSocket-Tic-Tac-Toe/main/images/Capture3.PNG)
![Player Connection](https://raw.githubusercontent.com/HamzaR13/WebSocket-Tic-Tac-Toe/main/images/Capture4.PNG)
