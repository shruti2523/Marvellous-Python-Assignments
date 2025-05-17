from functools import reduce

def main():
    numbers = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    
    filtered = list(filter(lambda x: 70 <= x <= 90, numbers))
    mapped = list(map(lambda x: x + 10, filtered))
    reduced = reduce(lambda x, y: x * y, mapped)

    print("List after filter =", filtered)
    print("List after map =", mapped)
    print("Output of reduce =", reduced)

main()
