n = int(input())
arr = list(map(int, input().split()))

def abs_arr(arr):
    for i in range(n):
        arr[i] = abs(arr[i])

abs_arr(arr)
for i in range(n):
    print(arr[i], end=' ')
