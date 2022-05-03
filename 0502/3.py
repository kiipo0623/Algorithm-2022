from collections import defaultdict
def timechange(time):
    hour = int(time[0:2])*60
    minute = int(time[3:5])
    return hour+minute

def solution(fees, records):
    answer = []

    recorddict = defaultdict(list)
    carfees = defaultdict(int)
    last = timechange('23:59')

    # record 정리
    for r in records:
        time, num, inout = r.split()
        recorddict[num].append((inout, timechange(time)))

    # 차량 가격 조회
    for key, value in recorddict.items():
        value.sort(key = lambda x : (x[1]))
        sumtime = 0
        if len(value)%2 == 1:
            value.append(('OUT', last))

        for i in range(1, len(value), 2):
            sumtime += value[i][1] - value[i-1][1]

        print(key, sumtime)
        if sumtime<=fees[0]:
            carfees[key] = fees[1]

        else:
            plustime = sumtime - fees[0]
            if plustime%fees[2] == 0:
                pluscnt = plustime//fees[2]
            else:
                pluscnt = plustime//fees[2]+1
            carfees[key] = fees[1]+(pluscnt*fees[3])

    turn = list(carfees.keys())
    turn.sort()

    for c in turn:
        answer.append(carfees[c])

    return answer

print(solution(
[180, 5000, 10, 600],
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
))