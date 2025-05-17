def sum_digits(n):
    return sum(int(digit) for digit in str(n))

def main():
    num = int(input("Enter a number: "))
    print("Sum of digits:", sum_digits(num))

main()
