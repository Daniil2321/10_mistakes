from time import time


def slow_function(n):
    result = 0
    for i in range(n):
        result += i
    return result


if __name__ == "__main__":
    start = time()
    print(slow_function(1000000000))
    end = time()
    print(f"Time: {end - start}")
