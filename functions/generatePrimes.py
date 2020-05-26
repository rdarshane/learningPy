from prime import *
'''This is using a prime function from prime.py module'''

def primeGen(n):
    c = 1
    for i in range(1, n+1):
        while(1):
            c+=1
            if(prime(c)==True):
                yield c
                break
            

n = int(input("Enter the numer of primes to be generated: "))

for i in primeGen(n):
    print("next prime number: {}".format(i))

