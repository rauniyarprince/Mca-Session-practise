#calculate the length of string

name = input("enter the name here: ")
print("your name length is: ",len(name))
print("\n")

#Display charcters using positive and negative indexing 

print("Displaying char using indexing:\n")
adress = "Gorakhpur"
print("Negative indexxing:",adress[-1])
print("Positive indexing",adress[6])

#Extract a substring using slicing.

print("using slicing:\n")
name = "prince rauniyar"
print(name[0:3])
print(name[:2])
print(name[:-1])
print(name[-1:-4])

#split the string into word and join the words using a separator
sequence= "prince rauniyar i am from the GKP"
print(sequence)
SplitW = sequence.split()
print("spliting sequence:\n",SplitW)
JoinW = " ".join(SplitW)
print("After join sequence:",JoinW)

#Convert the string into uppercase,lowercase and title case.

print("Using function:\n")
print("upper letter:" ,name.upper())
print("lower letter:",name.lower())
print("titlecase:", name.title())

#Find a specific word/char and replace it with another word/char.

print("find a specific word:\n")
Data = "i am currently completed BCA"
FindW = Data.replace("Currently completed BCA","uursuing BCA")
print("Replace string:",FindW)
FindC= Data.replace("u","P")
print("Replace c: ",FindC)
print("\n")

#Perform simple validation using string method such as isalpha(),isdigit(), and isalnum().

Check_Data = "princ52"
print("Check Data is string:",Check_Data.isalpha())
print("Check Data is digit:",Check_Data.isdigit())
print("Check Data is not_special_char:",Check_Data.isalnum())




