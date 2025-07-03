a, b = map(int, input().split())
cnt = 0

def is_div_3(num):
    if(num // 10 % 3 == 0 or num % 10 % 3 == 0 or num % 3 == 0):
        return True

for i in range(a, b+1):
    if(is_div_3(i)):
        cnt += 1

print(cnt)