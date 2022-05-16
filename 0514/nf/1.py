def solution(recruits, s1, s2):
    answer = []
    person = dict()
    junior, senior = [], []
    max_day, max_grade, min_day, min_grade = 0, 0, 101, 101

    for idx, recruit in enumerate(recruits):
        if recruit[0] > max_day: max_day = recruit[0]
        if recruit[0] < min_day: min_day = recruit[0]
        if recruit[1] > max_grade: max_grade = recruit[1]
        if recruit[1] < min_grade: min_grade = recruit[1]

        if recruit[0] >= s1 or recruit[1] >= s2:
            senior.append(idx)
            person[idx] = 'senior'
        else:
            junior.append(idx)
            person[idx] = 'junior'


    for e1 in range(min_day, max_day + 1):
        for e2 in range(min_grade, max_grade + 1):
            expert, senior, junior =



    return answer