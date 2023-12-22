def solution(strings, n):
    answer = []
    new_strings = []
    for string in strings:
        new_strings.append(string[n] + string)

    new_strings = list(enumerate(new_strings))
    print(new_strings)
    print(list(sorted(new_strings, key=lambda s: s[1])))

    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
