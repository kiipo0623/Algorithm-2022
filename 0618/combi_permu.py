def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 핵심 : used로 선택 여부를 확인하고, 전체 를 계속 돌려야 한다 순서가 있어서
    def generate(chosen, used):
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)

def combination(arr, r):
    arr = sorted(arr)

    # 중복과 무관하므로 해당 인덱스부터 확인하면 된다
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

        start = arr.index(chosen[-1])+1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()

    generate([])


permutation('ABCDE', 2)
combination('ABCDE', 2)