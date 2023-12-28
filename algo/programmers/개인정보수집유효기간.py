def solution(today, terms, privacies):
    def time_convert(t):
        year, month, day = map(int, t.split('.'))
        return year * 12 * 28 + month * 28 + day

    term_dict = dict()
    today = time_convert(today)
    answer = []

    for term in terms:
        name, period = term.split()
        term_dict[name] = int(period) * 28

    for idx, privacy in enumerate(privacies):
        start, name = privacy.split()
        end = time_convert(start) + term_dict[name]
        if end <= today:
            answer.append(idx + 1)

    return answer


