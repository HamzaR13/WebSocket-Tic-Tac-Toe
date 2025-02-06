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

python main.py

GAME SCREENSHOTS:
![Capture](https://github.com/user-attachments/assets/7593a040-3d30-4a42-a5d5-544a2548402d)
![Capture 2](https://github.com/user-attachments/assets/3ceb8f1d-d3ed-467b-a656-a9c42afd5b94)
![Capture 3](https://github.com/user-attachments/assets/0ded346f-ca41-45bf-bc83-b052e389a9a6)
![Capture 4](https://github.com/user-attachments/assets/f54c8a74-2beb-49a5-8a8a-7867b9f7bf12)
