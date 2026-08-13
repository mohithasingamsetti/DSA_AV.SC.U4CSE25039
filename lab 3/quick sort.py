def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in arr[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)

n = int(input("Enter the number of elements:"))

arr = []

for i in range(n):
    element = int(input(f"Enter element{i + 1}:"))
    arr.append(element)

arr = quick_sort(arr)

print("Sorted elements:", arr)
     
