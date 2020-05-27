from prime import *
'''This is using a prime function from prime.py module'''

def primeGen(n):
    pr = 2
    cnt = 0
    while(1):
        if(prime(pr)==True):
            cnt+=1
            yield pr
        pr+=1
        if(cnt>=n):
            break
        
            

n = int(input("Enter the numer of primes to be generated: "))

for i in primeGen(n):
    print("next prime number: {}".format(i))

