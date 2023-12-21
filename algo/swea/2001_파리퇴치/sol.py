# swea/2001_파리퇴치/sol.py

import sys
# 이 파일의 입력(input())을 파일로 대체
sys.stdin = open('input.txt')


# Test Case 총 개수
T = int(input())

# 각 테스트 케이스 시작
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0

    # 전체 N * N 중에서 시작점
    for r_start in range(N-M+1):
        for c_start in range(N-M+1):

            # 파리채 한번 휘두르기 (M * M)
            total = 0
            for r in range(M):
                for c in range(M):
                    row, col = r_start + r, c_start + c
                    total += board[row][col]

            if total > maximum:
                maximum = total

    print(f'#{tc} {maximum}')
