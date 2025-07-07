N = int(input())

def temp(N):

    if N==1:
        return 0

    if N % 2 == 0:
        return temp(N//2)+1
    else:
        return temp(N//3)+1

print(temp(N))