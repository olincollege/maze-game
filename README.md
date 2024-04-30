# Python Project Template Repository

## Overview

Inspired by the nostalgic game "Jumpscare Maze Prank Game Online", the Maze Prank Game
is a game where the cursor is the player. The player uses their cursor to navigate 
through the maze and cannot touch outside the path, otherwise the game will restart.

At the end is a surprise jumpscare, catching the concentrated player off-guard. There 
are three levels, each increasingly more challenging, so the player will have to see 
when the jumpscare pops out!

## How to Use

Click on the "Use this template" button in the top right corner to create a new
repository based on this template. If this is for a class project, we ask that
you keep it in the `olincollege` GitHub organization, and that you refrain from
keeping the repository private. This will ensure that relevant people can access
your repository for assessment, etc.

## Files and Directories

### Game Files

* game.py: The file that runs the game.
* maze.py: The file that has the Model class. This file contains
  all the classes and methods pertaining to saving game and user data.
* view.py: The file that has the View class. The classes and methods that
  display the screen and other visual elements are here.
* controller.py: The file that has the Controller class. It translates inputs
  from the players into calls to the appropriate methods in the board.
* library.py: The file that holds all our level designs.
* img/: The folder storing the images we used for the game.
  * start_btn.png: The start button design.
  * test.png: The green grass used as borders.
 
### Website Files

* docs/: The folder containing anything pertaining to the website.
  * index.md: The file that contains the markdown code for the GitHub website.

## How to Download

To download the Maze Prank Game, follow these steps:

1. Navigate to the Maze Prank Game GitHub page.
2. Click on the green "Code" button.
3. Select "Download ZIP" from the dropdown menu.
4. Once the ZIP file is downloaded, extract its contents to a folder on your computer.
5. Open the folder containing the extracted files in your preferred code editor, such as VSCode. Make sure you have Python and Pygame installed on your system.
6. Run the game.py file from the extracted folder to launch the game.

Enjoy playing the Maze Prank Game!
```

If you already have a `requirements.txt`, the above command will ask you to
rerun the command with the `--force` flag to overwrite it.
