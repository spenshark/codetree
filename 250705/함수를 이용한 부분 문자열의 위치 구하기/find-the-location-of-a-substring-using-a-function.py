text = input()
pattern = input()

def sub_str():
    if(pattern in text):
        return text.index(pattern)
    else:
        return -1

print(sub_str())