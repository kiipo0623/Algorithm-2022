def solution(files):
    lst = []
    for idx, file in enumerate(files):
        length = len(file)
        headcut, numbercut = -1, -1
        for i in range(length):
            if headcut == -1 and file[i].isdigit():
                headcut = i
            if headcut != -1 and not file[i].isdigit():
                numbercut = i
                # 여기서 다섯개 넘으면 잘라야 함
                break
        if numbercut == -1: numbercut = length

        H, N = file[:headcut].lower(), file[headcut:numbercut]
        print(H, N)
        lst.append([H, int(N), idx, file])
    lst = sorted(lst, key = lambda x : (x[0], x[1], x[2]))

    answer = [i[3] for i in lst]
    return answer

print(solution(
["F-15"]
))