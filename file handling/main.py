# file_obj = open("sample.txt", 'w')
# string = """Hi Hello
# This is rishitha
# today's topic is file handling"""
# file_obj.write(string)
# file_obj.close()

## opening a file in write mode
# file_obj = open("sample.txt", 'w')
# strings_list = ["welcome to file handling\n", 
#                 "this is write operation"]
# file_obj.writelines(strings_list)
# file_obj.close()

##opening file in read mode
# try:
#     file_obj = open("test.txt", 'w')
#     data = file_obj.read()
#     print(data)
# except Exception as e:
#     print(f"Something wrong: {e}")
# finally:
#      file_obj.close()

##opening file using 'with' keyword
##if we use "with" it closes by default

try:
    with open('sample.txt', 'r') as file_obj:
        data = file_obj.read()
        print(type(data))
        print(data[:10])
        print(data)
except Exception as e:
    print(f"Something wrong: {e}")

