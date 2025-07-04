n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def sequence(a, b):
    for i in range(n1):
        j = 0
        while(a[i]==b[j]):
            if(j == n2-1):
                return True
            if(i < n1-1 and j < n2-1):
                i += 1
                j += 1
            else:
                break

    return False

if(sequence(a, b)):
    print('Yes')
else:
    print('No')