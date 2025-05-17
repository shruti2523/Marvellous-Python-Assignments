def sum_of_factors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

def main():
    num = int(input("Enter a number: "))
    print("Sum of factors:", sum_of_factors(num))

main()
