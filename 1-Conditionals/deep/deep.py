userInput = input(
    "What is the answer to the great question of life, the universe, and everything? "
)
if (
    userInput == str("42")
    or userInput == str("forty-two")
    or userInput == str("forty two")
):
    print("Yes.")
else:
    print("No.")
