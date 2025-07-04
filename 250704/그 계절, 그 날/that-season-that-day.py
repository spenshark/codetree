Y, M, D = map(int, input().split())

def is_leap(Y):
    if Y % 4 == 0:
        if Y % 100 == 0 and Y % 400 != 0:
            return False
        return True
    return False


def last_day(Y, M):
    if M == 2:
        if is_leap(Y):
            return 29
        else:
            return 28
    elif M == 4 or M == 6 or M == 9 or M == 11:
        return 30
    else:
        return 31

def exist_day(Y, M, D):
    if 1 <= M and M <= 12:
        if D <= last_day(Y, M):
            return True
    
    return False

def season(Y, M, D):
    if(not exist_day(Y, M, D)):
        return -1
    
    if(M == 12 or M <= 2):
        return 'Winter'
    
    if(M <= 5):
        return 'Spring'
    
    if(M <= 8):
        return 'Summer'
    
    if(M <= 11):
        return 'Fall'

print(season(Y, M ,D))