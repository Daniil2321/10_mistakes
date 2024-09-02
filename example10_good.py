from unittest import TestCase, main


def add(a, b):
    if a and b:
        return a + b


class TestAddFunction(TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_None(self):
        self.assertEqual(add(1, None), None)


if __name__ == '__main__':
    main()
