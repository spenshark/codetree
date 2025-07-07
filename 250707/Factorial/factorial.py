N = int(input())

def fact(N):
    if N == 1:
        return 1

    return fact(N-1) * N

print(fact(N))