call_count_memo = 0
memo = {}

def fibonacci_memo(n):
    global call_count_memo
    call_count_memo += 1

    if n in memo:
        return memo[n]

    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)

    return memo[n]


call_count_memo = 0
memo.clear()

for i in range(n):
    print(fibonacci_memo(i), end=" ")

print("\nTotal function calls (Memoized):", call_count_memo)