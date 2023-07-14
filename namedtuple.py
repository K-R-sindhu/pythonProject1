
from collections import namedtuple
student_count = int(input())
attributes = input().split()
Student = namedtuple('Student', attributes)
total_marks = 0
for _ in range(student_count):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

average_marks = total_marks / student_count
print('{:.2f}'.format(average_marks))