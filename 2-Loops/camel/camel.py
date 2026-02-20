user_variable = input("Please input a variable name: ")

snake_case = ""


for character in user_variable:
    if character.isupper():
        snake_case += "_" + character.lower()
    else:
        snake_case += character


print(snake_case)
