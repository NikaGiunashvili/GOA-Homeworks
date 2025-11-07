students = {
    "ნიკა": 100,
    "ანა": 92,
    "ლუკა": 78,
    "მარიამი": 95,
    "გიორგი": 88
}

highestpoints_student = max(students, key=students.get)

print("student with hightest points is:", highestpoints_student, "->", students[highestpoints_student])
