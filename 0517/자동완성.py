def solution(words):
    answer = 0
    N = len(words)
    words.sort()

    for idx, word in enumerate(words):
        if idx == 0: # 맨 앞인 경우 ( 앞이랑은 비교 불가)
            before, after = words[idx+1], words[idx+1]
        elif idx == N-1: # 맨 뒤인 경우 (뒤랑은 비교 불가)
            before, after = words[idx-1], words[idx-1]
        else:
            before, after = words[idx-1], words[idx+1]

        cnt = 0
        if len(before) < len(word):
            before = before + '!'*(len(word)-len(before))
        if len(after) < len(word):
            after = after + '!'*(len(word) - len(after))
        print(before, word, after)
        beforeflag, afterflag = True, True
        for i in range(len(word)): # 앞/뒤 따로 생각해줘야 함
            if beforeflag and before[i] == word[i]:
                cnt = i+1
            else:
                beforeflag = False
            if afterflag and word[i] == after[i]:
                cnt = i+1
            else:
                afterflag = False

        answer += min(cnt+1, len(word))
        print(word, cnt+1, len(word))
    return answer

print(solution(
# ["go","goo","gooo"]
# ["abc","def","ghi","jklm"]
# ["word","war","warrior","world"]
["aaaaa",
"aaaab",
"aaabb",
"aabbb",
"abbbb"]
))
