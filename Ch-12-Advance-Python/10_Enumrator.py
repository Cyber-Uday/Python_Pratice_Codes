
l=[10,20,30,998,55]

index=0
#basic we run like this 
for item in l:
    print(f"THE INDEX OF {index} is :> {item}")
    index+=1

# same way we can do easily with ENUMRATOR >>>  so go on..!
print()
print("AFTE THE ENUMERATER>> ")
for newindex,item in enumerate(l):
    print(f"THE INDEX OF {newindex} is :> {item}")