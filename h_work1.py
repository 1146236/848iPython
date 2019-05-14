def main():
    lower= int(input("Enter lower number of limit: "))
    upper = int(input("Enter upper number of limit: "))
    for i in range(lower,upper+1):
        if(i %5 ==0 and i%7!=0):
            print (i)
main()
