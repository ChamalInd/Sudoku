let time = 0;
let interval;
let selectedBtn = null
const btns = document.querySelectorAll('.sudoku-btns');
let gameBoard = [
    [['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', '']]
]

// increment timer 
function gamePageTimmer() {    
    const timmer = document.querySelector('.clock');
    
    clearInterval(interval)

    interval = setInterval(() => {
        time++;

        seconds = time % 60;
        minutes = Math.trunc(time / 60);

        timmer.innerHTML = minutes.toString().padStart(2, '0') + ' : ' + seconds.toString().padStart(2, '0');

    }, 1000);

}

// start timer when game page loads 
document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.clock')) {
        gamePageTimmer();
    }
});

// get selected box in sudoku board 
function buttonSelect(button) {
    // check for a currently active button 
    const currentSelected = document.querySelector('.sudoku-btns.active');
    
    if (currentSelected) {
        currentSelected.classList.remove('active');
        for (let i = 0; i < btns.length; i++) {
            btns[i].classList.remove('others');
        }
    }

    // selecting the button 
    selectedBtn = button;
    selectedBtn.classList.add('active');

    // highlighting the impact buttons
    let current = button.id.split('x').map(Number);
    
    // filling rows 
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            id = `${current[0]}x${i}x${j}`;
            document.getElementById(id).classList.add('others');
        }
    }

    // filling columns 
    for (let i = 0; i < 9; i++) {
        id = `${i}x${current[1]}x${current[2]}`;
        document.getElementById(id).classList.add('others');
    }

    // filling sections 
    let row = Math.trunc(current[0] / 3) * 3;
    for (let i = row; i < row + 3; i++) {
        for (let j = 0; j < 3; j++) {
            id = `${i}x${current[1]}x${j}`;
            document.getElementById(id).classList.add('others');
        }
    }

}

// enter or clear values from the board 
function keyPadAction(button) {
    let text = button.id;
    const numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    if (numbers.includes(text)){
        selectedBtn.innerText = text;
    } else if (text === 'c') {
        selectedBtn.innerText = '';
    }

    syncWithServer();
    
}

// syncing the webpage with flask app 
async function syncWithServer() {
    // updating game board 
    for (let i = 0; i < btns.length; i ++) {
        let index = btns[i].id.split('x').map(Number);
        if (btns[i].innerText === '') {
            gameBoard[index[0]][index[1]][index[2]] = btns[i].innerText;
        } else {
            gameBoard[index[0]][index[1]][index[2]] = Number(btns[i].innerText);
        }
    }

    try {
        const response = await fetch('/update-board', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ board: gameBoard, active: selectedBtn.id.split('x').map(Number) })
        });

        const serverResponse = await response.json();
        if (serverResponse.server_message === 'incorrect' && selectedBtn.innerText) {
            selectedBtn.classList.add('error');
        } else if (serverResponse.server_message === 'correct' || selectedBtn.innerText === '') {
            selectedBtn.classList.remove('error');
        }
    } catch (error) {
        alert('Sync faild ' + error);
    }
}