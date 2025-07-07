N = int(input())

def temp(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    if N % 2 == 0:
        return temp(N-2) + N
    else:
        return temp(N-2) + N

print(temp(N))