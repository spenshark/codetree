a, b, c = map(int, input().split())

total_m = 0

m = b * 60 + c 

m11 = 11 * 60 + 11

if m > m11:
    day = a-11
    total_m = day * 1440 + m - m11
else:
    day = a - 11 - 1
    total_m = day * 1440 + m - m11 + 1440

print(total_m)