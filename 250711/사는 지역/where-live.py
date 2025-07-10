from operator import attrgetter

n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)


class user:
    def __init__(self, n, s, r):
        self.n = n 
        self.s = s 
        self.r = r 

users = [user(name[i], street_address[i], region[i]) for i in range(n)]

users2 = sorted(users, key=attrgetter('n'), reverse=True)

user1 = users2[0]

print('name', user1.n)
print('addr', user1.s)
print('city', user1.r)