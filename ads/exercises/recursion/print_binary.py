""" Implement a program that prints all the n-bits binary numbers. """


def print_binary(bits: int) -> None:
    """Print all the n-bits numbers.

    Args:
        bits: Number of bits.
    """
    def _print_binary(bits: int, prefix: str) -> None:
        if bits == 0:
            print(prefix)
        else:
            _print_binary(bits - 1, prefix + '0')
            _print_binary(bits - 1, prefix + '1')

    prefix = ''
    _print_binary(bits, prefix)


def main():
    num_of_bits = 4  # randint(4, 16)
    print_binary(num_of_bits)


if __name__ == '__main__':
    main()
