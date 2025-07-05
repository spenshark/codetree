n = int(input())

def temp(n):
    if(n==0):
        return
    print("HelloWorld")
    temp(n-1)

temp(n)