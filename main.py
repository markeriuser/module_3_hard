def calculate_structure_sum(data_structure, total=0):
    for element in data_structure:
        if isinstance(element, (int, float)):
            total += element
        elif isinstance(element, str):
            total += len(element)
        elif isinstance(element, (list, tuple, set)):
            total = calculate_structure_sum(element, total)
        elif isinstance(element, dict):
            for key, value in element.items():
                total = calculate_structure_sum([key, value], total)
    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
