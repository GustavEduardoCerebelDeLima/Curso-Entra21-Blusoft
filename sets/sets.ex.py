# ex 1
old = open('clientes sistema antigo.txt', 'r').read().splitlines()
new = open('clientes sistema novo.txt', 'r').read().splitlines()

total_list = old + new

double = set()
for i in total_list:
    if total_list.count(i) > 1:
        double.add(i)

# print(f'Total of duplicated: {len(double)}')
# print(f'total of registers: {len(total_list)}')
# print(f'Old ones: {len(old)}')
# print(f'New ones: {len(new)}')
# print(f'Unics: {len(set(total_list))}')

# ex 2
# print(f'{len(total_list) - len(set(total_list))}')

# ex 3
# print(f'duplicated: {double}')

# ex 4
# print(f'Unics: {len(set(total_list))}')
