string=input("enter string: ")
count1=0
count2=0
for i in string:
    if(i.isdigit()):
        count1=count1+1
        
    count2=count2+1

print("the number of digits is: ")
print(count1)
