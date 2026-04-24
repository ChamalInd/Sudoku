# Sudoku

### Project Overview

Simple Sudoku Player built using Python and HTML. There are four modes in tha game as Easy, Medium, Hard and Extreme. The difficulty mode is decided by the amount of clues left for the player. A base score for each mode has been setup earlier and the final game score will be calculated using the factors such as no. of mistakes made by the player and the total time he took to complete the Sudoku board.

Currently no database is connected to the server and all the game statistics are stored temporally in browser cache using Flask Sessions. Therefore all the data will be erased once the browser is closed. 

### Tech Stack
- Back End: Python
- Front End: HTML, CSS, JS

### Project Structure
- `app.py`: Main Python file that contains all the routes and back end logic
- `board.py`: Hold functions related to creating the sudoku board
- `reauirements.txt`: Contains the python libraries used in making the app
- `static`
    - `script.js`: Contains all the front end logic
    - `styles.css`: Contains all the styling
- `templates`
    - `layout.html`: Contains the boilerplate html file
    - `index.html`: Contains all the home page elements
    - `game.html`: Contains all the game page elements
    - `stats.html`: Contains all the stat page elements


### Getting Started
#### Prerequisites
- Make sure you have python installed by running,
```
python --version
```

#### Installation
- Clone the repository into your machine and move into the folder
```
git clone https://github.com/ChamalInd/Sudoku.git
cd Sudoku
```
- Then install all the requirements
```
pip install -r requirements.txt
```

#### Running the app
- Start the Flask app by running
```
flask run
```


