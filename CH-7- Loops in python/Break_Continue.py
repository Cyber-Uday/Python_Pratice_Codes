
#using break statement we can stop the loop and implictly
print("Using Break Statement>> ")
for i in range(5):
    if(i==3):
        break
    print(i)
    
    # output = 0 1 2 bcz we add the statement to stop our program when i ==3 
    
#now we exploring the continue which stop and re start again 
# here we got output as :::::::: 0 1 2   4 bcz continue will stop that 3 and then print later
print("After Continue Statement>> ")
for i in range(5):
    if(i==3):
        continue
    print(i)
    