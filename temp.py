def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

def feet_to_meters(feet):
    meters = feet / 3.28084
    return meters

while True:
    print("Choose an option:")
    print("1. Convert meters to feet")
    print("2. Convert feet to meters")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        meters = float(input("Enter the length in meters: "))
        feet = meters_to_feet(meters)
        print(f"{meters} meters is equal to {feet} feet.\n")
    elif choice == "2":
        feet = float(input("Enter the length in feet: "))
        meters = feet_to_meters(feet)
        print(f"{feet} feet is equal to {meters} meters.\n")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")