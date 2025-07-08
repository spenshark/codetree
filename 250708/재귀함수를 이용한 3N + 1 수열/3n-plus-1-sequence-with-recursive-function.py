n = int(input())

def temp(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return temp(n / 2) + 1
    else:
        return temp(3*n + 1) + 1
    

print(temp(n))
