arr = [1, -6, 0, 3, -3, 8, 2, 0, 4, 5]
n = len(arr)

for i in range(n):
    if arr[i] == 0:
        first = i
        break
for i in range(n-1, -1, -1):
    if arr[i] == 0:
        second = i
        break
_sum = 0
for i in range(first+1, second):
    _sum += arr[i]

print(_sum)



left_index = arr.index(0)
rigth_index = arr[::-1].index(0)

t_arr = arr[left_index : -rigth_index ]
print(sum(t_arr))