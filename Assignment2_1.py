import Arithmetic

def main():
    a= float(input("Enter first number : "))
    b= float(input("Enter Second number : "))
    
    print("Addition :",Arithmetic.Add(a,b))
    print("Substraction :",Arithmetic.Sub(a,b))
    print("Multiplication :",Arithmetic.Mult(a,b))
    print("Division :",Arithmetic.Div(a,b))

if __name__ == "__main__":
    main()