a, b = map(int, input().split())

sum = 0

def is_Prime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    
    return True

for i in range(a, b+1):
    if(is_Prime(i)):
        sum += i

print(sum)
