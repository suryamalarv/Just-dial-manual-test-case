arr = list(map(int, input()))

seen = set()
left = 0
max_len = 0

for right in range(len(arr)):

    while arr[right] in seen:
        seen.remove(arr[left])
        left += 1

    seen.add(arr[right])

    length = right - left + 1
    max_len = max(max_len, length)

print(max_len)