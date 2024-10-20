"""
At Audible, a subscriber can gift an audiobook from his/her
library to another non-subscriber to kick start their
audiobook journey. The first time subscriber can receive
up to a maximun of N audiobooks from their friends/relatives.
When a non-subscriber receives a gift, we can infer that
two may be related. Similarly if the non-subscriber receives
gifted books from other two subscribers, we can infer that
all of them are related and the three of them form a group.
More formally, a group is composed of all of the people who know
one another, wheter directly or transitively. Audible would like your
help finding out the number of such distinct groups from the 
input data

Example
Consider the following input matrix M:
110
110
001

['1100', '1110', '0110', '0001']
"""

def countGroups(related):
    
    visited = set()
    groups = 0
    def dfs(i):
        visited.add(i)
        for j in range(len(related)):
            if related[i][j] == '1' and j not in visited:
                dfs(j)

    for i in range(len(related)):
        if i not in visited:
            dfs(i)
            groups += 1

    return groups

countGroups(['1100', '1110', '0110', '0001']) # Expected output: 2
