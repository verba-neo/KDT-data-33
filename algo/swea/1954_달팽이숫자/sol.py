import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 시계방향    우  하  좌  상
    delta_rows = [0, 1, 0, -1]
    delta_cols = [1, 0, -1, 0]
    idx = 0

    row, col = 0, 0
    num = 1
    board = [[0] * N for _ in range(N)]

    while num < N ** 2:
        # 턴을 해야 한다면 (idx 0 ~ 3) 계속 반복
        idx = (idx + 1) % 4

        # 숫자를 채워야 한다면
        board[row][col] = num
        row = row + delta_rows[idx]
        col = col + delta_cols[idx]
        num += 1

    print(f'#{tc}')