unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

class boomb:
    def __init__(self, u, w, s):
        self.u = u
        self.w = w
        self.s = s

boomb1 = boomb(unlock_code, wire_color, seconds)

print('code :', boomb1.u)
print('color :', boomb1.w)
print('second :', boomb1.s)