n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

astr = bstr = ""

for i in range(n1):
    astr += str(a[i])

for j in range(n2):
    bstr += str(b[j])    

if bstr in astr:
    print('Yes')
else:
    print('No')