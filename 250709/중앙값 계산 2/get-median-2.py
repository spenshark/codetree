n = int(input())
arr = list(map(int, input().split()))
newarr = []

for i in range(n):
    newarr.append(arr[i])
    if i%2 == 0:
        newarr.sort()
        print(newarr[i//2], end = ' ')