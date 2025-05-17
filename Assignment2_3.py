# Take number input from user
num = int(input("Enter a number: "))

# Initialize result to 1
factorial = 1

# Use a counter variable
i = 1

# Multiply numbers from 1 to num
while i <= num:
    factorial = factorial * i
    i = i + 1

# Print the result
print("Factorial:", factorial)
