def nth_root(A, n):
    """
    Return nth root of A.
    >>> nth_root(27, 3)
    3
    """

    current = A / 2
    limit = 0.1
    while True:
        value = pow(current, n) - A
        if abs(value) < limit:
            break
        offset = value / (n*pow(current, n-1))
        current -= offset
    return round(current, 2)

print("nth_root(27, 3): %s" % nth_root(27, 3))
print("nth_root(25, 3): %s" % nth_root(25, 3))
print("nth_root(81, 4): %s" % nth_root(81, 4))
print("nth_root(80, 4): %s" % nth_root(80, 4))
