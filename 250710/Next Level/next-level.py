user2_id, user2_level = input().split()
user2_level = int(user2_level)

class user:
    def __init__(self, id='codetree', level=10):
        self.id = id
        self.level = level

user1 = user()
user2 = user(user2_id, user2_level)

print('user', user1.id, 'lv', str(user1.level))
print('user', user2.id, 'lv', str(user2.level))