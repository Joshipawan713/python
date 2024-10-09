# file i/o in python - i/o - input or output
# python can be used to perform operations on a file.(read & write data)
# type of all files
# 1. text files - .txt, .docx, .log, etc.
# 2. binary files - .mp4, .mov, .png, .jpeg, etc.
# open , read and close file - we have to open a file before reading or writing.
# 'r' - open for reading(default)
# 'w' - open for writing , truncating the file first
# 'x' - create a new file and open it for working
# 'a' - open for writing , appending to the end of the file if it exist
# 'b' - binary mode
# 't' - text mode
# '+' - open a disk for updating (reading and writing)

# open method in file

# f = open("demo.txt","r")
# data = f.read()
# data = f.read(5) #read entire file
# print(data)
# print(type(data))

# # readline one by one

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

# # write method in file

# f = open("demo.txt","w")

# f.write("Python is very fast programming language.")

# f.close()

# # append method in file

# f = open("demo.txt","a")

# f.write("\n Python is very fast programming language.")

# f.close()


# # with syntax through - with not complusory to f.close() because with automic f.close() the file
# with open('demo.txt','r') as f:
#     data = f.read()
#     print(data)

# # delete file

# import os
# os.remove("demo.txt")