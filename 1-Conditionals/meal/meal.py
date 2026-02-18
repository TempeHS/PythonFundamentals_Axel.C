def main():
    userInput = input("Please input a time: ")
    totalTime = convert(userInput)
    if totalTime >= 7 and totalTime <= 8:
        print("Time for breakfast.")
    elif totalTime >= 12 and totalTime <= 13:
        print("Time for lunch.")
    elif totalTime >= 18 and totalTime <= 19:
        print("Time for dinner.")
    else:
        print("starve to death")


def convert(time):
    hrStr, minStr = time.split(":")
    result = float(hrStr) + float(minStr) / 60
    return result


main()
