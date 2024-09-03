# madhan-r-git
<u>**Tic Tac Toe Game**</u>


**Overview:**


This is a simple console-based Tic Tac Toe game implemented in Python. The game offers both single-player and multiplayer modes. In single-player mode, you can choose between easy and hard difficulty levels, while in multiplayer mode, two players can play against each other.


**Features:**


Single Player Mode:


Easy Mode: The AI makes random moves.


Hard Mode: The AI uses a strategy to maximize its chances of winning.


Multiplayer Mode:


Two players can play against each other on the same console.


**Game Modes:**


Single Player:


Play against the computer.
Choose between Easy or Hard difficulty.


Multiplayer:


Play against another player.
Both players take turns on the same console.


**How to Play:**


Run the Game:


Execute the main() function in the script.


Choose Game Mode:


Input S for Single Player or M for Multiplayer.

Choose Difficulty (Single Player Mode):

Input E for Easy mode or H for Hard mode.


Make a Move:


Enter a number between 1 and 9 to place your symbol (X or O) on the board.

Enter -1 to surrender.


Win the Game:


Get three of your symbols in a row, column, or diagonal to win.


**File Structure:**

main.py: The main entry point of the game. Handles user input and initiates the game.

Base_page.py: Contains the base logic for the Tic Tac Toe game, including the board setup and move validation.

Single_player.py: Implements the logic for single-player mode, including AI moves for both easy and hard difficulties.

Multi_player.py: Implements the logic for multiplayer mode, where two players can compete.

