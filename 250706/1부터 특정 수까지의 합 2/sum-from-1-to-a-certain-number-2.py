N = int(input())

def temp(N):
    if N<1:
        return 0
    
    return N + temp(N-1)

print(temp(N))