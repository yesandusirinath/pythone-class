#list 
#string 

age = 13 
print(f"age value is {age}")

ages = [14,17,11,44,23]
#neg
print(ages)
print (ages[2])
print (ages[4])
print (ages[-1])

#slicing 
print (ages[2:])
print (ages[1:3])
print (ages[::-1])

#modify
print(ages[0])
ages[0] = 16
print(ages[0])
print(ages[1])
ages[1] = "yesandu"
print(ages[1])
#element = input("Enter data: ")
#ages.append(element)
ages += ["xyz","abc"]

print(ages)
#pop : that removes the last element 
ages.pop()
print(ages)
ages.pop(2)
print(ages)
#also can use ages.remove("xyz") for this one you need to give the exact thing that need to remove or ages .remove(11) for this you need to the index 

# put someting secificaly in to the list 
ages.insert(1,"akash")
print(ages)

# how to find out that is soemthing is on the list if it is there it will say true and if it is not there it will say false
print("yesandu" in ages)

# how to find out what is the index of that spicific number or the word in the list 
print (ages.count(11))

# how to find the number of charater in the list or the lenght of the list 
print (len(ages))

#how to display the charactor individulvaly 
for i in range(len(ages)):
    print(ages[i]*10)
for element in ages:
    print(element*10)