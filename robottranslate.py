input_string = input()

# Initialize variables
current_number = ""
natija = ""

# Iterate through each character in the string
for char in input_string:
    if char.isdigit():
        current_number += char
    elif not  char.isdigit():
        natija+=char
    elif current_number:
        # Convert the current number from decimal to binary and append to the result
        natija += bin(int(current_number))[2:]
        current_number = ""


# Check if there's a number at the end of the string
if current_number:
    natija += bin(int(current_number))[2:]

# Print the result
print(natija)