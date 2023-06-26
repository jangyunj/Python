def verify(index):
    if index is None:
        print("Target found at index ", index)
    else:
        print("Target not found in the list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)