m1, d1, m2, d2 = map(int, input().split())

day_of_the_weeks = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

cnt = 0

minute1 = minute2 = 0

for i in range(1, m1):
    minute1 += m1

minute1 += d1 # 월요일

for i in range(1, m2):
    minute2 += m2

minute2 += d2

if d1 > d2:
    cnt = (d1 - d2) % 7
elif d2 > d1:
    cnt = (d2 - d1) % 7
else:
    cnt = 2

cnt = cnt - 1 if cnt > 0 else cnt + 6

print(day_of_the_weeks[cnt])

