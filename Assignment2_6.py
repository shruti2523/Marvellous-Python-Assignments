def pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)

def main():
    num = int(input("Enter a number: "))
    pattern(num)

main()
