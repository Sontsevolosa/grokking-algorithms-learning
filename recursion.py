def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x - 1)


# how to use this code:
print(fact(3))
