#Import the math module
import math
import datetime

# Tire prizes
tire_prices = {
    (185, 70, 14): 100.00,
    (205, 55, 16): 120.00,
    (215, 65, 17): 130.00,
  
}

#Description of what the program does
print("This program reads input, computes and outputs  the volume")
print("of space inside the tire")

#Get input for width, aspect ratio and diameter of the tire
width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

#Compute the volume of the space inside the tire

pi = math.pi
volume = pi * width**2 * aspect_ratio * (width * aspect_ratio + float(2540) * diameter) / float(10000000000)

# Output
print(f"The approximate volume is {volume:.2f} liters.")

# Check if tire size is available in dictionary
tire_size = (width, aspect_ratio, diameter)
if tire_size in tire_prices:
    price = tire_prices[tire_size]
    print(f"The price for the selected tire size is ${price:.2f}")
else:
    print("Tire size not found in the price list. Please inquire at your local tire shop.")


buy_tires = input("Do you want to buy tires? (yes/no): ")

# Get the current date from the computer's operating system
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Append the tire information to the volumes.txt file
with open("volumes.txt", "at") as volumes:
    volumes.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n")


# Check if the user wants to buy tires with the inputed dimensions
if buy_tires == "yes":
    # Ask for the user's phone number
    phone_number = input("Please enter your phone number: ")
    # Append the phone number to the volumes.txt file
    with open("volumes.txt", "at") as volumes:
        volumes.write(f"{phone_number}")
    print("Thank you! Your phone number has been recorded.")
else:
    print("Thank you for using our tire volume calculator.")





   










