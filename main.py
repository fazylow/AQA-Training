def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number


def extra_case(x):
    storage = {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0}
    for numbers in x:
        z = fizzbuzz(numbers)
        if z == "FizzBuzz":
            storage["FizzBuzz"] += 1
        if z == "Fizz":
            storage["Fizz"] += 1
        if z == "Buzz":
            storage["Buzz"] += 1
    return storage


## Am abordat un exercitiu simplu de fizz buzz in care am testat cazurile posibile si rezultatele, aditional am mai
## creeat o functie noua care primeste ca parametru o functie si are rolul de a trece toate numerele prin functia fizzbuzz
## iar rezultatele avand sa fie stocate intr-un dicionar care tine minte de cate ori "fizz" "buzz" au fost returnate de catre functia noastra si am testat si acest aspect.
