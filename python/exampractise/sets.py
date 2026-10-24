seta = {1,2,3,4,5,6}
setb = {1,2,3,7,8,9}

# for i in seta:
#   print(i)
union = seta.union(setb)
print(union)

intersection = seta.intersection(setb)
print(intersection)

difference = seta.difference(setb)
print(difference)

symetric_Difference = seta.symmetric_difference(setb)
print(symetric_Difference)

seta.add(12)
print(seta)
seta.update({52,99,66,33})
print(seta)

seta.pop()
print(seta)

# seta.remove(200)
# print(seta)

seta.discard(200)
print(seta)

print(len(seta))
print(min(setb))