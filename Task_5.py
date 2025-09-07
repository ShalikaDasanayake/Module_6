# The program that removes all uneven numbers from a given list of integers.

# Function to remove all uneven (odd) numbers from a list
def remove_odds(nimbers):

    # Create a new list to hold even numbers only
    even_numbers =[]
    for number in nimbers:
        if number % 2 == 0: # Check whether number is even or not
            even_numbers.append(number)
    return even_numbers

# Main program
def main():
    original_list = [1,2,3,4,5,6,7,8,9,10] # Sample list
    filtered_list = remove_odds(original_list) # Function to remove odd numbers

# Show both lists
    print("Original list:", original_list)
    print("List without odd numbers:", filtered_list)

# Run the main program
main()