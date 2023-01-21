from random import randint, randrange, choices
import json, os
from typing import Container, List, Iterable, Sequence, Optional, Callable

from ..fundamentals.singly_linked_list import SLL
from ..fundamentals._nodes import *
from ..searching.bst_st import BinarySearchTreeST
from ..searching.bst import AVL, BST
from ..searching._nodes import BSTNode
# =============================================================================
ARRAY_FOR_TREE = [10, 5, 13, 3, 7, 11, 14, 2, 4, 6, 8, 15, 16]

NUMBERS = {
    "ZERO": 0,
    "TEN": 10,
    "TWENTY": 20,
    "THIRTY": 30,
    "FORTY": 40,
    "FIFTY": 50
}
ZIP_CODES = {
    'Lower East Side': 10003,
    'Lower Manhattan': 10004,
    10003: 'Lower East Side',
    10004: 'Lower Manhattan'
}
COLORS = sorted([
    "RED", "GREEN", "BLACK", "BLUE", "WHITE", "PINK", "YELLOW", "CYAN",
    "MAGENTA", "GRAY", "BISQUE", "AZURE", "AQUA", "BEIGE"
])
# =============================================================================


def swap(array: List[Sequence], i: int, j: int) -> None:
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def is_sorted(array):
    ''' Return True if the given list is sorted. '''
    for i in range(len(array) - 1, 0, -1):
        if array[i] < array[i - 1]:
            return False
    return True


def gen_rendom_matrix(m=5, n=5):

    M1 = [[randrange(10, 100) for _ in range(m)] for _ in range(n)]
    M2 = [[0] * m for _ in range(n)]
    M3 = [[0] * m] * n
    assert M2 == M3
    assert M2 is not M3
    return M1


def print_matrix(M):
    for _list in M:
        print(_list)


def reverse(a: List, low: int, high: int) -> None:
    """Reverse python sequence object in place.

    This function reverse the portion of `a` starting from index `low` to
    'high` (high inclusive).

    Args:
        a (List)  : An subscriptable and mutable python object like list.
        low (int) : The first index in `a`.
        high (int): The last index in `a`.
    """
    if len(a) == 0 or low < 0 or high >= len(a):
        raise IndexError("len(a) == 0 or low < 0 or high >= len(a)")

    while low < high:
        a[low], a[high] = a[high], a[low]
        low += 1
        high -= 1


def rotate_list(a: list, rotate_amount: int) -> None:
    """Rotate a list to right by `rotate_amount`.

    Args:
        a: The list to be ratated.
        rotate_amount: The amount by which `a` to be rotated.

    Raises:
        IndexError: if the given list `a` is None.
    """
    if not a:
        raise IndexError("Unable to rotate an empty object")
    rotate_amount %= len(a)

    reverse(a, 0, len(a) - 1)
    reverse(a, 0, rotate_amount - 1)
    reverse(a, rotate_amount, len(a) - 1)

# Not Completed yet!
def gen_list_of_words(n=50, **kwargs):
    """Generates list of words from a file of text.

    Args:
        n (int): The number of words to be generated.
        **dir_name (str) : The basepath of the project repository. Default
                           to `os.path.abspath(".") + '/data/'`.
        
        **word_file_name (str): The name of text file containing data.
                           Default to `tongue_twisters.txt`.

    Returns:
        List of words.
    """
    kwargs = {
        'dir_name': os.path.abspath(".") + '/data/',
        'word_file_name': 'tongue_twisters.txt',
        **kwargs
    }

    DATA_PATH = kwargs["dir_name"] + kwargs["word_file_name"]
    with open(DATA_PATH) as f:
        list_of_words = f.read().split()

    return choices(list_of_words, k=n)


def gen_bt(L):
    def _gen_bt(L, low, high):
        if low > high: return None
        mid = (low + high) // 2
        x = BSTNode(None, L[mid])
        x._left = _gen_bt(L, low, mid - 1)
        x._right = _gen_bt(L, mid + 1, high)
        return x

    return _gen_bt(L, 0, len(L) - 1)


def gen_bst(seq: Iterable = None, **kwargs: str):
    """Generate a Binary Search Tree (`BST` or `AVL`).

    This function generates Binary Search Tree taking the elements of given
    'seq' as it's elements if the `seq` is given else it generates a Binary
    Search Tree of random integer of size fifteen.

    Returns:
        BSTNode: The root of BST, if **tree_type is not specified.
        AVLNode: The root of BST, If **tree_type=AVL

    Raises:
        TypeError: If the given parameter `seq` is not Iterable.
    """

    kwargs = {"bst_type": BST, 'size': 15, **kwargs}
    bst = kwargs["bst_type"]()
    SIZE = kwargs['size']

    if kwargs['bst_type'] == AVL:
        for _ in range(SIZE): bst.insert(randint(-10, 10))
    elif seq:
        if not hasattr(seq, "__iter__"): raise TypeError("`seq` is not Iterable!")
        for item in seq: bst.insert(item)
    else:
        for elm in ARRAY_FOR_TREE: bst.insert(elm)
    return bst._root


