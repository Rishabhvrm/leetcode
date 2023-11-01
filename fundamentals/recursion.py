## 1. FIBONACCI

## RECURSION
def recursice_fib(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive step
    return recursice_fib(n - 1) + recursice_fib(n - 2)
print('------------------------------------------------')
# print(f'function => recursice_fib(34) Output => {recursice_fib(34)}')
print('------------------------------------------------')



## ITERATIVE MEMOIZATION
def iterative_memo_fib(n):
    dp = [0] * (n+1)
    # base cases
    dp[0] = dp[1] = 1

    # iterative
    for idx in range(2, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]
    return dp[n]
print('------------------------------------------------')
print(f'function => iterative_memo_fib(34) Output => {iterative_memo_fib(34)}')
print('------------------------------------------------')




## RECURSIVE MEMOIZATION
## memo = {}, n -> fib value for n
def recursive_memo_fib(n, memo):
    if n in memo: return memo[n]

    if n == 0 or n == 1:
        memo[n] = 1
    else:
        memo[n] = recursive_memo_fib(n - 1, memo) + recursive_memo_fib(n - 2, memo)
    return memo[n]
print('------------------------------------------------')
print(f'function => recursive_memo_fib(100, [memo]) Output => {recursive_memo_fib(100, {})}')
print('------------------------------------------------')
