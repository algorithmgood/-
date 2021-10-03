'''
Greedy Algorithm
'''
import sys

cnt = 0
x = list(sys.stdin.readline().split())
num, goal = int(x[0]), int(x[1])
coin = []
for _ in range(num): # 동전 리스트 받아옴
    input = int(sys.stdin.readline())
    if input <= goal: # 동전이 목표 금액보다 작은 경우에만 리스트에 추가
        coin.append(input)
while goal:# 오름차순이니까 맨 뒤 동전부터 비교
    cnt += goal // coin[-1] # 동전 개수 추가
    goal -= coin[-1] * (goal // coin.pop()) # pop과 동시에 목표 금액 줄이는 작업 수행
print(cnt)
