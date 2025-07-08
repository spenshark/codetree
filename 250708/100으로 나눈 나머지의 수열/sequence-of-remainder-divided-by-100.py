N = int(input())

def temp(N):
    if N == 1:
        return 2
    elif N == 2:
        return 4
    else:
        return (temp(N-1) * temp(N-2)) % 100

print(temp(N))