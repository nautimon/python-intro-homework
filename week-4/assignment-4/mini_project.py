students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
high_score = students[0]["score"]
top_name = students[0]["name"]
for student in students:
    if student["score"] > high_score:
        high_score = student["score"]
        top_name = student["name"]
print(f"Top scorer: {(top_name)} ({(high_score)}) ")

total_score = 0
total_students = len(students)
for student in students:
    total_score += student["score"]
average = total_score/total_students
print(f"Class average: {(average)}")

subject_set = set()
for student in students:
    subject_set.add(student["subject"])
print(f"Subjects offered: {(subject_set)}")

top_scorers_list = list()
for student in students:
    if student["score"] > 75:
        top_scorers_list.append(student["name"])
print(f"High Scorers: {(top_scorers_list)}")