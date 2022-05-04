from collections import deque
def solution(info, query):
    answer = []
    cache = [[] for _ in range(1<<6-1)]
    for i in info:
        cjp, bf, js, cp, grade = i.split()
        grade = int(grade)
        idx = 0

        if cjp == 'cpp':
            cjp = 0
        elif cjp == 'java':
            cjp = 1
        elif cjp == 'python':
            cjp = 2

        if bf == 'backend':
            bf = 0
        elif bf == 'frontend':
            bf = 1

        if js == 'junior':
            js = 0
        elif js == 'senior':
            js = 1

        if cp == 'chicken':
            cp = 0
        elif cp == 'pizza':
            cp = 1

        idx |= cjp<<3
        idx |= bf<<2
        idx |= js<<1
        idx |= cp<<0

        cache[idx].append(grade)

    for q in query:
        q = list(q.split())
        checklist = deque([])
        while 'and' in q:
            q.remove('and')
        cjp, bf, js, cp, grade = q
        grade = int(grade)
        if cjp == '-':
            checklist.append(0<<3)
            checklist.append(1<<3)
            checklist.append(2<<3)
        elif cjp == 'cpp':
            checklist.append(0<<3)
        elif cjp == 'java':
            checklist.append(1<<3)
        elif cjp == 'python':
            checklist.append(2<<3)

        leng = len(checklist)
        for _ in range(leng):
            c = checklist.popleft()
            if bf == '-':
                checklist.append(c|0<<2)
                checklist.append(c|1<<2)
            elif bf == 'backend':
                checklist.append(c|0<<2)
            elif bf == 'frontend':
                checklist.append(c|1<<2)

        leng = len(checklist)
        for _ in range(leng):
            c = checklist.popleft()
            if js == '-':
                checklist.append(c | 0 << 1)
                checklist.append(c | 1 << 1)
            elif js == 'junior':
                checklist.append(c | 0 << 1)
            elif js == 'senior':
                checklist.append(c | 1 << 1)

        leng = len(checklist)
        for _ in range(leng):
            c = checklist.popleft()
            if cp == '-':
                checklist.append(c | 0 << 0)
                checklist.append(c | 1 << 0)
            elif cp == 'chicken':
                checklist.append(c | 0 << 0)
            elif cp == 'pizza':
                checklist.append(c | 1 << 0)
        cnt = 0
        for c in checklist:
            for g in cache[c]:
                if g >= grade:
                    cnt += 1

        answer.append(cnt)
    return answer


print(solution(
["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
))