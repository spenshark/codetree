n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

class student:
    def __init__(self, n, k, e, m):
        self.n = n 
        self.k = k
        self.e = e
        self.m = m
    
    def __str__(self):
        return f"{self.n} {self.k} {self.e} {self.m}"

students = [student(name[i], korean[i], english[i], math[i]) for i in range(n)]

students.sort(key = lambda x : (-x.k, -x.e, -x.m))

for stu in students:
    print(stu)