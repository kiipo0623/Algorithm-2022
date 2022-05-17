import re
url_idx = dict() # 주소 : idx
idx_default = dict() # idx : 기본점수
idx_toidx = dict() # idx : [toidx1, toidx2..]
idx_fromidx = dict() # idx : [fromidx1, ...]
def simulate(word, page, idx):
    body_flag = False
    for line in page.split('\n'):
        line = line.strip()
        if line[:5] == '<meta':
            for word in line.split(' '):
                if word[:8] == 'content=':
                    print("this")
                    print(word)
                    pass
                    # print(re.findall('"([^"]*)"', word))



        if line[:7] == '<a href':
            pass
        if not body_flag and line == '<body>':
            body_flag = True

        if body_flag: # 문장마다 짤라서 확인 # ><태그 사이
            pass


def solution(word, pages):
    answer = 0
    for idx, page in enumerate(pages):
        simulate(word, page, idx)
    return answer

print(solution(
    'blind',
["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
))