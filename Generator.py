import itertools


# this modified function allow to obtain string instead of tuple
def product_str(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield ''.join(prod)


def generate(n):
    result_iterator = product_str('ACGT', repeat=1)
    if n > 1:
        for i in range(2, n+1):
            new_iterator = product_str('ACGT', repeat=i)
            result_iterator = itertools.chain(result_iterator, new_iterator)
    return result_iterator


print(generate(3))
