import csv

def compare_csv_files(file1, file2):
    with open(file1, 'r', newline='') as f1, open(file2, 'r', newline='') as f2:
        # Read CSV files
        csv_reader1 = csv.reader(f1)
        csv_reader2 = csv.reader(f2)

        # Extract data from CSV files
        csv_data1 = list(csv_reader1)
        csv_data2 = list(csv_reader2)

    # Initialize lists to store mismatched records
    mismatched_records_1_to_2 = []
    mismatched_records_2_to_1 = []

    # Compare each record in file1 with all records in file2
    for i, row1 in enumerate(csv_data1):
        found_match = False
        for row2 in csv_data2:
            if row1 == row2:
                found_match = True
                break
        if not found_match:
            mismatched_records_1_to_2.append((i + 1, row1))

    # Compare each record in file2 with all records in file1
    for i, row2 in enumerate(csv_data2):
        found_match = False
        for row1 in csv_data1:
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
    with open(file, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        return sum(1 for _ in csv_reader)

# Provide CSV files path that you want to compare
csv_file1 = r"C:\Users\xxxxxxx\Downloads\Input\inputfile.csv"
csv_file2 = r"C:\Users\xxxxxxx\Downloads\Output\outputfile.csv"

compare_csv_files(csv_file1, csv_file2)

# Print number of records in each CSV file
print(f"\nNumber of records in {csv_file1} is {count_rows(csv_file1)}")
print(f"Number of records in {csv_file2} is {count_rows(csv_file2)}")