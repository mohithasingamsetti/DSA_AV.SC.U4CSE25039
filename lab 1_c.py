def search_employee(id_list, target_id):
    if not id_list:
        return False
    if id_list[0] == target_id:
        return True
    return search_employee(id_list[1:], target_id)
employee_ids = [2327, 6980, 1023, 9014, 9398]

print(search_employee(employee_ids, 2327))
print(search_employee(employee_ids, 2324))
