import sys
n = int(sys.stdin.readline())
cnt = [0] * (10001)
for _ in range(n):
    a = int(sys.stdin.readline())
    cnt[a] += 1 # 전체 수의 개수를 세줌

j = 1
while j < 10001:
    if cnt[j] == 0: # 0인 경우는 해당 숫자가 없는 경우니까 건너뜀
        j+=1
    else:
        sys.stdout.write(str(j) + '\n')
        cnt[j] -= 1 # 해당 숫자가 있는 만큼 반복을 해야하니까 -1을 해줌
