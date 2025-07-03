a, b = map(int, input().split())
cnt = 0

def is_div_3(num):
    numstr = str(num)
    if('3' in numstr or '6' in numstr or '9' in numstr or num%3==0):
        return True

for i in range(a, b+1):
    if(is_div_3(i)):
        cnt += 1

print(cnt)