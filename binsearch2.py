def binary_search(arr,target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
n = int(input("Enter the number of elements:"))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
target = int(input("Enter the element to search:"))
index = binary_search(arr,target)
print("Sorted array:",arr)
if index != -1:
    print(f"Element found at index {index} in the sorted array.")
else:
    print("Element not found.")
