
#native fibonacci function,it will calculate same fibonacci numbers multiple times.
naive_calls = 0

def fib(n):
    global naive_calls
    naive_calls += 1
    
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# here we are using memoization to optimize the fibonacci function, it will store the previously computed results in a dictionary 
memo = {}
memo_calls = 0

def fib_memo(n):
    global memo_calls
    memo_calls += 1
    
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]


#testing the functions
n = 10

print("Naive Result:", fib(n))
print("Naive Calls:", naive_calls)

print("\nMemoized Result:", fib_memo(n))
print("Memoized Calls:", memo_calls)