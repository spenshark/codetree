y = int(input())

def leaf_year(y):
    if(y % 4 == 0):
        if(y % 100 == 0 and y % 400 != 0):
            print('false')
        print('true')

leaf_year(y)