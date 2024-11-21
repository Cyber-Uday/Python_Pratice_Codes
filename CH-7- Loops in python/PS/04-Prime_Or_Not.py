#here we are going to explore the number is prime or not >> 

#number divide by itself or 1 then called it as prime 

n = int(input(print("Enter the number :> ")))

for i in range(2,n):
    if(n%i)==0:
        print("Number is not prime ")
        break
else:
        print("NUmber is Prime ")