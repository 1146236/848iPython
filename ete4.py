string=input("Enter the text: ")
count1=0
count2=0
for i in string:
    if(i.isdigit()):
        count1=count1+1

    count2=count2+1

print("The number of numeral(s) is: ")

print(count1)
