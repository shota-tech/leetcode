package arraysandhashing

func IsValidSudoku(board [][]byte) bool {
	var rows [9][9]bool
	var cols [9][9]bool
	var grid [9][9]bool

	for row := range board {
		for col, val := range board[row] {
			if val == '.' {
				continue
			}
			index := val - '1'
			gridKey := row/3 + col/3*3
			if rows[row][index] || cols[col][index] || grid[gridKey][index] {
				return false
			}
			rows[row][index] = true
			cols[col][index] = true
			grid[gridKey][index] = true
		}
	}
	return true
}
