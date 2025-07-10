secret_code, meeting_point, time = input().split()
time = int(time)

class spot:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time


spot1 = spot(secret_code, meeting_point, time)

print('secret code :', spot1.secret_code)
print('meeting point :',spot1.meeting_point)
print('time :',spot1.time)