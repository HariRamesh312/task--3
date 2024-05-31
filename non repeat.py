def count(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    for key, value in frequency.items():
        if value == 1:
            print(key)
arr = [10, 89, 45, 67, 18, 45, 50, 10]
count(arr)