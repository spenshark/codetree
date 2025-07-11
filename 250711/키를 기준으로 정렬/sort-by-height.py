n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

class user:
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w
    
    def __str__(self):
        return f"{self.n} {self.h} {self.w}"

users = [user(name[i], height[i], weight[i]) for i in range(n)]

users.sort(key = lambda u : u.h)

for u in users:
    print(u)