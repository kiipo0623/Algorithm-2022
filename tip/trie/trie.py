root = {}

def insert(s):
    global root
    cur_node = root
    for c in s:
        if c not in cur_node:
            cur_node[c] = {}
        cur_node = cur_node[c]
    cur_node['*'] = s

def search(s):
    global root
    cur_node = root
    for c in s:
        if c in cur_node:
            cur_node = cur_node[c]
        else:
            return False
    if cur_node['*'] == s:
        return True
# ㅆㅂ
def startwith(s):
    cur_node = root
    words = []

    for p in s:
        if p in cur_node:
            cur_node = cur_node[p]
        else:
            return None

    current_node = list(cur_node.keys())
    next_node = []
    while True:
        for node in current_node:
            if node == '*':
                word.append(current_node['*'])
            next_node.append(node)
        if len(next_node) != 0:
            current_node = next_node
            next_node = []
        else:
            break
    return words


word_list = ["frodo", "front", "firefox", "fire"]
for word in word_list:
    insert(word)

print(startwith("fr"))

