n, m = map(int, input().split())
A = list(map(int, input().split()))

def div_plus(m):
    sum = 0
    while m >= 1:
        sum += A[m-1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    
    return sum

print(div_plus(m))