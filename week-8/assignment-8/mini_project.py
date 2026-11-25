import csv

try:
    with open("../data/messy_data.csv") as file:
        reader = csv.DictReader(file)
        clean_data = []
        skipped_data = []
        rows_attempted = 0
        for row in reader:
            rows_attempted += 1
            if None in row:
                skipped_data.append(f"Row {rows_attempted}: extra column detected - skipped")
                continue

            try:
                row["amount"] = float(row["amount"])
            except ValueError as e:
                skipped_data.append(f"Row {rows_attempted}: ValueError - {e}")
                continue
            except KeyError as k:
                skipped_data.append(f"Row {rows_attempted}: KeyError - {k}")
                continue
            clean_data.append(row)
        rows_parsed = len(clean_data)
        rows_skipped = rows_attempted - rows_parsed

    print(f"""=== CSV Report ===
Rows attempted: {rows_attempted}
Rows parsed: {rows_parsed}
Rows skipped: {rows_skipped}""")
    print("\nSkipped rows:")
    for message in skipped_data:
        print(message)
    print("\nClean data: ")
    for item in clean_data:
        print(f"{item["name"]} | {item["category"]} | ${item["amount"]:.2f}")
except FileNotFoundError:
    print(f"Error: File not found")