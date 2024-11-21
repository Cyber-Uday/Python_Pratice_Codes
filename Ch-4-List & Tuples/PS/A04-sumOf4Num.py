#Write a program to sum a list with 4 numbers. 

num=[]

a = int(input("ENter 1st Number: > "))
num.append(a)

b= int(input("ENter 2nd Number:> "))
num.append(b)

c= int(input("Enter 3rd Number:> "))
num.append(c)

d= int(input("ENter 4th Number:> "))
num.append(d)

print(sum(num))
#or
#print("The addition is:> ",(num[0]+num[1]+num[2]+num[3]))
