# Import the create_monsys function from __init__.py
from website import create_monsys

# Assigns the variable run_monsys to the function create_monsys
run_monsys = create_monsys()

if __name__ == "__main__":
    # Initializes the MONSYS Server
    run_monsys.run(debug=True, host="0.0.0.0", port=7337)