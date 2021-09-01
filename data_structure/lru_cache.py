import time


def timer(func):
    def inner(arg):
        print(arg)
        st = time.time()
        print(arg)
        func(arg)
        print(time.time() - st)
    return inner


def lru_cache(func):
    cache = {}

    def inner(arg):
        if arg in cache:
            return cache[arg]
        else:
            ret = func(arg)
            cache[arg] = ret
            return ret

    return inner


@lru_cache
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


@lru_cache
@timer
def fibo2(n):
    if n == 1 or n == 2:
        return 1
    else:
        print("..calculate!")
        return fibo(n - 1) + fibo(n - 2)


fibo2(35)
