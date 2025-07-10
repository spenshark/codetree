MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class user:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

users = [user(codenames[i], scores[i]) for i in range(MAX_N)]

min = 10000
cnt = 0

for i in range(MAX_N):
    if users[i].score < min:
        min = users[i].score
        cnt = i

print(users[cnt].codename, str(users[cnt].score))
