n = int(input())

students = list(map(int,input().split()))
students.sort()
midRangeStudents = students[n:3*n-n]

print(max(midRangeStudents) - min(midRangeStudents))