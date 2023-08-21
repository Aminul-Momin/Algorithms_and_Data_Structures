<p align="center"><img src="ads_logo.png"></p>

<h1 style="color: red" align="center">Algorithms and Data Structures</h1>

## How to install ?

If you want to use the API of `Algorithms and Data Structures` in your code, you can clone it from github as follows:

-   `$ git clone git@github.com:Aminul-Momin/Algorithms_and_Data_Structures.git`

How to install the project in edit mode?

-   `$ pip install -e .`

## How to use it?

After you have install the package, use it as follows.

```python
from ads.sortings import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort(my_list)
    print(my_list)
```

## How to test using [pytest](https://docs.pytest.org/en/latest/index.html)?

-   [Pytest API Reference](https://docs.pytest.org/en/latest/reference/reference.html#command-line-flags)
-   [How to invoke pytest](https://docs.pytest.org/en/latest/how-to/usage.html#specifying-which-tests-to-run)

-   `$ pytest [-q | -v]` → It will run all tests contained by files of the form `test_*.py` or `*_test.py` in the current directory and its subdirectories in quiet (`q`) or verbose (`v`) mode.
-   `$ pytest -k key_word` → run pytest by key (`k`) word expression
    -   `$ pytest -k test_searching.py` → Run pytest on the given module only.
    -   `$ pytest -k test_magic_index` → Run pytest on the given function (as key-word) only.
    -   `$ pytest -k -s test_avl_tree` → Use `-s` flag to allow to execute print statement in your test functions.
-   `$ pytest -m marker` → run all tests by marker (marked by `marker` using the `@pytest.mark.marker` decorator).
    -   `pytest -m parametrize` → run all tests by marker (marked by `parametrize` using the `@pytest.mark.parametrize` decorator).
    -   `pytest -m slow`
    -   `pytest -m xfail`
-   `$ python3 -m pytest tests/exercises/test_searching.py` → Run pytest on the given module only.
-   `$ pytest -v tests/my-directory/test_demo.py::test_specific_function` → To run a single test function, add double colon (`::`) and the test function name as above.

## How to format ?

-   `$ python -m black <file_name.py | package>` → Format the given file/package using `black`
-   `$ black ads/searching/avl_tree.py` → Formatting perticular module using black.

## List of Implemented Data Structures

-   [Fundamentals](ads/fundamentals/)

    -   [bag](ads/fundamentals/bag.py)
    -   [disjoint_sets](ads/fundamentals/disjoint_sets.py)
    -   [Stack](ads/fundamentals/stack.py)
    -   [resizing_array_queue](ads/fundamentals/resizing_array_queue.py)
    -   [resizing_array_stack](ads/fundamentals/resizing_array_stack.py)
    -   [doubly_linked_list](ads/fundamentals/doubly_linked_list.py)
    -   [singly_linked_list](ads/fundamentals/singly_linked_list.py)

-   [Sortings](ads/sorting/)

    -   [quick_sort](ads/sorting/quick_sort.py)
    -   [merge_sort](ads/sorting/merge_sort.py)
    -   [selection_sort](ads/sorting/selection_sort.py)
    -   [insertion_sort](ads/sorting/insertion_sort.py)
    -   [bullbe_sort](ads/sorting/bullbe_sort.py)

-   [Searching](ads/searching/)
    -   [Binary Search Tree](ads/searching/bst.py)
    -   [Binary Search Tree Symbol Table](ads/searching/bst_st.py)
    -   [AVL Tree Symbol Table](ads/searching/avl_tree_st.py)
    -   [Sequentiao Search Hash Table](ads/searching/sequential_search_st.py)
    -   [Linear Probing Hash Table](ads/searching/linear_probing_ht.py)
    -   [Seperate Chaining Hash Table](ads/searching/seperate_chaining_ht.py)
-   [Heaps](ads/heaps/)

    -   [Priority Queue](ads/heaps/priority_queue.py)
    -   [Min Priority Queue](ads/heaps/min_pq.py)
    -   [Indexed Min Priority Queue](ads/heaps/index_min_pq.py)

-   [String Processing](ads/string_processing/)
    -   [Tries](ads/string_processing/tries.py)
    -   [Ternary Search Tree](ads/string_processing/tst.py)
    -   [Substring Search](ads/string_processing/substring_search.py)
    -   [Knuth Morris Pret](ads/string_processing/KMP.py)
    -   [Suffix Array](ads/string_processing/suffix_array.py)
    -   [LSD Radix Sort](ads/string_processing/lsd_radix_sort.py)
    -   [MSD Radix Sort](ads/string_processing/msd_radix_sort.py)
    -   [Run Length](ads/string_processing/run_length.py)
-   [Graph Processing](ads/graphs_processing/)

    -   [Graph](ads/graphs_processing/clrs/graphs.py)
    -   [Depth First Search](ads/graphs_processing/clrs/dfs.py)
    -   [Depth First Search Order](ads/graphs_processing/clrs/dfs_order.py)
    -   [Cycle Detection](ads/graphs_processing/clrs/cycle_detection.py)
    -   [Directed Cycle](ads/graphs_processing/clrs/directed_cycle.py)
    -   [Undirected Cycle](ads/graphs_processing/clrs/undirected_cycle.py)
    -   [Dijkstra Shortest Path](ads/graphs_processing/clrs/dijkstra_sp.py)
    -   [Bellman Ford Shortest Path](ads/graphs_processing/clrs/bellman_ford.py)
    -   [Edges Classification](ads/graphs_processing/clrs/edges_classification.py)
    -   [Topological Sort](ads/graphs_processing/clrs/topological_sort.py)

-   [Exercises](ads/exercises/)
    -   Will be added in near future.

## Contributing

Thanks for your interest in contributing! There are no ways to contribute to this project currently. Please check back later.
