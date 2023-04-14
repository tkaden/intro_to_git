# Print Hello User!
print("Hello User!")

# Take in User Input
name = input("What is your name? ")

# Respond Back with User Input
print(f'Hello {name}')

# Take in the User Favorite Number
fav_num = input("What is your favorite number? ")

# Respond Back with a statement based on your favorite number
x = 50
if int(fav_num) < 50:
    print(f'Your fav number, {fav_num}, is less than mine!')
else:
    print(f'Your fav number, {fav_num}, is more than mine!')