def check_first_last(lst):
  if lst[0] == lst[-1]:
    return True
  else:
    return False

# Contoh
list1 = [50, 20, 30, 40, 50]
list2 = [80, 65, 35, 75, 40]

print(check_first_last(list1)) # True
print(check_first_last(list2)) # False