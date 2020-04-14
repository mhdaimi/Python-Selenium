#self is like this keyword in Java. self holds reference to the class

class Calculator:
    number = 100 #This is class variable
    
    #This method is like a constructor, used to initialize instance variables
    def __init__(self, number_1, number_2):
        self.num_1 = number_1
        self.num_2 = number_2
    
    def add(self):
        print("Addition of {} and {} is {}".format(self.num_1,self.num_2,self.num_1+self.num_2))
        
    def sub(self):
        print("Subtraction of {} and {} is {}".format(self.num_1,self.num_2,self.num_1-self.num_2))
        
    def mult(self):
        print("Multiplication of {} and {} is {}".format(self.num_1,self.num_2,self.num_1*self.num_2))
        
    def div(self):
        print("Division of {} by {} is {}".format(self.num_1,self.num_2,self.num_1/self.num_2))
        
    def add_number_to_class_variable(self, num):
        #class variables can only be accessed using the class name dot variable name
        print("Adding {} to class variable {}: result is {}".format(num,Calculator.number,num+Calculator.number))
        
        

#calc = Calculator(20,10) #creating object of class, passing two numbers as argument to constructor
#calc.add() #invoking add() method of class using object
#calc.div()
#calc.add_number_to_class_variable(100)