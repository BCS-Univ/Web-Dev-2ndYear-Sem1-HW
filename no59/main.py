with open('no59/data.txt', 'r') as f:
    data = f.read().split('\n')

arrData = []    
for item in data:
    arrData.append(item.split(' '))

query = input('Enter query: ')
for i in range(len(arrData)):
    if query in arrData[i]:
        print(arrData[i])
        print('Found at line', i+1)
        break