min_val = int(input())
max_val = int(input())
if min_val > max_val:
    tmp = min_val
    min_val = max_val
    max_val = tmp
max_length = 0
for i in range(min_val, max_val+1):
    val = i
    length = 1
    while val != 1:
        if val % 2 == 1:
            val = (val * 3) + 1
            length += 1
        else:
            val /= 2
            length += 1
    if max_length < length:
        max_length = length
print(min_val, max_val, max_length)