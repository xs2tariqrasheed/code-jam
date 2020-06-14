# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

arr = [10, 15, 3, 7]
k = 17

possible_pairs = dict()

for x in arr:
    possible_pairs[str(x)] = k - 10
    if possible_pairs[str(x)] == k - x:
        print (x, possible_pairs[str(x)])
        break;
