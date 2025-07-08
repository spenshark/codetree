N = int(input())

def temp(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        return temp(N//3) + temp(N-1)

print(temp(N))