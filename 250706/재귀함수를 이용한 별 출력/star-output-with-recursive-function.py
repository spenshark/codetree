n = int(input())

def star(num):
    global n
    if num > n:
        return
    
    print('*' * num, end ='')
    print()
    star(num+1)

star(1)