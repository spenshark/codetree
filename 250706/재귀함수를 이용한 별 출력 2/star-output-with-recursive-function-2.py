n = int(input())

def star(n):
    if n<1:
        return 
    
    print('* ' * n)
    star(n-1)
    print('* ' * n)

star(n)
    
