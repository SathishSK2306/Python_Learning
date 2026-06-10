student = {
    "name": "Sathish",
    "age": 23,
    "city": "Chennai"
}

# 1. get
print(student.get("name"))

# 2. keys
print(student.keys())

# 3. values
print(student.values())

# 4. items
print(student.items())

# 5. update
student.update({"age": 24})
print(student)

# 6. pop
student.pop("city")
print(student)

# 7. popitem
student.popitem()
print(student)

# 8. setdefault
student.setdefault("course", "Python")
print(student)

# 9. copy
a = student.copy()
print(a)

# 10. clear
student.clear()
print(student)
