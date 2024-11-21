#here we are going to explore the factorial Number >> 
#factorial number is like>> 5! like so incase 1*2*3*4*5 = 5! this way we can represent >> 

num = int(input(print("Enter the Number you want to make factorial> ")))
fact =1
for i in range(1,num+1):
            fact = fact*i
            
print(f"Factorial Number of {num} is :> ",fact)