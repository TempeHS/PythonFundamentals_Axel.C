def convert(userStr):
    return userStr.replace(":)", "🙂").replace(":(", "🙁")


def main():
    userInput = input("Enter text for emoji conversion: ")
    # this is passing userInput as userStr in the convert function
    print(convert(userInput))


main()
