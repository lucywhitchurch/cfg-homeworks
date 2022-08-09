"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""

"""
I made a few attempts at this questions. They work in different ways and do different things but none are able to complete
the task fully
"""

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

# def search_in_matrix(matrix, target):
#         for index, row in enumerate(matrix):
#             if target in row:
#              return index, row.index(target)
#             else:
#              return ('[-1,-1]')

""" This one seems to only loop through the first row of the matrix, I struggled to figure out how to loop through
each row in an efficient way"""

#  OR

# def search_in_matrix(matrix, target):
#     return [(index, row.index(target)) for index, row in enumerate(matrix) if target in row]

"""This returns the indices of the number in the matrix if it exists, but doesn't return [-1,-1] if not present"""


# # OR
#
def search_in_matrix(matrix, target):
    return [(index, row.index(target)) if target in row else '[-1,-1]' for index, row in enumerate(matrix)]

"""I think this may be the closest attempt."""

print(search_in_matrix(matrix=matrix, target=12))
print(search_in_matrix(matrix=matrix, target=33))