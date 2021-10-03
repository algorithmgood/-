# 통과 못함
# 정확성 : 32.1

def solution(relation):
    col_len, row_len = len(relation[0]), len(relation)
    relation_dic = {}
    candidate_key = []
    # 딕셔너리 리스트 형태로 생성
    for i in range(col_len):
        relation_dic['col_' + str(i)] = []
    print(relation_dic)
    # 딕셔너리 리스트에 모든 항목 삽입
    for rel in relation:
        for j in range(col_len):
            relation_dic['col_' + str(j)].append(rel[j])
    print(relation_dic)
    
    for k in range(col_len):
        flag = 0
        candidate = ''
        temp = ['' * i for i in range(row_len)]
        # 첫 줄은 무조건 k 값으로 고정
        candidate += 'col_'+str(k)+' '
        for m in range(row_len):
            temp[m] += relation_dic['col_'+str(k)][m]
        # target이 되는 col 선택 (꼭 포함되어야하는 col)
        for l in range(k + 1, col_len):
            candidate += 'col_'+str(l)+' '
            for m in range(row_len):
                temp[m] += relation_dic['col_'+str(l)][m]
            if len(set(temp)) == row_len:
                flag = 1
                candidate_key.append(candidate)
                break
        if flag:
            continue
    
    candidate_key.reverse()
    candidate_key.sort(key=len)
    
    print(candidate_key)
    
    answer = []
    for c in candidate_key:
        flag = 0
        for a in answer:
            if a in c:
                flag = 1
                break
        if flag:
            continue
        answer.append(c)
    
    return len(answer)
