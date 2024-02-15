list1 = [15, 9, 8, 2, 5, 33]
print("Original : ", list1)

list1.append(25)
print("After append : ",list1)
list2 = [6, 7]
list1.extend(list2)
print("After extend : ",list1)

list1.remove(15)
print("Remove 15 : ",list1)

list3 = list1[ : :-1]
print("Reverse list : ",list3)

list1.sort()
print("Ascending : ",list1)
list1.sort(reverse=True)
print("Descending : ",list1)

#B) List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana",
#"orange"]] From above list get word “orange” and “Python” & repeat this list five times
#without using loops.
List1 =[1,2,3,4,["python","java","c++",[10,20,30]],5,6,7,["apple","bana na","orange"]]

print("List1[8][2] : ",List1[8][2])

print("List1[4][0] : ",List1[4][0])

print("5 times : \n",List1*5)

#C) Create a list and copy it using slice function
list1 = [15, 9, 8, 2, 5, 33]
print("Original : ", list1)

list2 = list1[ : ]
print("Copied list : ",list2)


#D) Create a tuple and apply different types of mathematical operation on it (Sum, Maximum, minimum etc.).
tup = (5, 9, 22, 3, 10, 15)
print(tup)

print("Sum of elements : ",sum(tup))

print("Minimum element : ",min(tup))
print("Maximum element : ",max(tup))

print("Element at index 3 : ",tup[3])

print("Number of 5s : ",tup.count(5))
print("Index of 1st 5 :",tup.index(5))

print("\nIterate tuple elements :")
for i in tup:print(i,end = " ")