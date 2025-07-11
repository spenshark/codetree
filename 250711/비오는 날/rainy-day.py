from operator import attrgetter

n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class pred:
    def __init__(self, d, dy, w):
        self.d = d
        self.dy = dy
        self.w = w

pred_list = [pred(date[i], day[i], weather[i]) for i in range(n)]

pred_list = sorted(pred_list, key=attrgetter('d'))

idx = 0
for i, pred in enumerate(pred_list):
    if pred.w == 'Rain':
        idx = i
        break

pred_answer = pred_list[i]
print(str(pred_answer.d), pred_answer.dy, pred_answer.w)