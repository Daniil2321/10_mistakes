from time import time


def fast_function(n):
    return sum(range(n))


if __name__ == "__main__":
    start = time()
    print(fast_function(1000000000))
    end = time()
    print(f"Time: {end - start}")
