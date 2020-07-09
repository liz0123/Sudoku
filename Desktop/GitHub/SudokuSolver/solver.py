
board= [[5,3,0,0,7,0,0,0,0],
		[6,0,0,1,9,5,0,0,0],
		[0,9,8,0,0,0,0,6,0],
		[8,0,0,0,6,0,0,0,3],
		[4,0,0,8,0,3,0,0,1],
		[7,0,0,0,2,0,0,0,6],
		[0,6,0,0,0,0,2,8,0],
		[0,0,0,4,1,9,0,0,5],
		[0,0,0,0,8,0,0,7,9]]

def sudokuSolver(board):
	# Input: Double array representing the Sudoku Puzzle
	# Outputs: True or False dependon on if a solucion was found for the puzzle.
	# Note: if found solution, puzzle will be updated with solution.
	pos = emptyCell(board)
	if not pos:
		return True
	for i in range(1,len(board)+1):
		if verify(board,pos,i):
			board[pos[0]][pos[1]] = i
			if sudokuSolver(board):
				return True
			board[pos[0]][pos[1]] = 0
	return False

def verify(board,pos,num):
	# Input: Sudoku board, location if empty cell, and number for empty cell
	# Output: Return true if number to be added is not in the row, col and subsection of board
	row = pos[0]
	col = pos[1]
	#check row
	if num in board[row]:
		return False
	#check col
	for i in range(len(board[col])):
		if num == board[i][col]:
			return False
	#check subsection
	row = int(row/3)*3
	col = int(col/3)*3
	for r in range(row,row+3):
		for c in range(col, col+3):
			if num == board[r][c]:
				return False
	return True

def emptyCell(board):
	# Input: Sudoku board
	# Output: location of empty cell
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i,j)
	return None

def printBoard(board):
	for i in range(len(board)):
		print()
		if i%3 == 0 and i != 0:
				print("------------------------------")
		for j in range(len(board[0])):
			if j %3 ==0 and not(j in [0,len(board[0])-1]):
				print(" | ", end="")
			print(str(board[i][j])+" ",end="")
