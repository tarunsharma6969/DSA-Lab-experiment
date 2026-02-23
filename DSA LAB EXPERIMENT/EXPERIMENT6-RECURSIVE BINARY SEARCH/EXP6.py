# binary_search = function name
# (arr) = sorted list
# (key) = element to search
# (low) = starting index
# (high) = ending index
def binary_search(arr, key, low, high):

    # Base Case 1:
    # if low > high → element not found
    if low > high:
        return -1

    # Find middle index
    # // = integer division
    mid = (low + high) // 2

    # If key is found
    if arr[mid] == key:
        return mid

    # If key is smaller than middle element
    elif key < arr[mid]:
        # Search in left half
        return binary_search(arr, key, low, mid - 1)

    # Otherwise search in right half
    else:
        return binary_search(arr, key, mid + 1, high)


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

def main():

    # Take sorted input list from user
    arr = list(map(int, input("Enter sorted numbers separated by space: ").split()))

    # Take key to search
    key = int(input("Enter element to search: "))

    # Edge case: empty list
    if len(arr) == 0:
        print("Empty list. Nothing to search.")
        return

    # Call recursive binary search
    index = binary_search(arr, key, 0, len(arr) - 1)

    # Print result
    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found.")


# Run program
if __name__ == "__main__":
    main()