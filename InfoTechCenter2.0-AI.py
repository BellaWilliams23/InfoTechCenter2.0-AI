# Print a header for the Gasoline Branch
print("*************************************************************")
print("Gasoline Branch\n\n")

# Import necessary libraries
import random  # For generating random numbers
from time import sleep  # For introducing delays in the script


# Function that randomly selects a gas level and returns it
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Function that randomly selects a gas station and returns it
def listOfGasStations():
    gasStation = ["Shell", "Marathon", "Circle K", "Mobile", "Costco", "Meijer", "7Eleven"]
    gasStationsNearby = random.choice(gasStation)
    return gasStationsNearby


# Function that alerts the user based on the gas level
def gasLevelAlert():
    # Generate random distances to gas stations for different gas levels
    milesToGasStationsLow = round(random.uniform(1, 25), 1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50), 1)

    # Get the current gas level
    gasLevelIndicator = gasLevelGauge()

    # Check the gas level and provide appropriate alerts
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("\n  ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is a quarter full, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half full, which is plenty to get to your destination.")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three-quarters full, which is plenty to get to your destination.")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Full Tank":
        print("Your gas tank is FULL !!! YAY !!! YOU'RE NOT POOR AFTER ALL !!!!")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsLow, "miles away.")


# Call the function to start the simulation
gasLevelAlert()
