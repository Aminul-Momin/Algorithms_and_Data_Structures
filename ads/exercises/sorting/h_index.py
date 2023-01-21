""" Computing the h-index.- [EPI:13.3]. """


def h_index(citations):

    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0


def main():
    pass


if __name__ == '__main__':
    main()
