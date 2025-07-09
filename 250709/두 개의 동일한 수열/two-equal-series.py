n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

flag = True

A.sort()
B.sort()

for i in range(n):
    if A[i] != B[i]:
        flag = False

if flag == True:
    print('Yes')
else:
    print('No')