lower=int(input("enter lower range limit: "))
upper=int(input("enter upper range limit: "))
n=int(input("enter the number to be divided by: "))
n==7
for i in range(lower,upper+1):
    if(i%n==0 and i%7!=0):
        print (i)

