# Get the four-digit positive integer from user input
while True:
    number = input("Enter a four-digit positive integer: ")
    
    # Check if the number is -ve
    if number.startswith('-'):
        print("Invalid input. Negative numbers are not allowed.\n")
        continue
    
    # Check if the input is numeric
    if not number.isdigit():
        print("Invalid input. Please enter numeric values only.\n")
        continue
    
    # length of the number is exactly 4
    if len(number) != 4:
        print("Invalid input. Please enter a number with exactly four digits.\n")
        continue
    
    # If all checks pass
    break

# sum of digits
digit_sum = sum(int(digit) for digit in number)


print(f"The sum of digits is: {digit_sum}")