# Dictionary stores a key:value pair

city_pincode = {"Pune": 411014, "Mumbai": 400001, 100011:"Delhi"}

print("Pincode of Pune is {}".format(city_pincode["Pune"]))
print("Size of dictionary -> {}".format(len(city_pincode)))

#Add new key:value pair
city_pincode["Aurangabad"] = 431001
print(city_pincode)

#Update value of existing Key
city_pincode["Pune"] = 411001
print(city_pincode)

#Remove a key:value pair
del city_pincode["Pune"]
print(city_pincode)