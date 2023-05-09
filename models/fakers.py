from random import randint
from faker import Faker


def random_number(start: int = 100, end: int = 1000) -> int:
    return randint(start, end)


def random_string() -> str:
    return Faker().first_name()


def random_url() -> str:
    return Faker().dga()


if __name__ == "__main__":
    print(random_number())
    print(random_string())
    print(random_url())
