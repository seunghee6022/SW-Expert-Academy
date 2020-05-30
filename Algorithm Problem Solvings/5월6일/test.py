def sum10(n):
    if n <= 1:
        return n
    else:
        return n + sum10(n-1)

print(sum10(10))