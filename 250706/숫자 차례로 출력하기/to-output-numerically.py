n = int(input())

def temp(num):
    if num < 1:
        return

    print(n-num+1, end=' ')
    temp(num-1)
    if num == 1:
        print()
    print(n-num+1, end= ' ')


temp(n)