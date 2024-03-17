def compare_tsv_files(file1, file2):
    # Read rows of both files into lists
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        rows1 = [line.strip().split('\t') for line in f1]
        rows2 = [line.strip().split('\t') for line in f2]

    # Initialize lists to store mismatched records
    mismatched_records_1_to_2 = []
    mismatched_records_2_to_1 = []

    # Compare each record in file1 with all records in file2
    for i, row1 in enumerate(rows1):
        found_match = False
        for j, row2 in enumerate(rows2):
            if row1 == row2:
                found_match = True
                break
        if not found_match:
            mismatched_records_1_to_2.append((i + 1, row1))

    # Compare each record in file2 with all records in file1
    for i, row2 in enumerate(rows2):
        found_match = False
        for j, row1 in enumerate(rows1):
            if row2 == row1:
                found_match = True
                break
        if not found_match:
            mismatched_records_2_to_1.append((i + 1, row2))

    # Print mismatched/additional records
    if mismatched_records_1_to_2 or mismatched_records_2_to_1:
        print(f"Mismatched/Additional records when {file1} is matched to {file2}")
        for row_num, row in mismatched_records_1_to_2:
            print(f"row {row_num}: {' | '.join(row)}")
        print(f"\nMismatched/Additional records when {file2} is matched to {file1}")
        for row_num, row in mismatched_records_2_to_1:
            print(f"row {row_num}: {' | '.join(row)}")
    else:
        print("No mismatched/additional records found.")

def count_rows(file):
    with open(file, 'r') as tsvfile:
        return sum(1 for _ in tsvfile)

# Provide CSV files path that you want to compare
tsv_file1 = r"C:\Users\xxxxxxx\Downloads\Input\inputfile.tsv"
tsv_file2 = r"C:\Users\xxxxxxx\Downloads\Output\outputfile.tsv"

compare_tsv_files(tsv_file1, tsv_file2)

# Print number of records in each TSV file
print(f"\nNumber of records in {tsv_file1} is {count_rows(tsv_file1)}")
print(f"Number of records in {tsv_file2} is {count_rows(tsv_file2)}")

