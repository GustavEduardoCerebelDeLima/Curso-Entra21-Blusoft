# ex 5
a = open('Candidato A.txt', 'r').read().splitlines()
b = open('Candidato B.txt', 'r').read().splitlines()

total_votes = a + b
print(f'Total votes: {len(total_votes)}')
print(f'votes in A {len(a)}')
print(f'votes in B: {len(b)}')

# ex 6
if len(a) > len(b):
    print(f'The A candidate won!\n')
elif len(a) < len(b):
    print(f'The B candidate won!\n')
else:
    print('Tied the election!\n')


# ex 7
print(f'Replicated: {len(set(a).intersection(set(b)))}')

# ex 8
people_vote = 108 - len(set(a).intersection(set(b)))
print(f'{people_vote} people voted and {100 - people_vote} did not voted\n')

# ex 9
print(f'A candidate votes: {len(set(a))}')
print(f'B candidate votes: {len(set(b))}')
print(f'Total votes: {len(set(a)) + len(set(b))}')

if len(set(a)) > len(set(b)):
    print(f'The A candidate won!')
elif len(set(a)) < len(set(b)):
    print(f'The B candidate won!')
else:
    print('Tied the election!')


