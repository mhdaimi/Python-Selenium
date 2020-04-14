#function declaration
def greet_me():
    print("Hello, How are you?")

#function declaration    
def square_of(number):
    print("Square of {} is {}".format(number, number*number))

def double_the_number(number):
    return 2*number

#calling the function
greet_me()
square_of(10)
double_of_number = double_the_number(100)
print(double_of_number)    
