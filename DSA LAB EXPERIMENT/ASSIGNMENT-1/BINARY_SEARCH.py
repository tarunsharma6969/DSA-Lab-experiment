def binary_search(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)

arr = [2, 4, 6, 8, 10]
key = 8
index = binary_search(arr, key, 0, len(arr)-1)

if index != -1:
    print("Found at index:", index)
else:
    print("Not found")