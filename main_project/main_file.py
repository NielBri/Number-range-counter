# List
numbers = []
# Make a function that allows and detects a number
while True:
    # Number input
    try:
        num = input("Please input a number from 1-50 (press again ENTER to finish process): ")
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

# Make a function that counts how many numbers are in each range
amount_range1 = len(range1)
amount_range2 = len(range2)
amount_range3 = len(range3)
amount_range4 = len(range4)
amount_range5 = len(range5)

# Print
print("The amount of numbers from 1-10 are:", amount_range1)
print("The amount of numbers from 11-20 are:", amount_range2)
print("The amount of numbers from 21-30 are:", amount_range3)
print("The amount of numbers from 31-40 are:", amount_range4)
print("The amount of numbers from 41-50 are:", amount_range5)