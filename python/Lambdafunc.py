# even_odd = lambda x : "even" if x%2==0 else "odd"
# print(even_odd(10))

# square = lambda x : x**2
# print(square(10))

#use of map filter
li =[1,3,6,9,8,6,4,2,3465,6,7,89,76,5544]
evenno = list(filter(lambda x : x%2==0,li))
print(evenno)

#use of map
multiply = list(map(lambda x : x**2 , li))
print(multiply)