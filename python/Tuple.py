# #empty tuple
# tuple2 =()
# tuple2=tuple()

# #accesing
# tu = (7,8,9,6,3)
# print(tu[2])
# print(tu[-1])
# print(tu[4::-1]) #revese
# print(tu[2::-1]) #8,7
# print(tu[::-1])

# #nested tuple
# tu =(2,3,4,56,(23,34,5,(4,5.5,3),76,7),7,8,9)
# print(tu[4][3][1])
# print(tu[5])

# # mebership

# tu=("prince","deepak",8,5,6,9)
# if "prince" in tu:
#   print("found")
# else:
#   print("not fund")


#   #change tuple by converting in list
# tu2=("prince","deepak",8,5,6,9)
# list= list(tu2)
# list[0]="jagriti"
# tuple =tuple(list)
# print(tuple)

#  #if tuple contain list
# tu = (8,9,6,3,6,[1,3,6],23)
# tu[5][1]=999  #its possible because tuple itself imutable but it contain mutable object so it change list 
# print(tu)

# #packing (it meand putting multiple value into single variable)
# t= (5,9,6,3,6)
# print (t)
# #unpacking(when you assing the tuple value into separrate variable)
# t= (5,9,6,3,6)
# a,b,c,d,e =t
# print (d) #3

# #iterate tuple
# t = (8,9,6,3,6,9)
# for i in t:
#   print (i)

# #joining tuple
# t=(8,9,6)
# t2=(9,6,3,6)
# print(t+t2)
# #multiple tuple
# t5 = t*5
# print(t5)

# #comparing
# t=(8,9,6)
# t2=(9,6,3,6)
# print(t == t2)

#tuple function
t2=(9,6,9,3,6)
# print(len(t2))
# print(min(t2))
# print(max(t2))
# print(sorted(t2))
# t2.count(9)
# print(t2)
t2.index(3)
print(t2)
