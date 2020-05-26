def sum(a,b):
    return a+b;

print("Concatenation of two  strings: Hello and World is '{}'".format(sum("Hello, ","World")))

print("enter two numbers separated by space: ")

numbers = input().split()

a=int(numbers[0])
b=int(numbers[1])

print("sum of two numbers is {}".format(sum(a,b)))
