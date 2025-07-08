a, b, c = map(int, input().split())

def temp(n):
    if n < 10:
        return n % 10
    
    return temp(n//10) + n%10

print(temp(a*b*c))