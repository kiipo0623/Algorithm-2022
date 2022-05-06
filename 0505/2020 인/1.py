def solution(numbers, hand):
    answer = ''
    pos = {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1 ,1), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2), 0:(3, 1)}
    Lrow, Lcol = 3, 0
    Rrow, Rcol = 3, 2

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            Lrow, Lcol = pos[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            Rrow, Rcol = pos[number]
        else:
            Ldis = abs(Lrow-pos[number][0]) + abs(Lcol-pos[number][1])
            Rdis = abs(Rrow-pos[number][0]) + abs(Rcol-pos[number][1])
            if Ldis<Rdis:
                answer += 'L'
                Lrow, Lcol = pos[number]
            elif Ldis==Rdis:
                if hand == "left":
                    answer += 'L'
                    Lrow, Lcol = pos[number]
                elif hand == "right":
                    answer += 'R'
                    Rrow, Rcol = pos[number]
            elif Ldis>Rdis:
                answer += 'R'
                Rrow, Rcol = pos[number]

    return answer