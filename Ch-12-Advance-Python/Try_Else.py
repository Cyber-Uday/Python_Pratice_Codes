
try:
    a=int(input("ENTER THE VALID NUMBER:> "))
    print(a)
except Exception as e:
    print(e)
else:#if try block sucessfully run then it will go in else block otherwise not
    print("I AM INSIDE THE A ")