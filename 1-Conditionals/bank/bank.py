userGreeting = input("Greet me. Now. ")
if userGreeting.startswith("hello") or userGreeting.startswith("Hello"):
    print("0$")
elif userGreeting.startswith("h") or userGreeting.startswith("H"):
    print("$20")
else:
    print("$100")