def gen_bst_st(seq: Iterable = ARRAY_FOR_TREE, **kwargs: str):
    """Generate a Symbol Table (`BinarySearchTreeST` or `AVLTreeST`).

    This function generates Symbol Table taking the elements of
    given 'seq' as key and random integers as value.

    Returns:
        BinarySearchST: By default, if **type is not specified.
        AVLTreeST     : If **type=AVLTreeST

    Raises:
        TypeError: If the given parameter `seq` is not a list.
    """
    if not hasattr(seq, "__iter__"):
        raise TypeError("seq is not Iterable!")

    kwargs = {"type": BinarySearchTreeST, **kwargs}

    st = kwargs['type']()

    for key in seq:
        st[key] = randint(0, 1000)

    return st._root


def get_subtree(x, key):
    if x is None:
        return None
    if key < x._key:
        return get_subtree(x._left, key)
    elif key > x._key:
        return get_subtree(x._right, key)
    else:
        return x


def gen_ll(seq: Iterable = ARRAY_FOR_TREE, **kwargs: str):
    """Generate a Linked List.

    Args:
        seq: Collection of items to generate linked list from
        ** type (Optional[LinkedList]): the linked list data type.
        ** size (int): number of items if 'seq' is None.
        ** has_cycle (bool): Whether generated list has cycle or not.

    returns:
        Generated Linked List.
    """
    kwargs = {"type": SLL, 'size': 15, 'has_cycle': False, **kwargs}

    sll = kwargs['type']()
    SIZE = kwargs['size']
    if seq is not None:
        for item in seq:
            sll.append(item)
    else:
        for _ in range(SIZE):
            num = randint(-15, 15)
            sll.append(num)
    if kwargs['has_cycle']:
        pass

    return sll


def green(s):
    # return '\033[01;32m%s\033[m' % s
    return "\033[01;5m  \033[01;32m %s \033[m  \033[m" % s


def yellow(s):
    return '\033[01;33m%s\033[m' % s


def red(s):
    # return '\033[01;31m%s\033[m' % s
    return "\033[01;5m  \033[01;31m %s \033[m  \033[m" % s


def load_json_data(test_package_name: str, **kwarg: Optional[str]) -> dict:
    """Load the required testing data for given 'test_package_name'.

    Args:
        test_package_name: Name of the testing package for which data is needed.
        
        **dir_name (str) : The basepath of the project repository. Default
                           to `os.path.abspath(".") + '/data/'`.
        
        **file_name (str): The name of jason file containing data.
                           Default to `ece.json`.

    Returns:
        Data to be used for testing the given package.
    """
    kwarg = {
        'dir_name': os.path.abspath(".") + '/data/',
        'file_name': 'ece_backup.json',
        **kwarg
    }

    DATA_PATH = kwarg["dir_name"] + kwarg["file_name"]
    kce_data = None

    with open(DATA_PATH) as f:
        kce_data = json.load(f)

    return kce_data[test_package_name]


def dump_data(mdul_key, data_key, new_data, **kwargs) -> None:
    """Dump 'new_data' into a json file.

    Args:
        mdul_key (str): The key associated to the data of each module.
        data_key (str): The key associated to the 'new_data'.
        new_data (list): The data which is to be dumped.

        **file_dir (str) : The basepath of the project repository. Default
            to `os.path.abspath(".") + '/data/'`.
        **file_name (str): The name of jason file containing data.
            Default to `ece.json`.
    """

    kwargs = {
        "file_dir": os.path.abspath(".") + '/data/',
        "file_name": 'ece.json',
        **kwargs
    }

    full_file_path = kwargs["file_dir"] + kwargs["file_name"]

    with open(full_file_path) as f:
        data = json.load(f)

    if data.get(mdul_key):
        data[mdul_key][data_key] = new_data
    else:
        data[mdul_key] = {}
        data[mdul_key][data_key] = new_data

    with open(full_file_path, 'w') as f:
        json.dump(data, f, indent=2)


def load_data_from_file(file_name: str, container: Container):
    """Add data from the file 'file_name' into the given container.

        It assumes the given file `file_name` is in data folder of this project.
        It also assumes the given container either has `append` or `__setitem__` attribute
        
    Args:
        file_name (str): the name of data file with file extention.
        container (Container): The collection into which data to be added.
    """

    # data = "Algorithms_and_Data_Structures/data/" + file_name
    # DATA_FILE_PATH = os.path.abspath(os.path.join(os.pardir, data))

    DATA_FILE_PATH = os.path.abspath(".") + '/data/' + file_name

    with open(DATA_FILE_PATH, encoding="utf-8") as f:  # Open the file

        value = 0
        while True:
            line = f.readline()
            if not line:
                break  # line is empty so exit
            for word in line.split():
                if hasattr(container, 'append'): container.append(word)
                elif hasattr(container, '__setitem__'): container[word] = value
                value += 1
        return container


