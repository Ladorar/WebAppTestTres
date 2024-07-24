const board = document.getElementById('board');
const cols = 9;
const rows = 9;
let currentPlayer = 1;

// Initialize the board with empty cells
function initializeBoard() {
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.dataset.row = row;
            cell.dataset.col = col;
            board.appendChild(cell);
        }
    }
}

// Function to drop a token in the clicked column
function dropToken(col) {
    for (let row = rows - 1; row >= 0; row--) {
        const cell = document.querySelector(`.cell[data-row='${row}'][data-col='${col}']`);
        if (!cell.hasChildNodes()) {
            const token = document.createElement('div');
            token.className = `token player${currentPlayer}`;
            cell.appendChild(token);
            currentPlayer = currentPlayer === 1 ? 2 : 1;
            break;
        }
    }
}

// Initialize the board
initializeBoard();