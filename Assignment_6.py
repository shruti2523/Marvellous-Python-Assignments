def main(): 
    print("Enter a Number : ")
    num = float(input())

    if num > 0:
        print("The Number is Positive")
    elif num < 0:
        print("The Number is Negative")
    else:
        print("The Number is Zero")   

if __name__ == "__main__":
    main()         
