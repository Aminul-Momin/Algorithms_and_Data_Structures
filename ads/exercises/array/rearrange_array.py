
"""Write a program that takes an array A of n numbers, and rearrange A's elements to get a new array B having that property that B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] ... .... - [EPI: 5.8]. """


def rearrange(A):

    for i in range(len(A)):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)
