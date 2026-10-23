def generator():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5 
  yield 6
  yield 7

iter = generator()
for i in range(7):
  print(next(iter))
