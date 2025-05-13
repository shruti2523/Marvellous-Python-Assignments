def Add(no1,no2):
    output = (no1+no2)
    return output

def main():
    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    result = Add(Value1,Value2)
    print("Addition : ",result)


if __name__ == "__main__":
    main()