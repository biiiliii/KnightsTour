import pygame
from time import sleep


n = 5


WIDTH = n
HEIGHT = n
GRANDARIA_QUADRAT = (125-n*n)

# colors

blanc = (118,150,86)
negre = (0, 0, 0)
verd = (80, 255, 100)
vermell = (255, 0, 0)
blau = (0,191,255)

gris1 = (221, 224, 227)
gris2 = (238,238,210)

llistacolors = [negre, gris1, vermell, vermell, blau, verd]

# pantalla i font

screen = pygame.display.set_mode((WIDTH * GRANDARIA_QUADRAT, HEIGHT * GRANDARIA_QUADRAT))
pygame.display.set_caption('Knight Tour')
pygame.font.init()
font = pygame.font.SysFont('Arial', GRANDARIA_QUADRAT)
font2 = pygame.font.SysFont('Arial', 7)
screen.fill(negre)
pygame.display.flip()
pygame.init()

# rellotge
clock = pygame.time.Clock()

class Casella:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        linia = pygame.Rect(self.x * GRANDARIA_QUADRAT, self.y * GRANDARIA_QUADRAT, GRANDARIA_QUADRAT, GRANDARIA_QUADRAT)
        pygame.draw.rect(screen, self.color, linia)
        pygame.display.flip()

    def drawX(self):
        k = 20
        pygame.draw.aaline(screen, "black", (self.x * GRANDARIA_QUADRAT + k, self.y * GRANDARIA_QUADRAT + k), (GRANDARIA_QUADRAT-(GRANDARIA_QUADRAT / 2) + self.x * GRANDARIA_QUADRAT + k, GRANDARIA_QUADRAT-(GRANDARIA_QUADRAT / 2) + self.y * GRANDARIA_QUADRAT+ k))
        pygame.draw.aaline(screen, "black", (GRANDARIA_QUADRAT-(GRANDARIA_QUADRAT / 2) + self.x * GRANDARIA_QUADRAT + k, self.y * GRANDARIA_QUADRAT + k), (self.x * GRANDARIA_QUADRAT + k, GRANDARIA_QUADRAT-(GRANDARIA_QUADRAT / 2) + self.y * GRANDARIA_QUADRAT + k))
        pygame.display.flip()

    def drawKnight(self):
        k = 20
        for i in range(5):
            pygame.draw.aaline(screen, "red", (i + self.x * GRANDARIA_QUADRAT + k, self.y * GRANDARIA_QUADRAT + k), (GRANDARIA_QUADRAT-(GRANDARIA_QUADRAT / 2) + i + self.x * GRANDARIA_QUADRAT + k, GRANDARIA_QUADRAT-(GRANDARIA_QUADRAT / 2) + self.y * GRANDARIA_QUADRAT+ k))
            pygame.draw.aaline(screen, "red", (GRANDARIA_QUADRAT-(GRANDARIA_QUADRAT / 2) + i + self.x * GRANDARIA_QUADRAT + k, self.y * GRANDARIA_QUADRAT + k), (i + self.x * GRANDARIA_QUADRAT + k, GRANDARIA_QUADRAT-(GRANDARIA_QUADRAT / 2) + self.y * GRANDARIA_QUADRAT + k))
            pygame.display.flip()

def drawBoard():
    firstWhite = False
    taula = []
    for y in range(n):
        tmp = []
        if not firstWhite:
            firstWhite = True
            white = True
        else:
            firstWhite = False
            white = False
        for x in range(n):
            if white:
                tmp.append(Casella(x, y, blanc))
                white = False
            else:
                tmp.append(Casella(x, y, gris2))
                white = True
        taula.append(tmp)
    for linia in taula:
        for casella in linia:
            casella.draw()
    return taula


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

def knightstour(board, n, N, taulapygame):

    if n >= N:
        printboard(board)
        return True
    y = 0
    while y < len(board):
        x = 0
        while x < len(board[y]):
            if possible(board, x, y, n):
                taulapygame[y][x].drawKnight()
                sleep(0.1)
                taulapygame[y][x].draw()
                taulapygame[y][x].drawX()
                board[y][x] = n+1
                if knightstour(board, n+1, N, taulapygame):
                    return True
                board[y][x] = 0
                taulapygame[y][x].draw()
            x += 1
        y += 1
    return False

def main():
    #n = int(input("Size of the board: "))
    board = [[0]*n for _ in range(n)]
    taulapygame = drawBoard()
    if knightstour(board, 0, n*n, taulapygame):
        pass
    else:
        print("impossible!")
    return

if __name__ == "__main__":
    main()