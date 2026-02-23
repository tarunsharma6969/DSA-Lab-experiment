def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter number: "))
result = factorial(n)

if result is None:
    print("Invalid input")
else:
    print("Factorial:", result)