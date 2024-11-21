import random

n=random.randint(1,100)
guess =1
a=-1
while(a!=n):
    a=int(input("Guess the Corect Number:> "))
    if(a>n):
        print("Lower Number please : ")
        guess+=1
    elif(a<n):
        print("HIGHER Number Please : ")
        guess+=1

print(f"You Guess Correct Number {n} In Number of Guesses: {guess}")