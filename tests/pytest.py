from parameterized import parameterized
from main import fizzbuzz


@parameterized.expand([
    (3, "Fizz"),  # testing fizz case with 3 examples
    (6, "Fizz"),
    (9, "Fizz"),

    (5, "Buzz"),  # testing buzz case with 3 examples
    (-5, "Buzz"),
    (20, "Buzz"),

    (15, "FizzBuzz"),  # testing fizzbuzz case with 3 examples
    (0, "FizzBuzz"),
    (30, "FizzBuzz"),

    (2, "2"),  # testing the case in which the number is not divided by either 3 or 5
    (4, "4"),
    (7, "7"),
])
def test_fizzbuzz(number, expected_result):
    result = fizzbuzz(number)
    print(f" Testing number {number}, the expected result is {expected_result} and the result is {result}")
    assert str(result) == expected_result
