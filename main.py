import tkinter as tk  # Import the tkinter library for creating GUI applications
from src.ui import SOSGameUI  # Import the SOSGameUI class from the ui module for the game's interface
from src.game_logic import GameLogic  # Import the GameLogic class from the game_logic module for handling game logic

def main():
    # Create the main window for the game using tkinter
    root = tk.Tk()

    # Initialize the game logic with a starting grid size of 3
    # The GameLogic class handles the core functionality of the game
    game_logic = GameLogic(3)  

    # Create an instance of the SOSGameUI class to manage the user interface
    # It takes the main window (root) and the game logic object (game_logic) as arguments
    app = SOSGameUI(root, game_logic)

    # Start the tkinter event loop, which waits for user input and updates the UI accordingly
    root.mainloop()

# Check if this script is being run directly (rather than being imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to start the game
