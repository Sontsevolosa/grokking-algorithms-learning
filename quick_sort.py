def quickSort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
  return quickSort(less) + [pivot] + quickSort(greater)


# how to use this code:
print(quickSort([10, 5, 2, 3]))
