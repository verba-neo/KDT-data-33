# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    answer = 0
    for n in d:
        budget -= n
        if budget >= 0:
            answer += 1
        else:
            break

    return answer


print(solution([1,3,2,5,4], 9))  # 3
print(solution([2,2,3,3], 10))   # 4