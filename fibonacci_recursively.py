def get_fib(position):
    if position == 0 or position == 1:
        return position

    print get_fib(position - 1) + get_fib(position - 2)


# Test cases
print get_fib(12)
print get_fib(16)
print get_fib(10)
print get_fib(0)
