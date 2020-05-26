def modify(x):
    x=9
    print(x, id(x))
x=10
print(x, id(x))
modify(x)
print(x, id(x))