
num = int(input("Enter a number: "))

for i in range(num):   #range(num) means it will run from 0 to num-1.So if num = 5, this loop runs 5 times (i.e., i = 0 to 4).

    for j in range(num):
        print("*", end="\t")
    print()
