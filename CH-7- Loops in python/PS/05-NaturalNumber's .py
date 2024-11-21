#here we are making first 
#Write a program to find the sum of first n natural numbers using while loop.

num=int(input("ENter the number you want to sum::>> "))

'''for i in range(0,num+1):
    print(i)'''
    
i=0
sum=0
while(i<num):
    sum +=i
    i+=1

print(sum)