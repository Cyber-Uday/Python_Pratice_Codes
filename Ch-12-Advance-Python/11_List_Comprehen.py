
#List Comprehension is an elegant way to create lists based on existing lists. 

#let's make the list and make it in the Square format..! 

mylist=[1,4,6,89]

""" squareList=[]
for item in mylist:
    squareList.append(item*item)
print (squareList) """

#yes we make it again efficient way..!>> 

squareList=[i*i for i in mylist]
print(squareList)
