def fibonacci(n):
    fib = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
    return fib[n]

if __name__ == '__main__':
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(10))
