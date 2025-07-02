list=[1,2,3,4,5,6]

# 1. append
print(list.append(7))
print(list)

# 2. insert
list.insert(6,8)
print(list)

# 3. pop
list.pop(6)
print(list)

# 4. remove
list.remove(6)
print(list)

# 5. reverse
list.reverse()
print(list)

# 6. count
print(list.count(2))

# 7. extend
list.extend([7,8])
print(list)

# 8. index
print(list.index(5))

# 9. sort
list1=[2,6,1,9,6,2,1,5]
list1.sort()
print(list1)

# 10. copy
a=list.copy()
print(a)
print(list)

# 11. clear
list.clear()
print(list)
