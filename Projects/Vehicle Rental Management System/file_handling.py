import csv
# Read data from CSV file
def read_data(filename):
    data = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File not found")
    return data


# Write data into CSV file
def write_data(filename, data, fieldnames):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Add new record to CSV file
def append_data(filename, record):

    with open(filename, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=record.keys()
        )

        # Write header only when file is empty
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(record)