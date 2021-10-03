def solution(name):
    answer = 0
    name = list(name) # 리스트로 바꿈
    if name[1] == 'A': # 두번째 문자가 'A'일때 첫번째 문자만 놔두고 reverse 시행
        name.append(name.pop(0))
        name.reverse()
        answer -= 1
    for i in range(len(name)):
        if i > 0 and name[i-1] == 'A' and name[i] == 'A': continue
        if ord(name[i]) < ord('N'):
            answer += (ord(name[i]) - ord('A'))
        else:
            answer += abs(ord(name[i]) - ord('Z')) + 1
        answer+=1
    return answer - 1
