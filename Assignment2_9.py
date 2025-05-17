def count_digits(n):
    return len(str(n))

def main():
    num = int(input("Enter a number: "))
    print("Number of digits:", count_digits(num))

main()
