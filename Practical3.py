#A
str1 = "Meet"
str2 = "Vasava"

str3 = str1 + str2
print("Concatenate String : ",str3)

str4 = "D23CE155"
print("Length : ",len(str4))

str5 = "D23CE155@charusat.edu.in"
print("First element : ",str5[0])
print("Last element : ",str5[-1])

str6 = "Hello ! World"
str7 = str6[ : : -1]
print("Reverse String : ",str7)

#copying string

str8 = "This is No One."
str9 = str8[3:10]
print("Copying string : ",str9)

str10 = "Good Morning"
str11 = str10.replace('n','m')
print("Replacing a with b : ",str11)

str12 = "My name : Meet"
str13 = str12.upper()
str14 = str13.lower()
print("Upper case : ",str13)
print("Lower case : ",str14)

str15 = "Hello There!"
str16 = str15.split()
str17 = str15.split('!')
print("Split : ",str16)
print("Split : ",str17)

str18 = "I Attended Lecture Today."
print("Char in string : ",'k' in str18)
str19 = "Computer engineering"
print("Count of h : ",str19.count('e'))
str20 = "Bachelor of technology"
print("Find h : ",str20.find('h'))

#B
#Dictionary
#empty dictionary {}
dict1 = dict()
print("Empty dict : ",dict1)
dict2 = {155:"Meet", 148:"Vishnu", 166:"Het"}
print("\nDictionary 2 : ",dict2)

dict3 = dict2.copy()
print("\nDictionary 3 : ",dict3.items())

ele = dict2.pop(67)
print("\nElement popped: ",ele)
print("\nLast item popped : ",dict2.popitem())

print("\nKeys : ",dict2.keys())
print("Values : ",dict2.values())

dict4 = dict({177:"Vedant"})
dict4.update(dict2)
print("\nUpdated : ",dict4)

del dict4[177]
print("After deleting : ",dict4)
#merge 3 dictionaries
dict5 = {154:"Utsav"}
dict6 = dict({188:"Ravi"})
dict7 = {**dict2,**dict5,**dict6}
print("\nAfter merging 3 dictionaries : ",dict7)
#clear function
print("Clear function : ",dict7.clear())