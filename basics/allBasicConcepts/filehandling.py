#Reading from and writing to files is essential when dealing with test data or logs.

#reading from a file

with open("test.txt","r") as file:
    content = file.read()
    print(content)

#writing to a file
with open("test.txt","w") as file:
    file.write("\n 1 \n 2")