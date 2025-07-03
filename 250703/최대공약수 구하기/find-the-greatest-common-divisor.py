n, m = map(int, input().split())
max = 0

def denominator(n, m):
    for i in range(1, n/2):
        for j in range(1, m/2):
            if(i==j and max < i):
                max = i

print(max)