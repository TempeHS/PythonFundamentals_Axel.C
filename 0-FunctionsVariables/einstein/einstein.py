userInput = input("Please enter mass in kg: ")

lightSpeedSquared = int(300000000 * 300000000)
userMass = int(userInput)
totalEnergy = userMass * lightSpeedSquared
print("Total energy of given mass: " + str(totalEnergy))
