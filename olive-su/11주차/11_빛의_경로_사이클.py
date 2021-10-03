# 통과 못함
# 테스트 케이스만 통과

def solution(grid):
    # 하, 좌, 상, 우
    # 사이클이 존재하는지 판단 어떻게?
    # 방향, 위치 동일할 경우 사이클이라 판단
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    answer, cycle = [], []
    row_len, col_len = len(grid), len(grid[0])
    for d in range(4):
        length = 0
        flag = 0
        i, j, start = 0, 0, d
        now = start # 현재 방향
        before = []
        while True:
            length += 1
            if (now, i, j) in cycle: # 이미 사이클 리스트에 있을 경우 탈출
                flag = 1
                break
            cycle.append((now, i, j))
            if grid[i][j] == 'L':
                if before == 'R':
                    now = (now + 1) % 4
                else:
                    now = (now - 1) % 4
            elif grid[i][j] == 'R':
                if before == 'L':
                    now = (now - 1) % 4
                else:
                    now = (now + 1) % 4
            # print('i', i, 'j', j, 'now', now, 'len', length)
            before = grid[i][j]
            i = abs((i + dy[now])) % row_len
            j = abs((j + dx[now])) % col_len

            # 되돌아 왔을 경우 반복문 탈출
            if i == 0 and j == 0 and now == start:
                break
        if flag:
            continue
        else:
            answer.append(length)
        answer.sort(reverse=True)


    return answer
