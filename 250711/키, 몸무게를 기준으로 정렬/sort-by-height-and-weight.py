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
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} {self.height} {self.weight}"

users = [user(name[i], height[i], weight[i]) for i in range(n)]

users.sort(key = lambda x : (x.height, -x.weight))

for u in users:
    print(u)