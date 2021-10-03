# 통과 못함
# 정확성 : 22.2

def solution(N, number):
    old = [N]
    cnt = 1
    while True:
        cnt += 1
        if cnt > 8:
            return -1
        new = []
        for i in old:
            new.append(int(str(N) * cnt))
            if i + N > 0:
                new.append(i + N)
            if new[-1] == number:
                return cnt
            if i - N > 0:
                new.append(i - N)
            if new[-1] == number:
                return cnt
            if i * N > 0:
                new.append(i * N)
            if new[-1] == number:
                return cnt
            if i // N > 0:
                new.append(i // N)
            if new[-1] == number:
                return cnt
        old = new
