#List - Collection of different data types - MUTABLE
sample_list = ["Python", 3.8, "Programming"]

print("Item at index 0 -> {}".format(sample_list[0]))
print("Item at index 2 -> {}".format(sample_list[2]))
print("Length of list -> {}".format(len(sample_list)))

#Replace an existing value 
sample_list[2] = "Programming language"
print(sample_list)

# Insert a value in between index 0 and 1
sample_list.insert(1, "Inserted")
print(sample_list)

#Add value at end
sample_list.append(100)
print(sample_list)

# Get last value of list
print("Last value in list -> {}".format(sample_list[-1]))

# Get a range of items from list
print("Sublist of index range 0 to 3 -> {}".format(sample_list[0:3]))

#Delete or remove values from List
sample_list.remove(100)
del sample_list[0]
print(sample_list)

print("-------------------------****------------------------------")
