# Li = [8,6,9,6,"prince","rauniyar"]
# print(Li)
# n = int(input("enter the num :"))
# Li.append(n)
# print(Li)
# Li.pop(2)
 #creating list using list()
# list = list(("prince",5,2,6,3,6))
 # print(list)
 # listrepeat = [2,3]*5
 # print(listrepeat)
 # print(list[2+1])
# print(list.append[2,6,5])


# liempty = []
# liempty = list()
# li = [5,8,9,6]
# #insert element

# li.append(50) # insert one element at the end
# print(li)
# li.extend([0,2,3]) # insert multiple element at the end
# print(li)
# li.insert(0,222) # insert at specfic point
# print(li)

# #update
# li[0]=111
# print(li)

# #removing
# li.remove(111) # remove first occurance
# print(li)
# li.pop() # remove specified index or if not give than del last ele
# print(li)
# del li[1] # delete by index
# print(li)

# #iterating list
# l2=[8,7,6,9,6,3]
# for var in l2:
#   print(var)

# #nested list
# l3 =[2,3,6,3,[8,9,6,3],[8,6,2]]
# print("6 is print:", l3[4][2])

# #slicing
# l4 = [8,7,6,9,6,2,3,1]
# print(l4[2:5]) #6,9,6
# print(l4[::-1]) #reverse
# print(l4[-1::-1]) #reverse
# print(l4[::-2]) # 2,9,7
# print(l4[0:]) #all print
# print(l4[-1::5]) #1 only not going backward

# #consuctive modifing
# l5=[8,9,6,3,6,9]
# l5[1:4]=[0,1,2]
# l5[0:3]=[99,88,77,66] # range se jade item honge to bhi add ho jayega
# print(l5)
# l5[1:4]=["A"] # range replace ho jayega kewal A se [8,'A',6,9]

# #repeatation
# l6=[2,5]*5
# print(l6) 

# #membership chekcing
# l7=[4,5,2,6,"prince","deepak","Pranshu",8,3]
# if "prince" in l7:
#   print("found")
# else:
#   print("unfound")

# print(8 in l7)

# # concatenation
# l6 =[38,2,5,23,12]
# l7 =[8,6,2]
# print(l7+l6) 

# #list comprehensions
# evenodd =["even" if i%2==0 else "odd" for i in range(5)]
# print(evenodd)

# square = [x**2 for x in range(1,5)]
# print(square)

# #function practise
# li = [8,6,3,6,9]
# l2=li.copy() # not pass argument copy the list into l2
# print(len(li))
# print(min(li))
# print(max(li))
# print(sorted(li))
# print(sum(li))
# print(li.sort()) # none  because sort in existing list not return anything so none is output
# print(li) # than sorted list appear 
# print(li.reverse()) #none because modifiy in existing list
# print(li.count(1)) #(0) because not 1 in list
# print(li.clear()) # clear all list element
# print(li.index(8)) # 0 return index if found otherwise gives error
# del li[1] #delete index which element obtained 1. (del li) delete entire lise





