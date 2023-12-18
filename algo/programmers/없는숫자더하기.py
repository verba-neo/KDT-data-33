# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    all_numbers = list(range(10))
    for num in numbers:
        all_numbers.remove(num)
    return sum(all_numbers)


def solution(numbers):
    answer = sum(range(10)) - sum(numbers)
    return answer


print(solution([1,2,3,4,6,7,8,0]))  # 14
print(solution([5,8,4,0,6,7,9]))  # 6