n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

str.sort()
cnt = 1

for i in str:
    if i.startswith(t):
        if cnt == 3:
            print(i)
            break
        else:
            cnt += 1

