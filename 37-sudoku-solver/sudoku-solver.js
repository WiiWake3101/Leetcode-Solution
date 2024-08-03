/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    function sudokuSolver(board) {
        for(let i = 0; i < 9; i++) {
            for(let j = 0; j < 9; j++) {
                if(board[i][j] === '.') {
                    let char = '1';
                    while(char <= 9) {
                        if(isValidSudoku(i, j, char)) {
                            board[i][j] = char;
                            
                            if(sudokuSolver(board)) return true;
                            else board[i][j] = '.';
                        }
                        char = (parseInt(char) + 1).toString();
                    }
                    return false;
                }
            }
        }
        return true;
    }
    function isValidSudoku(row, col, char) {
        for(let i = 0; i < 9; i++) {
            if(board[row][i] === char) return false;
        }
        
        for(let i = 0; i < 9; i++) {
            if(board[i][col] === char) return false;
        }
        
        let x = Math.floor(row / 3) * 3;
        let y = Math.floor(col / 3) * 3;
        
        for(let i = 0; i < 3; i++) {
            for(let j = 0; j < 3; j++) {
                if(board[x + i][y + j] === char) return false;
            }
        }
        return true;
    }
    sudokuSolver(board);
};