sample_list = ['p', 'q']
n = 5

new_list = [f'{element}{i}' for i in range(1, n+1) for element in sample_list]

print(new_list)
