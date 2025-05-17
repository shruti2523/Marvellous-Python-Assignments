from functools import reduce

def main():
    numbers = [2, 70, 11, 10, 17, 23, 31, 77]

    filtered = list(filter(lambda x: x % 2 != 0, numbers))
    mapped = list(map(lambda x: x * 2, filtered))
    reduced = reduce(lambda x, y: x if x > y else y, mapped)

    print("List after filter =", filtered)
    print("List after map =", mapped)
    print("Output of reduce =", reduced)

main()
