a, b = map(int, input().split())

def onjeonsu(a):
    if a%2==0:
        return 0
    elif a%10==5:
        return 0
    elif a%3==0 and a%9!=0:
        return 0
    else:
        return 1

cnt = 0

for i in range(a, b+1):
    cnt += onjeonsu(i)

print(cnt)