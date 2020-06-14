# This problem was asked by Google.
# Given a sorted list of integers, square the elements and give the output in sorted order.
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

arr = [-11, -9, -2, 0, 2, 3, 10]
s_arr = []
n_index = 0
p_index = 0

for i in arr:
    if i >= 0:
        n_index = arr.index(i) - 1
        p_index = n_index + 1
        break

for z in range(0, len(arr)):
    if (n_index >= 0 and p_index < len(arr) and abs(arr[n_index]) < arr[p_index]) or p_index == len(arr):
        s_arr.append(abs(arr[n_index]) ** 2)
        n_index = n_index - 1
    elif p_index < len(arr) or n_index == -1:
        s_arr.append(arr[p_index] ** 2)
        p_index = p_index + 1
        

print(s_arr)