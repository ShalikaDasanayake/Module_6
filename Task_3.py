# A program that gets the quantity of gasoline in American gallons and returns the number converted to litres.

def gallons_to_liters(gallons):

# 1 American gallon is approximately 3.78541 liters
    liters = gallons * 3.78541
    return liters

# Main program
def main():
    while True:

        # Ask user for input
        gallons = float(input("Enter volume in American gallons (negative to stop): "))

        # Stop if user enters negative value
        if gallons < 0:
            print("Program Ended.")
            break

        # Convert gallons to liters
        liters = gallons_to_liters(gallons)

        # Print putput
        print(f"{gallons} gallons is equal to {liters:.2f} liters.")

main()


