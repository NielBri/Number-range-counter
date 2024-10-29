# List
numbers = []
# Make a function that allows and detects a number
while True:
    # Number input
    try:
        num = input("Please input a number from 1-50 (press ENTER to finish process): ")
        if num == "":
            break
        num = float(num)
        if 0 < num <= 50:
            print("Input is within the range. ")
            # Put the numbers in an array
            numbers.append(num)
        else:
            print("Error. Please input a value within the range")
    except:
        print("Please input a valid number. ")

# Make a function that separates the numbers in the given ranges
# Make a function that counts how many numbers are in each range
# Print