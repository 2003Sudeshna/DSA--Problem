def solveNQueens(n):
    def is_safe(board, row, col):
        # Check if it's safe to place a queen at board[row][col]
        # Check the current column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check the upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check the upper-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0)
    
    return solutions

# Example usage:
n = 4
result = solveNQueens(n)
for solution in result:
    for row in solution:
        print(row)
    print()
