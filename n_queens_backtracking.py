import time

DELAY = 0.5

def print_board(board, step, action):
    """Menampilkan papan catur pada setiap langkah proses."""
    print(f"\nLangkah ke-{step}: {action}")

    border_length = (2 * len(board)) + 3 
    print("-" * border_length)
    
    for row in board:
        print("| " + " ".join(row) + " |")
    print("-" * border_length)
    time.sleep(DELAY)

def is_safe(board, row, col, n):
    """Memeriksa apakah posisi (row, col) aman untuk menempatkan ratu."""

    for i in range(col):
        if board[row][i] == 'Q':
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens_util(board, col, n, state):
    """Fungsi rekursif utama untuk menyelesaikan N-Queens dengan backtracking."""

    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):

            board[row][col] = 'Q'
            state['step'] += 1
            print_board(board, state['step'], f"Menempatkan ratu di baris {row}, kolom {col}")

            if solve_n_queens_util(board, col + 1, n, state):
                return True

            board[row][col] = '.'
            state['step'] += 1
            print_board(board, state['step'], f"BACKTRACK: Menghapus ratu dari baris {row}, kolom {col}")

    return False

def solve_n_queens(n=4):
    """Fungsi utama untuk menjalankan simulasi N-Queens."""
    board = [['.' for _ in range(n)] for _ in range(n)]
    state = {'step': 0}

    print("=" * 55)
    print(f"SIMULASI ALGORITMA BACKTRACKING: {n}-QUEENS PROBLEM")
    print("=" * 55)

    if solve_n_queens_util(board, 0, n, state):
        print("\n" + "=" * 55)
        print(f"SOLUSI DITEMUKAN DALAM {state['step']} LANGKAH")
        print("=" * 55)
        print("Papan akhir:")
        
        border_length = (2 * len(board)) + 3
        print("-" * border_length)
        for row in board:
            print("| " + " ".join(row) + " |")
        print("-" * border_length)
    else:
        print("\nSolusi tidak ditemukan.")

if __name__ == "__main__":
    solve_n_queens(4)