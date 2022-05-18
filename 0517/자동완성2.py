class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node['*'] = s

    def search(self, s):
        cur_node = self.root
        depth = 1
        cnt = 1
        for c in s:
            if len(cur_node) > 1:
                cnt = depth # 이만큼 겹
            if c in cur_node:
                cur_node = cur_node[c]
                depth += 1

        if len(cur_node) > 1:
            return depth
        else:
            return cnt

def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
    print(trie.root)

    for word in words:
        print(min(trie.search(word), len(word)))
        answer += min(trie.search(word), len(word))
    return answer
