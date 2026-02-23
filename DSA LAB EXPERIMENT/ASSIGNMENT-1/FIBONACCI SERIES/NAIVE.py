call_count = 0

def fibonacci_naive(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

n = int(input("Enter n: "))
call_count = 0
print("Fibonacci:", fibonacci_naive(n))
print("Function calls:", call_count)