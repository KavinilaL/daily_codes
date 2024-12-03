#using function
a=int(input("enter a number:"))
b=int(input("enter a number:"))
def add_function():
    print(a+b)
add_function()

#built in function
a=int(input("number1:"))
b=int(input("number2:"))
def big(a,b):
    return max(a,b)
print(big(a,b))

#vote elligibility using function
age=int(input("Enter your age:"))
def vote_elligible(age):
    if age>=18:
        return "elligible"
    elif age<=18:
        return "not elligible"
    else:
        return "invalid input"
print(vote_elligible(age))

#default arugument function
def age(age=19):
    return age
print(age())

#function without parameter with return statement
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
def add():
    return a+b
print(add())


#function with parameter with return statement
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
def add(a,b):
    return a+b
print(add(a,b))

#function without parameter and without return statement
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
def add():
    result_1 = a+b
    print(result_1)
print(add())

#function with parameter and without return statement
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
def add(a,b):
    result = a+b
    print(result)
print(add(a,b))

# code with except and try:
try:
    age=int(input("Enter your age:"))
    def vote_elligible(age):
        if age>=18:
            return "elligible for votting"
        else:
            return "not elligible for votting"
    print(vote_elligible(age))
except(ValueError):
    print("Enter numbers only.....!!! ")





