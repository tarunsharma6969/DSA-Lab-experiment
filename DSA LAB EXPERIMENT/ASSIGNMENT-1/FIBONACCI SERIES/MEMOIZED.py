call_count_memo = 0
memo = {}

def fibonacci_memo(n):
    global call_count_memo
    call_count_memo += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return memo[n]

call_count_memo = 0
memo.clear()
print("Fibonacci:", fibonacci_memo(n))
print("Function calls (Memo):", call_count_memo)