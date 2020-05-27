#list with integer numbers 
num=[1,2,3,4,5]
#print whole lst 
print ("Complete numbers List {}".format(num))

print("First=%d, Last=%d" %(num[0], num[4]))

print() #newline
#exception
#
try:
    print (num[5])
except IndexError:
    print("exception: Index out of range")

print() #newline
#list with strings
strs=["first", "second", "third", 'fourth', "fifth"]
#print whole lst 
print ("Complete strings List:{} ".format(strs))

print("First=%s, Last=%s" %(strs[0], strs[4]))

# list with mixed type values 


mixed=["first", 1, "second", 2, "third", 3]
print()
#print whole lst 
print ("Complete mixed List: ")
print (mixed)

print() #newline
print("Elemets of mixed List:")

for i in mixed: 
    print(i)




