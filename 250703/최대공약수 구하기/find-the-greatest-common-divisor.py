n, m = map(int, input().split())
max = 0

def gcd(n, m):
    if(n>m):
        if(m==0):
            return n
        return gcd(m, n%m)
    else:
        if(n==0):
            return m
        return gcd(n, m%n)

print(gcd(n, m))