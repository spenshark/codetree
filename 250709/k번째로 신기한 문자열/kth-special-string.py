n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

str.sort()
cnt = 0

for i in str:
    if i.startswith(t):
        cnt += 1
        if cnt == 3:
            print(i)
            break

