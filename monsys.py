# Import the create_monsys function from __init__.py
from website import create_monsys, socketio

# Assigns the variable run_monsys to the function create_monsys
app = create_monsys()

if __name__ == "__main__":
    # Initializes the MONSYS Server
    socketio.run(app, debug=True, host="0.0.0.0", port=7337)