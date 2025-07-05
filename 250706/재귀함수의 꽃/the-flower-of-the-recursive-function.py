N = int(input())

def temp(N):
    if N == 1:
        return

    print(N, end=' ')
    temp(N-1)
    print(N, end = ' ')

temp(N)