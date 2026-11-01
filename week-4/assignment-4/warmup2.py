student = {
    "name": "Minnie",
    "grade": "A",
    "subjects": ["Art", "Music", "Design", "Math"],
}
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")
student["graduated"] = False
print(student)
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")