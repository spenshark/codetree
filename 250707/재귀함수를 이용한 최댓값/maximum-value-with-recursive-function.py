n = int(input())
arr = list(map(int, input().split()))

def temp(n, m):
    if n < 1:
        return m
    
    if arr[n-1] > m:
        m = arr[n-1]

    return temp(n-1, m)

print(temp(n, 0))