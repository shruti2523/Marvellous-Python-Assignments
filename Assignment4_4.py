from functools import reduce

def main():
    numbers = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    filtered = list(filter(lambda x: x % 2 == 0, numbers))
    mapped = list(map(lambda x: x * x, filtered))
    reduced = reduce(lambda x, y: x + y, mapped)

    print("List after filter =", filtered)
    print("List after map =", mapped)
    print("Output of reduce =", reduced)

main()
