from parameterized import parameterized
from main import fizzbuzz
from main import extra_case


@parameterized.expand([
    (3, "Fizz"),  # testing fizz case with 2 examples
    (6, "Fizz"),

    (5, "Buzz"),  # testing buzz case with 2 examples
    (-5, "Buzz"),

    (15, "FizzBuzz"),  # testing fizzbuzz case with 2 examples
    (0, "FizzBuzz"),

    (2, "2"),  # testing the case in which the number is not divided by either 3 or 5
    (4, "4"),
    (7, "7"),
])
def test_fizzbuzz(number, expected_result):
    result = fizzbuzz(number)
    print(f" Testing number {number}, the expected result is {expected_result} and the result is {result}")
    assert str(result) == expected_result


@parameterized.expand([
    ([3, 5, 15, 20, 25], {"FizzBuzz": 1, "Fizz": 1, "Buzz": 3}),


    ([3, 9, 6], {"FizzBuzz": 0, "Fizz": 3, "Buzz": 0}),


    ([15, 30], {"FizzBuzz": 2, "Fizz": 0, "Buzz": 0}),


])
def test_extra_case(x, expected_result):
    result = extra_case(x)
    print(f" Testing outcome for {x}, the expected result is {expected_result} and the result is {result}")
    assert result == expected_result
