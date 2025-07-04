M, D = map(int, input().split())

year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def exist_day(M, D):
    if 1 <= M and M <= 12:
        if D <= year[M-1]:
            return True
    
    return False

if exist_day(M, D):
    print('Yes')
else:
    print('No')