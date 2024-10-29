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
range1 = [num for num in numbers if 1 <= num <= 10]
range2 = [num for num in numbers if 11 <= num <= 20]
range3 = [num for num in numbers if 21 <= num <= 30]
range4 = [num for num in numbers if 31 <= num <= 40]
range5 = [num for num in numbers if 41 <= num <= 50]

print(range1)
# Make a function that counts how many numbers are in each range
# Print