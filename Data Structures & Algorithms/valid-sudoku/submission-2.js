class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const row = {}
        const col = {}
        const square = {}

        for (let i = 0; i < board.length; i++) {
            for (let j = 0; j < board[i].length; j++) {
                if (board[i][j] == '.') continue

                if (row[i] == undefined) {
                    row[i] = {}
                }

                if (row[i][board[i][j]] == true) {
                    return false
                } else {
                    row[i][board[i][j]] = true
                }
            

                if (col[j] == undefined) {
                    col[j] = {}
                }

                if (col[j][board[i][j]] == true) {
                    return false
                } else {
                    col[j][board[i][j]] = true
                }
                
                const key = String(Math.floor(i / 3)) + String(Math.floor(j / 3))
                if (square[key] == undefined) {
                    square[key] = {}
                }

                if (square[key][board[i][j]] == true) {
                    return false
                } else {
                    square[key][board[i][j]] = true
                }
            }
        }
        return true
    }
}
