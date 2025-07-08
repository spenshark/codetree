n = int(input())
arr = list(map(int, input().split()))
lcm = 0

def gcd(a,b):
    if a % b == 0:
        return b
    
    return gcd(b, a%b)

def temp(n):
    global lcm

    if len(arr) == 1:
        lcm = arr[n-1]
        return

    if n == 1:
        return
    
    num1 = arr[n-1]
    num2 = arr[n-2]

    lcm = (num1 * num2) // gcd(max(num1, num2), min(num1, num2))
    arr[n-2] = lcm

    return temp(n-1)

temp(n)
print(lcm)