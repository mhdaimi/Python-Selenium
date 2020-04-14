a = 10
b = 0

try:
    c = a/b
except ZeroDivisionError as e: #catching a specific exception
    print(e)
except Exception as p: # catching exception using general Exception class
    print(p)
finally:
    print("I will always be executed")
    

# raising user defined exception

if b ==0:
    raise Exception("value of b is zero")