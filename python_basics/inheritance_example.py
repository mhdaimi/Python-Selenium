# we will inherit from Calculator class
from python_basics.oops_example import Calculator

# You need to mention the name of parent class in bracket
class Newcalculator(Calculator):
    #child class constructor
    def __init__(self, num1, num2):
        super(Newcalculator, self).__init__(num1,num2) #Parent class has a parameterized constructor, it needs to be invoked first
        self.num1 = num1
        self.num2 = num2
        
    #Overriding add method of parent class    
    def add(self):
        addition = self.num1+self.num2
        print("Addition of {} and {} is {}".format(self.num1, self.num2, addition))
        
    def modulus(self):
        mod = self.num1%self.num2
        print("Modulus of {} by {} is {}".format(self.num1, self.num2, mod))
        

new_calc = Newcalculator(50,40)
new_calc.add()
new_calc.mult() #calling mult method of parent class
new_calc.modulus()