def load_data_from_collection(collection, container):

    if type(collection) is dict:
        for key in collection.keys():
            container.put(key, collection[key])

    elif type(collection) is list:
        for item in collection:
            container.append(collection[item])


def dirpy(obj):
    """
    Display the name of the public members and attributes of an `obj`.
    """
    return list(
        filter(lambda x: not (x.startswith("__") or x.startswith("_")),
               dir(obj)))


def display_st(ST):
    print(f"""\t{"keys(): "} \t{ST.keys()}""")
    print(f"""\t{"root.key: "} \t{ST.root.key}""")
    print(f"""\t{"size(): "} \t{ST.size()}""")
    print(f"""\t{"height(): "} \t{ST.height()}""")
    print(f"""\t{"is_empty(): "} \t{ST.is_empty()}""")
    print(f"""\t{"contains('FORTY'): "} \t{ST.contains('FORTY')}""")
    print(f"""\t{"get('THIRTY'): "} \t{ST.get('THIRTY')}""")
    print(f"""\t{"select(3): "} \t{ST.select(3)}""")
    # print(f"""\t{"rank('THIRTY'): "} \t{ST.rank(ST.select(3))}""")
    print("\trank({}): \t{}".format(ST.select(3), ST.rank(ST.select(3))))
    print(f"""\t{"floor('TEEN'): "} \t{ST.floor('TEEN')}""")
    print(f"""\t{"ceiling('NINTYY'): "} \t{ST.ceiling('NINTYY')}""")

    print('\tkey-value pairs (IN-ORDER): ')
    for key in ST.keys():
        print(f"\t \t{key} \t{ST[key]}")


def name_of_module_scope():
    """
    Returns the name of the module scope.
    """
    return __name__

# FIXTURE_DIR = os.path.abspath(os.path.join(os.pardir, 'data'))

# @pytest.mark.datafiles(
#     os.path.join(FIXTURE_DIR, 'img1.jpg'),
#     os.path.join(FIXTURE_DIR, 'img2.jpg'),
#     os.path.join(FIXTURE_DIR, 'img3.jpg'),
# )
# def test_find_borders(datafiles):
#     for img in datafiles.listdir():
#         print(img)
#assert process(img) == some_expected_value

# def simple_test_AVLTreeST(data):
#     ST = AVLTreeST()
#     load_data_from_collection(data, ST)

#     print('*'*25, 'Before Mutation: ', '*'*25)
#     display_st(ST)

#     del ST["ZERO"]
#     del ST["FIFTY"]
#     ST.put("NINTY", 90)
#     ST['SIXTY'] = 60
#     del ST['TWENTY']

#     print('*'*25, 'After Mutation: ', '*'*25)
#     display_st(ST)

# @pytest.mark.skip(reason='Not complete yet !')
# def test_main():

#     if len(sys.argv) > 1:
#         simple_test_AVLTreeST(sys.argv[1])
#     else:
#         simple_test_AVLTreeST(NUMBERS)

# def simple_test_BinarySearchTreeST(data):
#     data_file_path = '../data/shellsST.txt'
#     ST = BinarySearchTreeST()
#     load_data_from_file(data_file_path, ST)

#     print("*"*25, "Before Mutation: ", "*"*25)
#     display(ST)

#     del ST["ZERO"]
#     del ST["FIFTY"]
#     ST.put("NINTY", 90)
#     ST["SIXTY"] = 60
#     del ST["TWENTY"]

#     print("*"*25, "After Mutation: ", "*"*25)
#     display(ST)
#     # for key in ST: del ST[key]
#     # for key in ST: del ST[key]

# def test_dunder_SequentialSearchST():
#     T1 = SequentialSearchST()
#     T1["Avocado"] = 10
#     T1["apple"] = 5
#     T1["Queens"] = "NYC"
#     T1["New York"] = "USA"
#     T1["Manhattan"] = "New York"
#     load_data("shellsST.txt", T1)
#     assert T1["apple"]
#     assert T1["Queens"]
#     assert len(T1) == 12

#     print("*" * 20, "Before Deletion: ", "*" * 20)
#     for key in T1.keys():
#         print(f"\t{key} \t{T1[key]}")
#     del T1["Queens"]
#     del T1["the"]
#     del T1["by"]
#     del T1["she"]
#     print("*" * 20, "After Deletion: ", "*" * 20)
#     for key in T1.keys():
#         print(f"\t{key} \t{T1[key]}")

# def test_SequentialSearchST(data):
#     ST = SequentialSearchST()
#     load_data(data, ST)

#     print("*" * 20, "Before Mutation: ", "*" * 20)
#     display(ST)

#     del ST["ZERO"]
#     del ST["FIFTY"]
#     ST.put("NINTY", 90)
#     ST["SIXTY"] = 60
#     del ST["TWENTY"]

#     print("*" * 20, "After Mutation: ", "*" * 20)
#     display(ST)
