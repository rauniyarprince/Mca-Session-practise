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

#delete
li=[8,9,6,5,6]
li.remove(6)
print(li)
li.pop(2)
print(li)
del li[0]
print(li)
del li
print (li) # li is not defined error because entire list del
