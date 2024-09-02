def divide(a, b):
    try:
        return a / b
    except Exception as e:
        return e


if __name__ == "__main__":
    print(divide(10, 5))
    print(divide(10, 0))
    print(divide(10, None))
