#reading all contents of an existing file
file_obj = open("sample_read_file.txt", "r")
print(file_obj.read())
file_obj.close()

#reading certain characters of an existing file
file_obj = open("sample_read_file.txt", "r")
print(file_obj.read(5))
file_obj.close()

#reading contents line by line of an existing file
file_obj = open("sample_read_file.txt", "r")
print(file_obj.readlines())
file_obj.close()

#reading contents one line at a time of an existing file
file_obj = open("sample_read_file.txt", "r")
print(file_obj.readline())
print(file_obj.readline())
file_obj.close()

#reading all content line by line and storing in a variable then iterating over it
with open("sample_read_file.txt", "r") as file_obj:
    all_data = file_obj.readlines() # reads and returns each line as an element of a list
i=1
for line in all_data:
    print("Line {} : {}".format(i,line))
    i += 1
    