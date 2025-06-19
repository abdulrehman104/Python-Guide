# Read and print the content of the file

# Method 1: Using open() and read()
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Method 2: Context Manager, Using 'with' statement (The preferred way)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# Write new content to the file
# If  the file exists, it will be overwritten. If the file does not exist, it will create a new file.
file = open("example.txt", "w")
file.write("This is new content written to the file.")
file.close()

# Append content to the file
# If the file exists, it will append to the end of the file. If the file does not exist, it will create a new file.
file = open("example.txt", "a")  
file.write("\nThis is appended content.")
file.close()

# Read & Write Mode
# If the file exists, it will read the content and then write to the end of the file. If the file does not exist, it will create a new file.
file = open("example.txt", "r+")
content = file.read()
print(content)
file.write("\nThis is read/write mode.")
file.close()

# Using 'with' statement for file handling
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


# Writing to a file using 'with' statement
with open("example.txt", "w") as file:
    file.write("This is new content written using 'with' statement.")


# Appending to a file using 'with' statement
with open("example.txt", "a") as file:
    file.write("\nThis is appended content using 'with' statement.")


# Reading and writing in 'with' statement
with open("example.txt", "r+") as file:
    content = file.read()
    print(content)
    file.write("\nThis is read/write mode using 'with' statement.")


# Reading lines from a file
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())


# Writing multiple lines to a file
with open("example.txt", "w") as file:
    lines = ["First line.\n", "Second line.\n", "Third line.\n"]
    file.writelines(lines)


# Reading a file in binary mode
with open("example.txt", "rb") as file:
    content = file.read()
    print(content)


# Writing to a file in binary mode
with open("example.txt", "wb") as file:
    file.write(b"This is binary content written to the file.")
