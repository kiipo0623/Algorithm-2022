def solution(survey, choices):
    answer = ''
    counter = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    grade = [0, 3, 2, 1, 0, 1, 2, 3]

    for i in range(len(choices)):
        if choices[i] <= 3:
            counter[survey[i][0]] += grade[choices[i]]
        elif choices[i] == 4:
            continue
        elif choices[i] >= 5:
            counter[survey[i][1]] += grade[choices[i]]

    if counter["R"]>=counter["T"]:
        answer += "R"
    else:
        answer += "T"

    if counter["C"]>=counter["F"]:
        answer += "C"
    else:
        answer += "F"

    if counter["J"]>=counter["M"]:
        answer += "J"
    else:
        answer += "M"

    if counter["A"]>=counter["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer

print(solution(
["AN", "CF", "MJ", "RT", "NA"],
[5, 3, 2, 7, 5]
))