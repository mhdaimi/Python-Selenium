#write one line at a time
with open("sample_write_file.txt", "w") as file_obj:
    file_obj.write("Mumbai\n")
    file_obj.write("Pune")
    

#write all lines at a time
with open("sample_write_file.txt", "w") as file_obj:
    file_obj.writelines(["Mumbai\n", "Delhi\n", "Chennai\n"])


#read existing file, reverse content and write to same file
with open("sample_read_file.txt", "r") as reader:
    content = reader.readlines()
    
    with open("sample_read_file.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)
    