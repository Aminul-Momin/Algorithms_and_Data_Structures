from random import randint
try:
    # assumed 'ads' is installed from PyPI into running environment
    from ads.fundamentals import SLLNode, SLL
except (ImportError):
    # assumed data structures of 'ads' are imported into ece.utils.py somehow
    from ece.utils import SLLNode, SLL
#==============================================================================


def evaluate(expression):

    intr_res = []
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    for token in expression.split(DELIMITER):
        if token in OPERATORS:
            intr_res.append(OPERATORS[token](intr_res.pop(), intr_res.pop()))
        else:  # token is a number.
            intr_res.append(int(token))

    return intr_res[-1]


def main():

    expression = '2,+,3'
    res = evaluate(expression)
    print(res)


if __name__ == '__main__':
    main()
