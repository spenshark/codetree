a, b, c = map(int, input().split())

def temp(n):
    if n < 10:
        return 0
    
    return temp(n//10) + n%10

print(temp(a*b*c))