# li1=[]
# li2=list()
# li=[8,9,6,3,6,9]
# li3=list([8,9,6,3,6])
# print(li)
# print(li3)

# #insert
# n = 10
# li.append(n) # we can also pass  var which one value
# li.append(5)
# print(li)
# li.extend([0,1,2,3])
# print(li)
# li.insert(0,99)
# print(li)

# #update
# li=[1,2,3,4,5,6]
# li[0]="prince"
# print(li)
# li[1:3]=[8,8,8]
# print(li)
# li[1:3]=['A']
# print(li)

# #delete
# li=[8,9,6,5,6]
# li.remove(6)
# print(li)
# li.pop(2)
# print(li)
# del li[0]
# print(li)
# del li
# print (li) # li is not defined error because entire list del


# #mebership 
# li = [8,6,9,63,"pr","de"]
# if 8 in li:
#   print("found")
# else:
#   print("not found")


# #user input
# list=[]
# li = int(input("enter the len of list"))
# for i in range(li):
#   user = input("enter the element: ")
#   list.append(user)
# print(list)


# #passing list in function
# def list(li):
#   for i in li:
#     print(i)
# li=[8,9,6,2,6]
# list(li)

# #function
# li=[8,9,6,3,3,3,3,6]
# print(len(li))
# print(min(li))
# print(max(li))
# print(sorted(li))
# li.reverse()
# print("reverse",li)
# li.sort()
# print("sorted",li)
# print(li.index(3))
# print("how many 3 in list",li.count(3))
# print(li.clear())

# #copy list
# li=[9,6,3,6]
# li2=li.copy() # gives the reference

# #list comprehensive

# square =[x**2 for x in range(5)]
# print(square)

# evenodd = ["even" if n%2==0 else "odd" for n in range(10)]
# print(evenodd)


li=[8,9,6,3,9]
li[0]=99
print(li)




