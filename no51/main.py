
sample_data = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# def sort_key(x):
#     return float(x[1])


# sorted_data = sorted(sample_data, key=sort_key, reverse=True)
sorted_data = sorted(sample_data, key=lambda x: float(x[1]), reverse=True)

print(sorted_data)
