def isPrime(num):
    if(num==2):
        return True
    for fact in range(2,(num//2)+1):
        if(num%fact==0):
            return False
    return True
minRange= int(input("Enter MinRange:"))
maxRange=int(input("Enter MaxRange:"))
PrimeCounter=0
CompositeCounter=0
for num in range(minRange,maxRange+1):
    if (isPrime(num)):
        print(num,"is Prime Number")
        PrimeCounter+=1
    else:
        print(num,"is Composite Number")
        CompositeCounter+=1
print("There are",PrimeCounter,"Prime numbers","and",CompositeCounter,"Composite numbers")