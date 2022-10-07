n = 5


def printboard(board):
    for linia in board:
        print(linia)
    return


def possible(board, x, y, n):
    #amunt
    if y >= 2:
        if x >= 1:
            if board[y-2][x-1] == n and board[y][x] == 0:
                return True
        if x <= len(board[y]) - 2:
            if board[y-2][x+1] == n and board[y][x] == 0:
                return True
    #avall
    if y <= len(board) - 3:
        if x >= 1:
            if board[y + 2][x - 1] == n and board[y][x] == 0:
                return True
        if x <= len(board[y]) - 2:
            if board[y + 2][x + 1] == n and board[y][x] == 0:
                return True
    #esquerra
    if x >= 2:
        if y >= 1:
            if board[y - 1][x - 2] == n and board[y][x] == 0:
                return True
        if y <= len(board) - 2:
            if board[y + 1][x - 2] == n and board[y][x] == 0:
                return True
    #dreta
    if x <= len(board[y]) - 3:
        if y >= 1:
            if board[y - 1][x + 2] == n and board[y][x] == 0:
                return True
        if y <= len(board) - 2:
            if board[y + 1][x + 2] == n and board[y][x] == 0:
                return True
    return False


def knightstour(board, n, N):
    if n >= N:
        printboard(board)
        return True
    y = 0
    while y < len(board):
        x = 0
        while x < len(board[y]):
            if possible(board, x, y, n):
                board[y][x] = n+1
                if knightstour(board, n+1, N):
                    return True
                board[y][x] = 0
            x += 1
        y += 1
    return False


def main():
    n = int(input("Size of the board: "))
    board = [[0]*n for _ in range(n)]
    if knightstour(board, 0, n*n):
        pass
    else:
        print("impossible!")
    return


if __name__ == "__main__":
    main()