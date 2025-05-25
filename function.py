def greetings():
    name = input("enter your name:")
    age = int(input("enter your age:"))
    print(f"hello world! am {name}!")
    print(f"{age} years old")
    print("welcome to python programming")
    print("lets start coding")

greetings()



def user():
    name = input("enter your name:")
    age = int(input("enter your age:"))
    if age <= 12:
        print(f"hello {name}, you are minor")
    elif age > 12 and age <= 20:
        print(f"hello {name}, you are a teenager")
    elif age > 20 and age <= 50:
        print(f"hello {name}, you are an adult")
    elif age > 50 :
        print(f"hello {name}, you are a senior citizen")
    else:
        print(f"hello {name}, not yet born")

user()


def fibbonaci(n):
    x = 0
    y = 1
    print(x)
    print(y)
    for fibbonaci in range(n):
        z = y + x
        print(z)
        x = y
        y = z
        

fibbonaci(10)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def factorial_of_number():
    number = int(input("enter a number to find its factorial: "))
    result = factorial(number)
    print(f"the factorial of {number} is {result}")

factorial_of_number()

