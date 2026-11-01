list_coding_languages1 = ["Python", "Javascript", "SQL", "Java", "C++"]
list_coding_languages2 = ["Typescript", "C#", "SQL", "Rust", "Python"]

coding_languages1 = set(list_coding_languages1)
coding_languages2 = set(list_coding_languages2)

print(coding_languages1.union(coding_languages2))
print(coding_languages1.intersection(coding_languages2))
print(coding_languages1.difference(coding_languages2))

