from __future__ import print_function
import time
import functools


def benchmark(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - t)
        return res

    return wrapper


@benchmark
def add(a, b):
    """
    Function add.

    :param a:
    :param b:
    :return:
    """
    time.sleep(1)
    return a + b


print(add(1, 2))
print (add.__name__)
print (add.__doc__)
