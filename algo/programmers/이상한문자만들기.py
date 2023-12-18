def solution(s):
    idx = 0
    new_str = ''
    for char in s:
        # 공백문자일 경우 그대로 넣고 짝홀판별 idx 리셋
        if char == ' ':
            new_str += char
            idx = 0
            continue
        elif idx % 2:
            new_str += char.lower()
        elif idx % 2 == 0:
            new_str += char.upper()
        idx += 1

    return new_str

print(solution("try hello WORLD"))  # "TrY HeLlO WoRlD"