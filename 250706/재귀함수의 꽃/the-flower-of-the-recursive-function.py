N = int(input())

def temp(N):
    if N == 0:
        return

    print(N, end=' ')
    temp(N-1)
    print(N, end = ' ')

temp(N)