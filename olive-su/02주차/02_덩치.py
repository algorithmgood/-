'''
Brute Force Algorithm
'''
import sys

n = int(sys.stdin.readline().rstrip())
profile, answer = [], []
for i in range(n): # 각 사람의 프로필 정보 받아옴
    person = sys.stdin.readline().rstrip().split()
    profile.append((int(person[0]), int(person[1])))

for j in range(n): # 현재 비교하려는 사람의 키, 몸무게
    rank = 1 # rank 초기화
    for k in range(n): # 현재 사람(j)보다 키, 몸무게가 큰 사람이 있으면 rank + 1
        if profile[k][0] > profile[j][0] and profile[k][1] > profile[j][1]:
            rank += 1
    answer.append(rank) # answer 리스트에 해당 사람의 rank 정보 추가

print(' '.join(list(map(str, answer))))
