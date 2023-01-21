"""
Let s and t be strings and D a dictionary, i.e. a set of strings. Define s to produce t if there exists a sequence of strings from the dictionary P = <s0, s1, …, sn-1> such that the first string is s, the last string is t, and adjacent strings have the same length and differ in exactly one character. The sequence P is called a production sequence. For example, if the dictionary is {bat, cot, dog, dag, dot, cat}, then <cat, cot, dot, dog> is a production sequence.

Given a dictionary D and two strings s and t, write a program to determine if s produces t. Assume that all characters are lowercase alphabets. If s does produce t, output the length of the shortest production sequence; otherwise, output -1.

Hint: Treat strings as vertices in an undirected graph, with an edge between u and v if and only if the corresponding strings differ in one character.
"""
"""
Solution:
Create a graph according to the hint in time complexity O(n2). Traverse the graph using BFS in time O(|V| + |E|) = O(n + n2) = O(n2).

Note that we don’t need to necessarily “create” a graph per se; edges can be “discovered” ad-hoc by finding words in the dictionary that are one character off from the current vertex.
"""