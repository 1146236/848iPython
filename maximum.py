a=[]
n=int(input("enter number of elements: "))
for i in range(1,n+1):
    b=int(input("enter element: "))
    a.append(b)
a.sort()
print("largest element is: ",a[n-1])
      
