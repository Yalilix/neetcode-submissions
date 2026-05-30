class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const row = new Map()
        const col = new Map()
        const square = new Map()

        for (let i = 0; i < board.length; i++) {
            for (let j = 0; j < board[i].length; j++) {
                if (board[i][j] === '.') continue
            
                const key = String(Math.floor(i / 3)) + String(Math.floor(j / 3))

                if (
                    (row.get(i) && row.get(i).has(board[i][j])) ||
                    (col.get(j) && col.get(j).has(board[i][j])) ||
                    (square.get(key) && square.get(key).has(board[i][j]))
                ) {
                    return false
                }

                if (!row.has(i)) row.set(i, new Set())
                if (!col.has(j)) col.set(j, new Set())
                if (!square.has(key)) square.set(key, new Set())

                row.get(i).add(board[i][j])
                col.get(j).add(board[i][j])
                square.get(key).add(board[i][j])
            }
        }
        return true
    }
}
