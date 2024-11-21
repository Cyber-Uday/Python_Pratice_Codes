#here we need to find which is greatest number among the 3 which givin by the user>> 

num1 = int(input("Enter first Number:> "))
num2 = int(input("ENter 2nd Number :> "))
num3 = int(input("ENter 3rd Number:> "))



def Greatest_Num(num1,num2,num3):
    if(num1>num2 and num1>num3 ):
        print(f"Greates Number is : ",num1)
    elif(num2>num3 and num2>num1):
        print(f"Greatest Number is: ",num2)
    else:
        print("Greatest Number is :",num3)
        
Greatest_Num(num1,num2,num3)