
def pattern(n):
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()

def main():
    num = int(input("Enter a number: "))
    pattern(num)

main()
