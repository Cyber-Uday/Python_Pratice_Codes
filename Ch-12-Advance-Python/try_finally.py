#here we are going with finally with exception

try:
    a=int(input("ENTER THE NUMBER:> "))
    print(a)

except Exception as e:
    print(e)
    
finally:
    print("HEY I AM FINAL BLOCK")
    
#now the question is if we try to finally method then same work was done by print even program wrong 

print ("HEY I AM OnlY PRINT ")
#then why should we need to use the finally method ..! 

#but the Ans is >> while you are in function 

#exp 2:> 

def FunA():
    try:
        a=int(input("ENtER THE NUMBER: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    #even if you return the finnaly said may try block ka part hu may chal kar he rahunga
    finally:
        print("HEY I AM FINALLY ..!")
    
    print("HEY I AM INSDIE THE FUN")#this willl not print bcz on upper side we do return
    

FunA()