#A tuple is an immutable data type in python. 
#a = () # empty tuple 
#a = (1,) # tuple with only one element needs a comma 
a = (1,7,2,5,6,78,9,5) # tuple with more than one element

print(a.index(7))
#complier will get that element and find the index of that number which you pass

print(a.index(1))
print(a.index(2))

#here tuples also used for count() fun to count how many time perticular num occur

print(f"The Counting of the 5 is: > ",a.count(5))

