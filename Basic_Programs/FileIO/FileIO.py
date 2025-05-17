# File reading and writing

def read_test():
    with open("readfile.txt", "r") as file:
       contents = file.read()
       print(contents) 

def write_test():
    with open("writefile.txt", "w") as file:
        file.write("ARE YOU WRITING ME?")

def append():
    name = input("Enter your name: ")
    with open("appendfile.txt", "a") as file:
        file.write(f" {name}")

def exception_test():
    try:
        totallyexistingfile = input("Enter the file you want to read: ")
        with open(totallyexistingfile, "r") as file:
            totallyexistingcontents = file.read()
            print(totallyexistingcontents)
    except FileNotFoundError:
        print(f"Are you sure the file '{totallyexistingfile}' exists?")

def line_by_line():
    with open("linebyline.txt", "r") as file:
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")

def write_multiple_lines():
    multiple_lines = ["Memories of You", "Don't", "Brand New Days"]
    with open("multiplelines.txt", "w") as file:
        for i, _ in enumerate(multiple_lines, start=1):
            writeme = multiple_lines[i-1]
            file.write(f"Line {i}: {writeme}\n")


if __name__ == "__main__":
    read_test()
    write_test()
    append()
    line_by_line()
    write_multiple_lines()
    exception_test()