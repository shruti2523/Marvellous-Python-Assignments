# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a factor, not prime
    return True  # No factors found, it is prime

# Main function
def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print("It is a Prime Number")
    else:
        print("It is Not a Prime Number")

# Call the main function
main()
