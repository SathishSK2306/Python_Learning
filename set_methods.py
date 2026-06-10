my_set = {1, 2, 3, 4, 5}

# 1. add
my_set.add(6)
print(my_set)

# 2. update
my_set.update([7, 8, 9])
print(my_set)

# 3. remove
my_set.remove(9)
print(my_set)

# 4. discard
my_set.discard(8)
print(my_set)

# 5. pop
my_set.pop()
print(my_set)

# 6. copy
a = my_set.copy()
print(a)

# 7. union
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

# 8. intersection
print(set1.intersection(set2))

# 9. difference
print(set1.difference(set2))

# 10. symmetric_difference
print(set1.symmetric_difference(set2))

# 11. clear
my_set.clear()
print(my_set)
