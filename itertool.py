# binary_search.py
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

if __name__ == '__main__':
    data = [1, 3, 5, 7, 9]
    print(binary_search(data, 3, 0, len(data) - 1))
    print(binary_search(data, -1, 0, len(data) - 1))
    # Output:
    # True
    # False