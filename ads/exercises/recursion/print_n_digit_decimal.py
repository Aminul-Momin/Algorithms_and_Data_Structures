""" Implement a program that prints all the n-digits decimal numbers. """


def print_decimal(digits: int) -> None:
    def _print_decimal(digits: int, prefix: str) -> None:
        if digits == 0:
            print(prefix)
        else:
            for i in range(10):
                _print_decimal(digits - 1, prefix + str(i))

    prefix = ''
    _print_decimal(digits, prefix)


def main():
    num_of_digits = 4  # randint(4, 16)
    print_decimal(num_of_digits)


if __name__ == '__main__':
    main()
