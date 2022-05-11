import sys
sys.setrecursionlimit(100000)
def solution(words, queries):
    answer = []
    counted = []
    rev_words = []

    for word in words:
        counted.append(len(word))
        rev_words.append(word[::-1])

    trie = make_trie({}, words)
    rev_trie = make_trie({}, rev_words)

    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            answer.append(counted.count(len(query)))
        elif query[0] == '?':
            answer.append(find_trie(rev_trie, query[::-1], len(query)))
        elif query[-1] == '?':
            answer.append(find_trie(trie, query, len(query)))

    return answer

def make_trie(trie, words):
    for word in words:
        cur = trie
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['!'].append(len(word))
            else:
                cur[w] = {}
                cur = cur[w]
                cur['!'] = [len(word)]
    return trie

def find_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['!'].count(length)
    elif query[0] in trie:
        count += find_trie(trie[query[0]], query[1:], length)
    return count

print(solution(
["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]
))