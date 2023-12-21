# https://www.acmicpc.net/problem/1244

# 스위치 개수
N = int(input())
# 초기 스위치 [0,1,0,1,0,0,0,1]
switches = list(map(int, input().split()))
student_cnt = int(input())

for _ in range(student_cnt):
    gender, no = map(int, input().split())

    # 스위치 index는 받은 no - 1 이다.
    idx = no - 1
    # 남학생일 때
    if gender == 1:
        # idx 가 총 스위치 개수보다 작으면 반복
        while idx < N:
            # 스위치를 바꾼다. (켜져있으면 끄고 / 꺼져있으면 킨다)
            switches[idx] = 0 if switches[idx] else 1
            # 배수 처리
            idx += no
    # 여학생일 때
    else:
        # no를 바꾸고
        switches[idx] ^= 1
        side = 1
        # idx-side => L / idx+side => R 가 범위 안에 있고
        while 0 <= (idx - side) and (idx + side) < N:
            l_idx = idx - side
            r_idx = idx + side
            # L == R 일때만 넘어가기 (XOR 연산자 활용)
            if switches[l_idx] == switches[r_idx]:
                switches[l_idx] = switches[l_idx] ^ 1
                switches[r_idx] ^= 1
                side += 1
            # L != R 라면 그만
            else:
                break

for line_no in range(N // 20 + 1):
    start = line_no * 20
    end = (line_no + 1) * 20
    print(' '.join(map(str, switches[start:end])))
