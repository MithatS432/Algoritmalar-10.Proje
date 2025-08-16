#Problemin tüm olasılıklarını sistematik olarak deneme
def is_safe(board, row, col, n):
    # Aynı sütun kontrolü
    for i in range(row):
        if board[i] == col:
            return False

    # Sol üst çapraz kontrolü
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Sağ üst çapraz kontrolü
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(n, row=0, board=[]):
    if row == n:
        print("Çözüm:", board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board.append(col)
            solve_nqueens(n, row + 1, board)
            board.pop()  # geri dön
    return False


solve_nqueens(4)  # 4-Queens için çözüm
