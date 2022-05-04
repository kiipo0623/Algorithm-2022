from collections import deque
def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = deque(new_id)
    leng = len(new_id)
    for _ in range(leng):
        now = new_id.popleft()
        if now.isalnum():
            new_id.append(now)
        elif now in ['-', '_', '.']:
            new_id.append(now)
    new_id = ''.join(list(new_id))
    # 3단계
    while ".." in new_id:
        new_id = new_id.replace('..', '.')
    # 4단계
    if len(new_id) and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 7
    if len(new_id) <= 2:
        last = new_id[-1]
        long = 3-len(new_id)
        new_id += last*long

    return new_id

print(solution(
"=.="
))