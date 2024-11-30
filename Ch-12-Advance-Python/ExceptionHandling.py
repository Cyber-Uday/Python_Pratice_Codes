#here we are going to explore the exception Handling in python ..!

""" try :
    a=int(input("Hey,Enter The valid Number pls:> "))
    print(f"BRROV..! YOU ENTER A VALID NUMBER:> {a} ")

except Exception as e:
    print(e)

print("THANK-YOu - THIS IS USER FRIENDLY MSG") """

#now we are going for exception with a perticular way..! 

#we handle the error depend's upon the the user input ..! so go on>> 

try:
    a=int(input("HEY ENTER 2 NUMBER FOR DIVISION >>> "))
    b=int(input("ENTER THE 2dn Number >> "))
    print("THE DIVISION IS:> ",(a/b))
except Exception as e:
    print("ERROR OCCUR",e)