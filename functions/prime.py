def prime(n):
    for i in range(2,n-1):
        if n% i == 0:
            return False
    return True

# use of __name to check if this is invoked as a module or main 
if(__name__ == '__main__'):
    num=int(input('Enter a number: '))
    result = prime(num)
    if result:
        print('number {} is a prime'.format(num))
    else:
        print('number {} is not a prime'.format(num))
        