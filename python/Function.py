# def sum(a,b):
#   return a+b
# print(sum(8,9))


def maximu_nu(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  else:
    return c

print(maximu_nu(3,12,9))
