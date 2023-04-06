# The Fibonacci sequence is 0, 1, 1, 2, 3, 5, ... where each
# subsequent number is equal to the the preceeding two.
# This means the next elements in the list above would be 8 (5 + 3)
# and 13 (8 + 5)
#
# The 9th element in the sequence is 21. Let's call this the `current` value.
# The 8th element in the sequence is 13. Let's call this the `last` Value.
#
# Using PARALLEL ASSIGNMENT/TUPLE UNPACKING, perform the following operations
# in a single statement
#   1. replace the value of `current` with the value of the 10th
#       element in the sequence (so the sum of the 8th and 9th element)
#   2. replace the value of `last` with the value of the 9th element

# Leave this here
current = 21 # at this point, the 9th element of the sequence
last = 13 # at this point, the 8th element of the sequence
# Now, use parallel assignment to replace the value of `current` and `last`
# (put your answer below)

current, last = current + last,current
print(current, last)