def gen():
  yield 1
  yield 2
  yield 3
  yield 4
  
result = gen()
print(next(result))
print(next(result))
print(next(result))
print(next(result))



