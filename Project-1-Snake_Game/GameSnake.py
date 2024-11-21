#here we are going to import random module as well a lot of more >> 

'''
    1 = snake 
    -1 = water
    0 - gun 
'''


import random

computer =random.choice([1,0,-1])
Youstr = input("ENter a Choice : ")
YouDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"gun"}#number's la sanke water game madhe convert karel >> 
you = YouDict[Youstr]

#by now we have 2 number's one is you and one is computer >>> 

print(f"You choose {reverseDict[you]} and computer Choose {reverseDict[computer]}")

if(computer == you):
    print("Game is Draw")
else:
    if(computer==1 and you==-1):
        print("You Lose ..!  ")
    
    elif(computer==-1 and you ==1):
        print("You Win ..!!")
    
    elif(computer==0 and you==1):
        print("You Lose ")
    
    elif(computer==0 and you==-1):
        print("YOU Lose ..! ")
    
    elif(computer==1 and you==0):
        print("You Win ")
    
    elif(computer==-1 and you==0):
        print("You Lose ")
    
    else:
        print("Invalid Input..! ")