N = int(input())

def temp(N):
    if N < 10:
        return N**2
    
    return temp(N//10) + (N%10)**2

print(temp(N))