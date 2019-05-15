a=[]
n=int(input("Include number of elements: "))
for i in range(1,n+1):
    b=int(input("Enter element: "))
    a.append(b)
a.sort()
print("Largest element is: ",a[n-1])
