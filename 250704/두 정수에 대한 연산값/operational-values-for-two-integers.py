a, b = map(int, input().split())

def operation(a,b):
    if a>b:
        a += 25
        b *= 2
    else:
        b += 25
        a *= 2
    
    return a, b

a, b = operation(a, b)
print(a, b)