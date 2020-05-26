moves=0
def towers(n, a, c, b):
    global moves
    if n==1:
        print("Move disk %i from %s to pole %s" %(n, a,c))
        moves+=1
    else:
        towers(n-1, a,b,c)
        moves+=1
        print("Move disk %i from %s to pole %s" %(n, a, c))
        towers(n-1, b,c,a)

n=int(input("enter number of disks: "))
towers(n, 'A', 'C', 'B')

print("required steps {}".format(moves))