with open("../data/notes.txt", "r") as file:
    line_index = 1
    for line in file:
        print(f"Line {line_index}: {line.strip()}")
        line_index += 1