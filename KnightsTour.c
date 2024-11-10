#include <stdio.h>
#include <stdbool.h>
#include <time.h>

#define N 8

void printboard(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

bool possible(int board[N][N], int x, int y, int n) {
    if (y >= 2) {
        if (x >= 1 && board[y - 2][x - 1] == n && board[y][x] == 0) {
            return true;
        }
        if (x <= N - 2 && board[y - 2][x + 1] == n && board[y][x] == 0) {
            return true;
        }
    }
    if (y <= N - 3) {
        if (x >= 1 && board[y + 2][x - 1] == n && board[y][x] == 0) {
            return true;
        }
        if (x <= N - 2 && board[y + 2][x + 1] == n && board[y][x] == 0) {
            return true;
        }
    }
    if (x >= 2) {
        if (y >= 1 && board[y - 1][x - 2] == n && board[y][x] == 0) {
            return true;
        }
        if (y <= N - 2 && board[y + 1][x - 2] == n && board[y][x] == 0) {
            return true;
        }
    }
    if (x <= N - 3) {
        if (y >= 1 && board[y - 1][x + 2] == n && board[y][x] == 0) {
            return true;
        }
        if (y <= N - 2 && board[y + 1][x + 2] == n && board[y][x] == 0) {
            return true;
        }
    }
    return false;
}

bool knightstour(int board[N][N], int n) {
    if (n >= N * N) {
        printboard(board);
        return true;
    }
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            if (possible(board, x, y, n)) {
                board[y][x] = n + 1;
                if (knightstour(board, n + 1)) {
                    return true;
                }
                board[y][x] = 0;
            }
        }
    }
    return false;
}

int main() {
    int board[N][N] = {0}; 
	clock_t start, end;
	double cpu_time;

	start = clock();
    if (knightstour(board, 0)) {
		end = clock();
		cpu_time = ((double) (end - start)) / CLOCKS_PER_SEC;

		printf("Execution time: %f seconds\n", cpu_time);
    } else {
        printf("Impossible!\n");
    }

    return 0;
}