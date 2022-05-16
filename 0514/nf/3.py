def solution(n, trains, bookings):
    answer = 0
    train_house = [0] * (n+1)

    for train in trains:
        s, e, k = train
        for i in range(s, e+1):
            train_house[i] += k

    print(train_house)
    people_house = [0] * (n+1)
    for booking in bookings:
        a, b = booking
        flag, stop = True, -1
        for i in range(a, b):
            if people_house[i] < train_house[i]:
                people_house[i] += 1
            else:
                flag = False
                stop = i
                break
        if flag:
            answer += 1
        else:
            for i in range(a, stop):
                people_house[i] -= 1
    print(people_house)
    return answer
print(solution(
    5, [[1,5,2],[2,3,1]], [[1,5],[1,3],[2,5],[2,4],[2,4],[3,5],[4,5]]
))