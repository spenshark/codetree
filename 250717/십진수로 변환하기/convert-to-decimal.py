binary = input()

binarys = list(map(int, binary))

num = 0

for i in range(len(binary)):
    num = num * 2 + binarys[i]

print(num)
