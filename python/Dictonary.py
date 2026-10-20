# # dictionary empty
# dict1 = {}
# dict2 =dict({})
# print(type(dict1),type(dict2))

#create a dictinary

dict1 = {"one":1,"two":2,"three":3,"four":4}
print(dict1)

#access dictionary
print(dict1["one"])
print(dict1["three"])

#access by attributes
print(dict1.keys())
print(dict1.values())
print(dict1.items())

#acess by loop
dict2 ={"name":"prince","address":"pratappur","father":"ramesh","mother":"sangita"}
for keys,values in dict2.items():
  print(keys,":",values)

#modify the dict
dict3={1:"sunday",2:"moday",3:"tues",4:"wed",5:"thru",6:"frid",7:"sat",8:"sun"}
dict3[3]="Tuesday"
print(dict3)

