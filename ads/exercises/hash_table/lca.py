"""
Problem 9.4 on Page 118 is concerned with computing the LCA in a binary tree with parent pointersin time proportional to the height of the tree. The algorithm presented in Solution 9.4 on Page 118 entails traversing all the way to the root even if the nodes whose LCA is being computed are very close to their LCA. Design an algorithm for computing the LCA of two nodes in a binary tree. The algorithm's time complexity should depend only on the distance from the nodes to the LCA. 
Hint: Focus on the extreme case described in the problem introduction.
"""
#==============================================================================