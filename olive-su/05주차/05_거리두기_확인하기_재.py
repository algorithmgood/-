# 통과 못함
# 정확성 : 23.9

def bfs(room, col, row):
    stack = []
    if col == 5 and row == 5:
        return 1
    elif row == 5:
        if bfs(room, col+1, 0) == 0:
            return 0
    else:
        # 우측 검사
        if room[col][row + 1]:
            if room[col][row + 1] == 'P': return 0
            stack.append(room[col][row + 1])
            if room[col][row + 2]:
                if room[col][row + 2] == 'P' and stack[0] == 'O': return 0
        # 하단 검사
        if room[col+1][row]:
            if room[col+1][row] == 'P': return 0
            stack.append(room[col+1][row])
            if room[col+2][row]:
                if room[col+2][row] == 'P' and stack[0] == 'O': return 0
        # 대각선 검사
        if room[col+1][row+1]:
            if room[col+1][row+1] == 'P' and stack == 'OO': return 0
            

def solution(places):
    answer = []
    for place in places:
        if bfs(place, 0, 0) == None:
            answer.append(1)
        else: answer.append(0)
    return answer
