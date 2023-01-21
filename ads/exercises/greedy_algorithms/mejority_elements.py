"""
Several applications require identification of elements in a sequence which occur more than aspecified fraction of the total number of elements in the sequence. For example, we may wantto identify the users using excessive network bandwidth or IP addresses originating the mostHypertext Transfer Protocol (HTTP) requests. Here we consider a simplified version of this problem.

You are reading a sequence of strings. You know a priori that more than half of the strings are repetitions of a single string but the positions where the majority element occurs are unknown. Write a program that makes a single pass over the sequence and identifies the majority element. For example, if the input is <b,a,c,a,a,b,a,a,c,a>, then a is the majority element (it appears in 6 out of the 10 places).

Hint: Take advantage of the existence of a majority element to perform elimination.
"""