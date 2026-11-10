#WRITING FUNCTION
def welcome():
 print("Welcome to Python programming")

welcome() 

#PARAMETER
def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

greet("ekemini")

#RETURN VALUE
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)

#SCOPE
#the code will print NameError means while the  (age) is
#is tries to access outside the function


def show():
    age = 20

show()
print(age)
