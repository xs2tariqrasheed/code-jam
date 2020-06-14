# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

arr = [10, 15, 3, 7]
k = 17

possible_members = dict()

for x in arr:
    possible_members[str(x)] = k - 10

for x in arr:
    if possible_members[str(x)] == k - x:
        print (x, possible_members[str(x)])
        break;
        