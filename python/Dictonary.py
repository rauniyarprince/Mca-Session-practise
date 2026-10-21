# # dictionary empty
# dict1 = {}
# dict2 =dict({})
# print(type(dict1),type(dict2))

# #create a dictinary

# dict1 = {"one":1,"two":2,"three":3,"four":4}
# print(dict1)

# #access dictionary
# print(dict1["one"])
# print(dict1["three"]) #it used when key exist otherwise gives key error
# print(dict1.get("five","not found")) #its used when the key is may not be exist in dict

# #access by attributes
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# #acess by loop
# dict2 ={"name":"prince","address":"pratappur","father":"ramesh","mother":"sangita"}
# for keys,values in dict2.items():
#   print(keys,":",values)

# #modify the dict
# dict3={1:"sunday",2:"moday",3:"tues",4:"wed",5:"thru",6:"frid",7:"sat",8:"sun"}
# dict3[3]="Tuesday" 
# print(dict3)

# #update a multiple item at once
# dict3={"math":28,"science":96,"physics":52,"chemistry":46}
# print(dict3)
# dict3.update({"sst":52,"gk":633}) # add multiple ele in dict
# print(dict3)

# #delete
# del dict3["sst"]
# print(dict3)
# dict3.pop("math","not found") # delte specified elem no error if not found 
# print(dict3)
# dict3.clear()  # clear dict

#checking in dict
num = 0
dictc={"one":1,"two":2,"three":3}
for 1 in dictc.values():
  if 1 in value:
    num +=1

if num <=1:
  print("present")

 
  









