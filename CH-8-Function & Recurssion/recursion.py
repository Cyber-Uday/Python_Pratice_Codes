#recursion is basically reduce or code as well time and 
#recursion play very imp role while implement a factorial 

def Factorial(n):
    if(n==1 or n==0):
        return 1
    return n*Factorial(n-1)

n = int(input(print("Enter the Number :> ")))
result=Factorial(n)
print(f"The Factorial of {n} is:> ", result)