# Problem 1
# 1.1 Algorithm to find the largest number in a list - without sorting the list
def find_largest(A):
    if not A:
        return None

    largest = A[0]  # Initialize largest to the first element

    for num in A:
        if num > largest:
            largest = num  # Update largest if current number is greater

    return largest

# test the function
print(find_largest([7, 6, 9, 3, 2, 5]))  # Output: 9
print(find_largest([-7, -2, -9, -1]))  # Output: -1
print(find_largest([1, 2, 3, 3, 2, 1]))  # Output: 3

# 1.2 Algorithm to find the second largest number in a list - without sorting the list
def find_second_largest(A):
    if len(A) < 2:
        return None  # Not enough elements for second largest

    largest = A[0]  # Initialize largest to the first element
    second_largest = A[1]  # Initialize second largest to the second element
    if second_largest > largest:  # Ensure largest is the larger of the two
        largest, second_largest = second_largest, largest

    for idx in range(2, len(A)):
        if A[idx] > largest:
            second_largest = largest  # Update second largest before updating largest
            largest = A[idx] # Update largest
        elif A[idx] > second_largest:  # Check if num is between largest and second largest
            second_largest = A[idx]

    return second_largest

# Example:
print(find_second_largest([7, 6, 9, 3, 2, 5]))  # Output: 7
print(find_second_largest([-7, -2, -9, -1]))  # Output: -2
print(find_second_largest([1, 2, 3, 3, 2, 1]))  # Output: 3


# Problem 2
# Algorithm to find the missing value in a list of N integers whose values are unique and from 0 to N

# Approach 1: check if 0 is missing, then check if 1 is missing, and so on until N is missing

# Approach 2: note that the sum of N integers is independent of the order of the integers. So, we can calculate the sum of all integers from 0 to N and subtract the sum of the integers in the list to find the missing value

def find_missing_value(A):
    N = len(A)  # N integers
    expected_sum = N * (N + 1) // 2  # Sum of integers from 0 to N
    actual_sum = sum(A)  # Sum of integers in the list (can use a for loop instead of sum function)
    missing_value = expected_sum - actual_sum  # The missing value is the difference
    return missing_value

print(find_missing_value([0, 3, 2, 4, 1]))  # Output: 5
print(find_missing_value([1, 5, 2, 4, 3]))  # Output: 0
print(find_missing_value([4, 0, 1, 5, 2]))  # Output: 3


# Problem 3
# Algorithm: Check if a string can be rearranged to form a palindrome: A string can be rearranged to form a palindrome if at most one character has an odd count.
# So, just count the frequency of each character. The data structure to use is a dictionary that map from character to its frequency.
# Something like: 'a': 3, 'b': 2, 'c': 6' means that the string has 3 'a's, 2 'b's, and 6 'c'.

def can_form_palindrome(s):
    # Count the frequency of each character in the string
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Check how many characters have an odd count
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # A string can form a palindrome if at most one character has an odd count
    return odd_count <= 1


# Problem 4
# Range sum query on a matrix (2D list)

matrix = [
  [1, 2, 3, 4, 5],
  [8, 6, 9, 1, 3],
  [8, 3, 1, 4, 3],
  [4, 8, 2, 9, 6]
]

# Approach 1: naive approach - iterate through all elements in the rectangle and calculate the sum
def range_sum_query(matrix, top, left, bottom, right):
    total_sum = 0

    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            total_sum += matrix[row][col]

    return total_sum

print(range_sum_query(matrix, 1, 2, 2, 3))  # Output: 15
print(range_sum_query(matrix, 1, 2, 3, 4))  # Output: 38

# Approach 2: precompute the prefix sum of the matrix to make the range sum query faster
# Define: prefix_sum2D[i][j] = sum of all elements in the rectangle defined by (0, 0) and (i, j)
# then, range_sum_query(top, left, bottom, right) = prefix_sum2D[bottom][right] - prefix_sum2D[top-1][right] - prefix_sum2D[bottom][left-1] + prefix_sum2D[top-1][left-1]

def compute_prefix_sum2D(matrix, queries):
    rows = len(matrix)
    cols = len(matrix[0])
    prefix_sum2D = [[0] * cols for _ in range(rows)]

    prefix_sum2D[0][0] = matrix[0][0]  # top left corner

    for col in range(1, cols):  # first row
        prefix_sum2D[0][col] = prefix_sum2D[0][col - 1] + matrix[0][col]

    for row in range(1, rows):  # first column
        prefix_sum2D[row][0] = prefix_sum2D[row - 1][0] + matrix[row][0]

    for row in range(1, rows):
        for col in range(1, cols):
            prefix_sum2D[row][col] = matrix[row][col] + prefix_sum2D[row - 1][col] + prefix_sum2D[row][col - 1] - prefix_sum2D[row - 1][col - 1]

    results = []
    for top, left, bottom, right in queries:
        total_sum = prefix_sum2D[bottom][right]
        if top > 0:
            total_sum -= prefix_sum2D[top - 1][right]
        if left > 0:
            total_sum -= prefix_sum2D[bottom][left - 1]
        if top > 0 and left > 0:
            total_sum += prefix_sum2D[top - 1][left - 1]
        results.append(total_sum)
    return results

print(compute_prefix_sum2D(matrix, [(1, 2, 2, 3), (1, 2, 3, 4)]))  # Output: [15, 38]
