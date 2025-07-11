num = 5
name = []
height = []
weight = []

for _ in range(num):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

class user:
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w

    def __str__(self):
        return f"{self.n} {self.h} {self.w:.1f}"


users = [user(name[i], height[i], weight[i]) for i in range(num)]

users.sort(key = lambda x : x.n)
print('name')
for u in users:
    print(u)

print()
print('height')
users.sort(key = lambda x : -x.h)
for u in users:
    print(u)
