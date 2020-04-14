print("Welcome to " + "Python learning")

name = "Python 3.8"
print("We are learning " + name)

print("We are learning Python", 3.8)

name = "Python"
version = "3.8" #Version as string
print("We are using version " + version + " of " + name )

# Plus(+) operator works only with 2 strings

name = "Python"
version = 3.8 # Version as a float
# The following will give an error as we try to concatenate string with float
#print("We are using version " + version + " of " + name ) 
print("We are using version", version,  "of " + name )
print("We are using version %f of %s " %(version, name))

#Best way to concatenate different types of data is to use format method of string
print("We are using version {} of {}".format(version, name))

city = "Pune"
temperature = 38
print("The temperature of {} is {}".format(city, temperature))

