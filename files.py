#file handeling

with open('TextFile.txt', 'r') as file:
    lines = file.read()
    print(lines)
    print(file.mode)
    print(file)