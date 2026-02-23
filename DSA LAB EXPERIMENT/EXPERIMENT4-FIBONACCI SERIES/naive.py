call_count = 0

def fibonacci_naive(n):
    global call_count
    call_count += 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)


n = int(input("Enter number of terms: "))

call_count = 0
for i in range(n):
    print(fibonacci_naive(i), end=" ")

print("\nTotal function calls:", call_count)