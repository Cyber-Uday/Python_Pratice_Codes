'''
8. Write a program to print the following star pattern: 
        * 
        ** 
        ***      for n = 3
'''
num = int(input("Enter The number:> "))
i=0
row=0
Star =1 
while(row<num):
    #for row 
    j=0
    while(j<Star):
        print("*")
        j+=1
    #for next row prep
    Star +=1
    row +=1
    print()
    