def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,3,5]))
print(test_distinct([2,4,6,7,7,9]))
