a, b = map(int, input().split())

def prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return 0

    if (num//10+num%10) % 2 ==0:
        return 1
    else:
        return 0
            

cnt = 0
for i in range(a, b+1):
    cnt += prime(i)
            
print(cnt)