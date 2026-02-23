# factorial = function name
# (n) = parameter that stores input number
def factorial(n):

    # if n < 0 → factorial not defined for negative numbers
    if n < 0:

        # return None means invalid input
        return None

    # Base Case:
    # if n == 0 → factorial of 0 is 1
    # This stops recursion
    if n == 0:
        return 1

    # Recursive Case:
    # n * factorial(n-1)
    # Function calls itself with smaller value
    return n * factorial(n - 1)


# ------------------------------------------------------------
# Call Stack Trace Function (for understanding)
# ------------------------------------------------------------

def factorial_with_trace(n):

    # print entering function
    print(f"Entering factorial({n})")

    if n < 0:
        return None

    if n == 0:
        print("Base case reached: factorial(0) = 1")
        return 1

    # recursive call
    result = n * factorial_with_trace(n - 1)

    # print returning value
    print(f"Returning from factorial({n}) = {result}")

    return result


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

def main():

    # take input from user
    n = int(input("Enter a number: "))

    # call factorial function
    result = factorial(n)

    # check invalid input
    if result is None:
        print("Invalid input! Factorial not defined for negative numbers.")
    else:
        print("Factorial:", result)

    print("\n--- Call Stack Trace ---\n")

    # show step-by-step recursion
    factorial_with_trace(n)


# run program
if __name__ == "__main__":
    main()