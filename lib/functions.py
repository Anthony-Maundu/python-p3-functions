#!/usr/bin/env python3

def greet_programmer():
    print(f"Hello, programmer!")

greet_programmer()



def greet(name = "Naureen"):
    print(f"Hello, {name}!")

greet("Naureen")

     

def greet_with_default(name):
    print(f"Hello, {name}!")

greet_with_default("Programmer")
greet_with_default("Sunny")


def add(num1, num2):
    sum = num1 + num2
    print(sum)

add(1, 2)

def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2


result1 = halve(4)
print(result1)  

result2 = halve("two")
print(result2)  
