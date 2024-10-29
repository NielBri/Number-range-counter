# List
numbers = []
# Make a function that allows and detects a number
while True:
    # Number input
    try:
        num = int(input("Please input a number (1-50): "))
        if 0 < num <= 50:
            # Breaks the loop that detects a number
            break
        else:
            print("Error! Please input a valid number range (1-50)")
    except:
        print("Error! Please input again.")

# Put the numbers in an array
# Make a function that separates the numbers in the given ranges
# Make a function that counts how many numbers are in each range
# Print