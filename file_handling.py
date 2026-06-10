# to create a file and write data into it

# for create and write the file
file = open("file1.txt", "w")
file.write("hello sathish, how are you ?")
file.close()

# to read the file
file = open("file1.txt", "r")
print(file.read())
file.close()
