Still in the process of updating this repo

# Human-vs-AI-BattleShip
![Images](Images/battleship.jpg)
#### Goal
* Practice using classes, object oriented programing, and inheritance/multiple inheritance to solve a complex problem.

### Prerequisites
* PyCharm (Recommended)
  - [Download PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
* Understanding for the game of BattleShip
  - If you have not played before, please play [this version](https://www.battleshiponline.org/) to gain familiarity with how the game works

## Running the tests

* First, download the zip into a desired directory on your device
* Next, the game configuration and random seed will be passed on the command line. To make them accessable to the program, you must use sys.argv and import the sys module. [This website](https://appdividend.com/2019/01/22/python-sys-argv-tutorial-command-line-arguments-example/) can be used to learn about how to use command line arguments. I will also explain below how to configure these arguments in PyCharm
  - First, to edit the command line argument in PyCharm click on your project and select Edit Configuration
  ![Images](Images/battleship.jpg)
  - Next, fill in the parameter fields with the command line parameters. Each parameter is separated by whitespace. If one of your parameters has whitespace enclose it in quotes
  ![Images](Images/battleship.jpg)
* The only other required step is to open the main.py file, and run the program. Player 1 will then be prompted to select their player type as either human, random AI, cheating AI, or search and destory AI. Each player type is defined as follows:
  - Human: Simply used to define a human player. Human players will manually chose where to place their ships on the board at the start of the game, and they will manually chose where to fire at each turn.
  - Random AI: Places ships on board in randomly chosen locations at start of game. Guesses coordinates to fire at randomly. 
  - Cheating AI: Places ships on board in randomly chosen locations at start of game. Plays a perfect game of BattleShip. It never misses and always hits its opponent's ships.
  - Search and Destory AI: Places ships in randomly chosen locations at start of game. When playing, operates in one of two modes: Search or Destroy. While in search mode, randomly guesses where to fire, just like the random AI. However, when it gets a hit, it switches to Destroy mode. In Destroy Mode, it will shoot to the left, above, right, and below the position that it hit. If it got any hits while doing this, it will repeat the process. Will switch back to Search Mode after it has finished shooting around all of the surroudning locations and hasn't found any more hits.
* Note about gameplay: 
  - Each player will have a placement board, and a scanning board. The placement board is the board that contains all of that players ships, and what the view of their board curretnly looks like. The scanning board is used to select where to fire at, and show the curent player all of the spots that they have either fired at and hit, fired at and missed, or have not yet fired at.

## Gameplay Sample
Player 1 please enter your name: 
Bob's Placement Board  
  0 1 2 3 4 5  
0 * * * * * *  
1 * * * * * *  
2 * * * * * *  
3 * * * * * *  
4 * * * * * *  

Bob enter horizontal or vertical for the orientation of Patrol which is 2 long:
Bob, enter the starting position for your Patrol ship ,which is 2 long, in the form row, column: 
Bob's Placement Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * * * *
2 P P * * * *
3 * * * * * *
4 * * * * * *
Bob enter horizontal or vertical for the orientation of Submarine which is 3 long:
Bob, enter the starting position for your Submarine ship ,which is 3 long, in the form row, column:
Bob's Placement Board
  0 1 2 3 4 5
0 S S S * * *
1 * * * * * *
2 P P * * * *
3 * * * * * *
4 * * * * * *

Player 2 please enter your name:
Sally's Placement Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * * * *
2 * * * * * *
3 * * * * * *
4 * * * * * *

Sally enter horizontal or vertical for the orientation of Patrol which is 2 long:
Sally, enter the starting position for your Patrol ship ,which is 2 long, in the form row, column:
Sally's Placement Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * * * *
2 P * * * * *
3 P * * * * *
4 * * * * * *

Sally enter horizontal or vertical for the orientation of Submarine which is 3 long:
Sally, enter the starting position for your Submarine ship ,which is 3 long, in the form row, column:
Sally's Placement Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * * * *
2 P * * * * *
3 P * * * * *
4 * * S S S *

Bob's Scanning Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * * * *
2 * * * * * *
3 * * * * * *
4 * * * * * *

Bob's Board
  0 1 2 3 4 5
0 S S S * * *
1 * * * * * *
2 P P * * * *
3 * * * * * *
4 * * * * * *

Bob, enter the location you want to fire at in the form row, column:
Miss
Bob's Scanning Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * O * *
2 * * * * * *
3 * * * * * *
4 * * * * * *
Bob's Board
  0 1 2 3 4 5
0 S S S * * *
1 * * * * * *
2 P P * * * *
3 * * * * * *
4 * * * * * *

Sally's Scanning Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * * * *
2 * * * * * *
3 * * * * * *
4 * * * * * *
Sally's Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * O * *
2 P * * * * *
3 P * * * * *
4 * * S S S *

Sally, enter the location you want to fire at in the form row, column:
Miss
Sally's Scanning Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * * * *
2 * * * * * *
3 * * * * * *
4 * * * * O *
Sally's Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * O * *
2 P * * * * *
3 P * * * * *
4 * * S S S *

Bob's Scanning Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * O * *
2 * * * * * *
3 * * * * * *
4 * * * * * *
Bob's Board
  0 1 2 3 4 5
0 S S S * * *
1 * * * * * *
2 P P * * * *
3 * * * * * *
4 * * * * O *

Bob, enter the location you want to fire at in the form row, column:
Miss
Bob's Scanning Board
  0 1 2 3 4 5
0 * * * * * *
1 O * * O * *
2 * * * * * *
3 * * * * * *
4 * * * * * *
Bob's Board
  0 1 2 3 4 5
0 S S S * * *
1 * * * * * *
2 P P * * * *
3 * * * * * *
4 * * * * O *

Sally's Scanning Board
  0 1 2 3 4 5
0 * * * * * *
1 * * * * * *
2 * * * * * *
3 * * * * * *
4 * * * * O *
Sally's Board
  0 1 2 3 4 5
0 * * * * * *
1 O * * O * *
2 P * * * * *
3 P * * * * *
4 * * S S S *

Sally, enter the location you want to fire at in the form row, column:
Miss
Sally's Scanning Board
  0 1 2 3 4 5
0 * * * O * *
1 * * * * * *
2 * * * * * *
3 * * * * * *
4 * * * * O *
Sally's Board
  0 1 2 3 4 5
0 * * * * * *
1 O * * O * *
2 P * * * * *
3 P * * * * *
4 * * S S S *

Bob's Scanning Board
  0 1 2 3 4 5
0 * * * * * *
1 O * * O * *
2 * * * * * *
3 * * * * * *
4 * * * * * *
Bob's Board
  0 1 2 3 4 5
0 S S S O * *
1 * * * * * *
2 P P * * * *
3 * * * * * *
4 * * * * O *

Bob, enter the location you want to fire at in the form row, column:
You hit Sally's Patrol!
Bob's Scanning Board
  0 1 2 3 4 5
0 * * * * * *
1 O * * O * *
2 X * * * * *
3 * * * * * *
4 * * * * * *
Bob's Board
  0 1 2 3 4 5
0 S S S O * *
1 * * * * * *
2 P P * * * *
3 * * * * * *
4 * * * * O *

Sally's Scanning Board
  0 1 2 3 4 5
0 * * * O * *
1 * * * * * *
2 * * * * * *
3 * * * * * *
4 * * * * O *
Sally's Board
  0 1 2 3 4 5
0 * * * * * *
1 O * * O * *
2 X * * * * *
3 P * * * * *
4 * * S S S *

Sally, enter the location you want to fire at in the form row, column: Miss
Sally's Scanning Board
  0 1 2 3 4 5
0 * * * O * *
1 * * O * * *
2 * * * * * *
3 * * * * * *
4 * * * * O *
Sally's Board
  0 1 2 3 4 5
0 * * * * * *
1 O * * O * *
2 X * * * * *
3 P * * * * *
4 * * S S S *

## Author

* **William Schmidt** - [Wil's LikedIn](https://www.linkedin.com/in/william-schmidt-152431168/)
