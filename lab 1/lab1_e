def search(lst, key, i=0):
    if i == len(lst):
        return False
    if lst[i] == key:
        return True
    return search(lst, key, i + 1)

ids = list(map(int, input("Enter employee IDs: ").split()))
key = int(input("Enter ID to search: "))

if search(ids, key):
    print("Employee ID found")
else:
    print("Employee ID not found")
