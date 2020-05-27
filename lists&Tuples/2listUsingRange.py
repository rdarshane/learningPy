def printList(lst):
    print("Print list using for")
    for i in lst:
        print(i, ', ', end='')
    print()

def printwithWhile(lst):
    i=0
    print("Print list using while")
    while(i<len(lst)):
        print(i, ', ', end='')
        i+=1
    print()

# create list using range function 
# 0-9 consecutive numbers 

# range format [Start:End:Step]
# Step default = 1
# Start default = 0 
# End - end element is not included
print("==================================")
print("Integers from 0 to 9 (range max set to 10, step 1 default, start 0 default)")
lst1=list(range(10))
printList(lst1)
printwithWhile(lst1)

# integers from 5 to 9
print()
print("==================================")
print("Integers from 5 to 9 (step 1 default)")
lst2 = list(range(5,9))
printList(lst2)
printwithWhile(lst2)


#list operations 
print()
print("==================================")
print("List operations")
odds = list(range(1,10,2))
print()
print("odds: {}".format(odds))
evens = list(range(0,10,2))
print()
print("evens: {}".format(evens))

lst3= evens + odds

print("concatenated list : {}".format(lst3))

print() 
lst3.sort()
print("ordered list : {}".format(lst3))


print()
#append to list
lst3.append(10)
print("After appending 10: {}".format(lst3))

print()
#delete from list
del lst3[0]
print("After deleting 0th element: {}".format(lst3))


print()
#delete from list
lst3.remove(10)
print("After removing 10: {}".format(lst3))

print()
lst3.reverse()
#reversing the list
print("reverse of the list: {}".format(lst3))

#using -ve indexing
# 
print()
print("list access using -ve index in reverse order (of reversed list)") 
n= len(lst3)
i=-1
while i > n*-1:
    print(lst3[i])
    i-=1

# cloning list using [:]
clone = lst3[:]
print()
print("==================================")
print("Cloning using [:]")
print(clone)