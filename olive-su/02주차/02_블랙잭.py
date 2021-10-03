'''
Brute Force Algorithm
Card 1 + Card 2 + Card 3 의 최댓값
'''
import sys
limit_num = int(list(sys.stdin.readline().split())[1])
a = list(sys.stdin.readline().split())
a = list(map(int, a))
max_value = 0
for i in range(len(a) - 2): # 첫번째 숫자
    for j in range(i + 1, len(a) - 1): # 두번째 숫자
        for k in range(j + 1, len(a)): # 세번째 숫자
            value = a[i] + a[j] + a[k]
            if value <= limit_num:
                max_value = max(value, max_value)
print(max_value)
