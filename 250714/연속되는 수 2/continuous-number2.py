n = int(input())
arr = [int(input()) for _ in range(n)]

max = 1
cnt = 0
for i in range(n):
    if i == 0 or arr[i] != arr[i - 1]:
        if cnt > max:
            max = cnt
        cnt = 0
    cnt += 1
    if i == n-1:
        if cnt > max:
            max = cnt

print(max)
