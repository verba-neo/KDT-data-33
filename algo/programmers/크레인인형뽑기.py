# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    stack = []

    # 인형 뽑기
    def pick(col):
        col -= 1
        # 한칸씩 밑으로 내려가며
        for row in range(len(board)):
            # 인형이 있으면 (0이 아니면)
            if board[row][col] != 0:
                # 인형을 뽑고
                doll = board[row][col]
                # 해당 칸을 비우고
                board[row][col] = 0
                # 인형을 return
                return doll
        # 줄 전체에 인형이 없으면 False return
        return False

    for move in moves:
        # 인형을 뽑아서
        doll = pick(move)
        # 인형이 있을 경우에만.
        if doll != False:
            # stack에 뭐라도 있고, 맨 위의 인형과 doll이 같다면
            if len(stack) != 0 and stack[-1] == doll:
                # 터뜨리고, answer를 올린다.
                stack.pop()
                answer += 2
            # 아니라면
            else:
                # stack에 쌓는다.
                stack.append(doll)

    return answer