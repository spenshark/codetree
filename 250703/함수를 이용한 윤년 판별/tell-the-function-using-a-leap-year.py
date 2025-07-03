y = int(input())

def leaf_year(y):
    if(y % 4 == 0):
        if(y % 100 == 0 and y % 400 != 0):
            return False
        return True

if(leaf_year(y)):
    print('true')
else:
    print('false')