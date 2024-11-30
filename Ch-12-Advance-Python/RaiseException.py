#we can raise up our program in sense stop and user friendly msg>> 

a=int(input("Enter the Number:> "))
b=int(input("ENTER the 2nd Number:> "))

if(b==0):
    raise ZeroDivisionError ("HEY Does not Enter the Zero")
else:
    print(f"THE DIVISION IS {a}/{b} is:> ",(a/b))