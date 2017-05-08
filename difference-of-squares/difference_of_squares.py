def square_of_sum(n):
    s = [i for i in range(n + 1)]
    s = sum(s)
    return s ** 2

def sum_of_squares(n):
    s = [i ** 2 for i in range(n + 1)]
    return sum(s)

def difference(n):
    return abs(square_of_sum(n) - sum_of_squares(n))
