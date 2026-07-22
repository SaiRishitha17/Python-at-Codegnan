import csv

# try:
#     with open("users.csv", "w", newline = "") as file:
#         writer = csv.writer(file)
#         writer.writerows([["Id","Name","Age"],
#                          ["1", "Ravi", 20],
#                          ["2","seetha",30]])
# except Exception as e:
#     print(f"something wrong: {e}")

##reading csv filecontent
try:
    with open("users.csv", "r", newline = "") as file:
        reader = csv.reader(file)
        print(reader)
        for row in reader:
            print(row)
except Exception as e:
    print(f"something wrong: {e}")