def changetime(s):
    res = 0
    hh, mm, sec = s.split(':')
    ss, sss = sec.split('.')
    res += int(hh)*60*60*1000
    res += int(mm)*60*1000
    res += int(ss)*1000
    res += int(sss)
    return res

def solution(lines):
    answer = 0
    traffic = []

    for line in lines:
        _, time, dur = line.split()
        time = changetime(time)
        dur = int(float(dur[:-1])*1000)
        traffic.append([time-dur+1, time]) # traffic 안에는 전부 포함

    # 시작점 기준 1000초
    # 끝점 기준 1000초
    # 변경이 발생하는 곳들
    for start, _ in traffic: # 여기 기준으로 뒤로 1000초
        cnt = 0
        for check in traffic:
            if start <= check[0] < start+1000 or start <= check[1] < start+1000 \
                    or check[0] <= start <= check[1] or check[0] <= start+999 <= check[1]:
                cnt += 1

    for _, end in traffic: # 여기 기준으로 뒤로 1000초
        cnt = 0
        for check in traffic:
            if end <= check[0] < end + 1000 or end <= check[1] < end + 1000 \
                    or check[0] <= end <= check[1] or check[0] <= end + 999 <= check[1]:
                cnt += 1

        answer = max(answer, cnt)

    return answer

print(solution(
[
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
))