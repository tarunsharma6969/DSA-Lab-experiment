# Complexity Check

# ------------------------------------------------------------
# 1. Single Loop → O(n)
# ------------------------------------------------------------

# single_loop = function name
# (n) = parameter that represents input size
def single_loop(n):

    # count = variable to count number of operations
    count = 0

    # for = loop keyword
    # i = loop variable
    # range(n) = generates numbers from 0 to n-1
    for i in range(n):

        # count += 1 increases count by 1 each iteration
        count += 1

    # print result
    print("Single Loop Operations:", count)
    print("Time Complexity: O(n)\n")


# ------------------------------------------------------------
# 2. Nested Loop → O(n^2)
# ------------------------------------------------------------

def nested_loop(n):

    count = 0

    # outer loop runs n times
    for i in range(n):

        # inner loop also runs n times
        for j in range(n):

            # total operations = n * n
            count += 1

    print("Nested Loop Operations:", count)
    print("Time Complexity: O(n^2)\n")


# ------------------------------------------------------------
# 3. Triangular Loop → O(n^2)
# ------------------------------------------------------------

def triangular_loop(n):

    count = 0

    # outer loop runs n times
    for i in range(n):

        # inner loop runs from 0 to i-1
        # total approx = n(n-1)/2
        for j in range(i):

            count += 1

    print("Triangular Loop Operations:", count)
    print("Time Complexity: O(n^2)\n")


# ------------------------------------------------------------
# 4. Halving Loop → O(log n)
# ------------------------------------------------------------

def halving_loop(n):

    count = 0

    # while loop runs until n becomes 1
    # each time n is divided by 2
    while n > 1:

        # n //= 2 means divide n by 2 (integer division)
        n = n // 2

        count += 1

    print("Halving Loop Operations:", count)
    print("Time Complexity: O(log n)\n")


# ------------------------------------------------------------
# Linear Search (Best / Worst Case Demonstration)
# ------------------------------------------------------------

def linear_search(arr, key):

    count = 0

    for i in range(len(arr)):
        count += 1

        if arr[i] == key:
            print("Element found at index:", i)
            print("Operations:", count)
            return

    print("Element not found")
    print("Operations:", count)


# ------------------------------------------------------------
# Binary Search (Worst Case O(log n))
# ------------------------------------------------------------

def binary_search(arr, key):

    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:

        count += 1

        mid = (low + high) // 2

        if arr[mid] == key:
            print("Element found at index:", mid)
            print("Operations:", count)
            return

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    print("Element not found")
    print("Operations:", count)


# ------------------------------------------------------------
# Main Program to Test Everything
# ------------------------------------------------------------

def main():

    # take input size
    n = int(input("Enter value of n: "))

    print("\n--- Loop Complexity Tests ---\n")

    single_loop(n)
    nested_loop(n)
    triangular_loop(n)
    halving_loop(n)

    print("\n--- Linear Search Test ---\n")
    arr = list(range(1, n+1))
    linear_search(arr, n)   # worst case example

    print("\n--- Binary Search Test ---\n")
    binary_search(arr, n)   # worst case example


# run program
if __name__ == "__main__":
    main()