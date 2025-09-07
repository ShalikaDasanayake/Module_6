# The program that returns the sum of all the numbers in the list.

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main program
my_list = [10,20,30,40,50,60,70,80] # example
result = sum_of_list(my_list)
print("The sum of the list is:", result)
