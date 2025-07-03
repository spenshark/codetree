n, m = map(int, input().split())

def abc(n, m):
    a = n
    b = m
    while(a != b):
        if(a > b):
            b += m
        else:
            a += n

    print(b)

abc(n, m)
