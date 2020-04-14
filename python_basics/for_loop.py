# For loop iterates over a range or list/tuple/dictionary

for i in range(10):
    print(i)
print("----------even numbers------------")
for i in range(2,20,2): #print even numbers between 1 to 20(excluding 20)
    print(i)
print("------------Iterate list using list items----------------")

fruits = ["apple", "banana", "orange", "mango"]
for fruit in fruits:
    print(fruit)
    
print("------------Iterate list using index----------------")

for i in range(len(fruits)):
    print("Index {} value is {}".format(i, fruits[i]))
    
print("------------Iterate dictionary using index----------------")

city_pincode = {"Pune": 411014, "Mumbai": 400001, 100011:"Delhi"}

for key,value in city_pincode.items():
    print("Key {} has value {}".format(key, value))