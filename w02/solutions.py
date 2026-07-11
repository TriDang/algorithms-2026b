# Problem 1
# The running time of your algorithm is: T(N) = 999*N + SQRT(N)
# Prove that T(N) = O(N^2)

# T(N) = 999*N + SQRT(N)

# Choose C = 1000 and N0 = 1, we have

# T(N) = 999*N + SQRT(N) <= 999*N + N = C*N <= C*(N^2), for N >= N0

# Therefore C*(N^2) is the upper bound on T(N)
# => T(N) = O(N^2)

# ====
# Notes: you can use the same process to prove that

# T(N) = O(N^3)
# T(N) = O(N*lg(N))
# T(N) = O(N)

# but not

# T(N) = O(lg(N))
# T(N) = O(SQRT(N))

##########################################

# Problem 2
# Implement an algorithm that prints out all the unique elements in a list (without using a dictionary).
# What is the complexity of your algorithm?

# Approach 1: without sorting

X = [6, 8, 10, 11, 6, 10]
for i in range(len(X)):
    is_unique = True
    for j in range(i):
        if X[i] == X[j]:
            is_unique = False
            break
    if is_unique:
        print(X[i])

# Complexity: O(N^2)

# Approach 2: with sorting

X = [6, 8, 10, 11, 6, 10]
X.sort()
for i in range(len(X)):
    if i == 0 or X[i] != X[i - 1]:
        print(X[i])

# Complexity: O(N*log(N))

##########################################

# Problem 3
# Given the arrival and departure time of planes reaching a particular airport.
# You need to find the minimum number of gates required to accommodate the planes at any point in time.
# Implement a solution and find the complexity of your algorithm.

arrivals = [150, 100, 200, 400, 215, 140]
departures = [220, 110, 230, 600, 315, 300]

arrivals.sort()
departures.sort()

arrival_index, departure_index, max_gates, current_gates = 0, 0, 0, 0

while arrival_index < len(arrivals) and departure_index < len(departures):
    if arrivals[arrival_index] < departures[departure_index]:
        current_gates += 1
        max_gates = max(max_gates, current_gates)
        arrival_index += 1
    else:
        current_gates -= 1
        departure_index += 1

print("The number of gates required is", max_gates)

# Complexity = O(N*log(N)) due to sorting, where N is the number of planes

##########################################

# Problem 4
# Given a list of numbers (size >= 2), find two elements in the list whose sum is closest to zero.
# Implement a solution and find the complexity of your algorithm.

def find_closest_to_zero(A):
    A.sort()  # Sort the list first
    left, right = 0, len(A) - 1
    closest_sum = float('inf')  # Initialize closest sum to infinity
    closest_pair = (None, None)  # Initialize closest pair

    while left < right:
        current_sum = A[left] + A[right]

        if abs(current_sum) < abs(closest_sum):  # Check if this pair is closer to zero than previous closest pair
            closest_sum = current_sum
            closest_pair = (A[left], A[right])

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_pair

X = [-100, 50, -52, 99]
print(find_closest_to_zero(X))  # Output: (-100, 99)

X = [-200, 190, -100, -5, 0, 3, -98, 6]
print(find_closest_to_zero(X))  # Output: (-5, 6)

# Complexity = O(N*log(N)) due to sorting, where N is the number of elements in the list

# Correctness Proof
# After sorting, we have X1, X2, ..., Xn such that X1 <= X2 <= ... <= Xn
# Assume that the closest pair is (Xi, Xj) where i < j
# We have to prove that during the while loop, the two pointers will eventually point to Xi and Xj at the same time
# Assume at a given time, the left pointer point to Xi and the right pointer point to Xk where k > j
# We have to prove that the left pointer remain at Xi and the right pointer will move to Xj

# We have two cases:

# Case 1: Xi + Xk > 0
# In this case, the right pointer will move to X(k-1) and so on until it reach Xj

# Case 2: Xi + Xk < 0
# We have Xi + Xj < Xi + Xk < 0 => abs(Xi + Xj) > abs(Xi + Xk) => the closest pair is NOT (Xi, Xj), which is a contradiction. As such, this case is not possible
##########################################

# Problem 5

# You develop an application that can track users' movement
# The application complexity is O(N^3) (N is the number of users)
# It takes 100 msec to run data for 1,000 users
# How many days it will take your application to run for 1,000,000 users?

# Time for 1,000 users = 100 msec
# Time for 1,000,000 users = 100 msec * (1,000,000 / 1,000)^3
# Convert time to days
time_in_days = 100 * (1_000_000 / 1_000) ** 3 / (1000 * 60 * 60 * 24)
print(f"Time to run for 1,000,000 users: {time_in_days}")
