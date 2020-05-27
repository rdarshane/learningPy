f=lambda x: x*x
print('''enter a 
number: ''')
n = int(input())
print("square of {} is {}".format(n,f(n)))

lst=[1,2,3,4,5,6,7,8,9]
evens=list(filter( lambda x: (x%2==0),lst))
print("even numbers {}".format(evens))   