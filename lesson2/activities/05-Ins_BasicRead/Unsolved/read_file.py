import os

# print(os.getcwd())
# txtpath = os.path.join('..','Resources','input.txt')
file = 'activities/05-Ins_BasicRead/Resources/input.txt'

with open(file, 'r') as text:
    # Stores a reference to a file stream
    print(text)

    #Store all the text inside of text
    lines = text.read()

    # Print the contents
    print(lines)