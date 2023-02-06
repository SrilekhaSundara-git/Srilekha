

memo: dict  = {0: 0, 1: 1} # base cases

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    print(memo)
    return memo[n]
print(fib3(100))
