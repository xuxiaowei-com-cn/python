unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
unprinted_designs_copy = unprinted_designs[:]
completed_models = []

while unprinted_designs_copy:
    current_design = unprinted_designs_copy.pop()
    print(f"Printing model：{current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed：")
for completed_model in completed_models:
    print(completed_model)

print(f"原列表：{unprinted_designs}")
