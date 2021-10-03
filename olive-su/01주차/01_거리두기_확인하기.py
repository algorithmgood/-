# 정확성 23.9 / 런타임 에러

def solution(places):
    answer = []
    invalid = 0
    for i in range(5): # 맵 하나 읽어옴
        p_distance = []
        invalid = 0
        for y in range(5): # 한 줄 읽어옴
            for x in range(5):
                if places[i][y][x] == 'P':
                    p_distance.append((x, y)) # 'P'의 좌표값 저장 / x, y : 현재 위치
                    for person in p_distance:
                        manhattan_dis = abs(person[0] - x) + abs(person[1] - y)
                        if manhattan_dis:
                            if manhattan_dis == 1:
                                print(0, i, y, x)
                                print(places[i][y][x])
                                print(p_distance)
                                answer.append(0) # 정답 배열에 0추가
                                i, y, x = i + 1, 0, -1
                                p_distance = [] # 초기화
                                invalid = 1
                                break
                            elif manhattan_dis == 2:
                                if person[0] == x: # 2칸 위
                                    if places[i][y-1][x] != 'X':
                                        answer.append(0)
                                        i, y, x = i + 1, 0, -1
                                        p_distance = []
                                        invalid = 1
                                        break
                                elif person[0] == x - 2: # 2칸 왼
                                    if places[i][y][x-1] != 'X':
                                        answer.append(0)
                                        i, y, x = i + 1, 0, -1
                                        p_distance = []
                                        invalid = 1
                                        break
                                elif person[0] == x - 1: # 북서
                                    if places[i][y-1][x] != 'X' or places[i][y][x-1] != 'X':
                                        answer.append(0)
                                        i, y, x = i + 1, 0, -1
                                        p_distance = []
                                        invalid = 1
                                        break
                                else : # 북동
                                    if places[i][y-1][x] != 'X' or places[i][y][x+1] != 'X':
                                        answer.append(0)
                                        i, y, x = i + 1, 0, -1
                                        p_distance = []
                                        invalid = 1
                                        break
            if invalid != 1 and y == 4:
                answer.append(1)
                # 맵 하나 다 돎
                
    return answer
