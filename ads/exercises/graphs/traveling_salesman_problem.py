"""
Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?


Problem: Determine an optimal tour in a weighted, directed graph. The weights are nonnegative numbers.
Inputs: a weighted, directed graph, and n, the number of vertices in the graph. The graph is represented by a two-dimensional array W , which has both its rows and columns indexed from 1 to n, where W [i] [j] is the weight on the edge from the ith vertex to the jth vertex.
Outputs: variable minlength, whose value is the length of an optimal tour, and
variable opttour, whose value is an optimal tour.

Note: Best-First Search is not the same as Breadth-First Search
"""