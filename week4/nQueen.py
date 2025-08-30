def is_safe(board, row, col, n):
    # Check this column up
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens_util(board, row, n):
    # Base case: If all queens are placed
    if row == n:
        return True  # Solution found

    # Try placing queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen

            # Recur to place the rest
            if solve_nqueens_util(board, row + 1, n):
                return True

            # Backtrack if placing queen doesn't lead to a solution
            board[row][col] = 0

    return False  # No solution found in this row


def solve_nqueens(n):
    # Create an N×N board initialized with 0s
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_nqueens_util(board, 0, n):
        print("No solution exists for N =", n)
        return

    # Print the solution
    print(f"Solution for {n}-Queens:")
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))



n = int(input("Enter the value of N: "))
solve_nqueens(n)