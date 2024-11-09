# File Creation
# Step 1: Create a new text file and write initial content
with open("my_file.txt", 'w') as file:
    file.write("Hello, this is the first line.\n")
    file.write("The answer to life is 42.\n")
    file.write("Python file handling is easy!\n")

# File Reading and Display
# Step 2: Read the contents of the file and display them on the console
with open("my_file.txt", 'r') as file:
    content = file.read()
    print("Contents of 'my_file.txt':")
    print(content)

# File Appending
# Step 3: Open the file in append mode and add more lines
with open("my_file.txt", 'a') as file:
    file.write("Appending a new line to the file.\n")
    file.write("File handling operations are useful.\n")
    file.write("This is the last appended line.\n")

# Verify the appended content by reading and displaying the final content
with open("my_file.txt", 'r') as file:
    final_content = file.read()
    print("Final contents of 'my_file.txt' after appending:")
    print(final_content)
