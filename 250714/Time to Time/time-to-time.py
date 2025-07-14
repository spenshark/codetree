a, b, c, d = map(int, input().split())

if b>d:
    h = c - a - 1
    m = d + 60 - b
else:
    h = c - a
    m = d - b

print(h*60 + m)