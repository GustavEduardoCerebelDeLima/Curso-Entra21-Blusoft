# key : value

dic = {'cairo': ['é', 'lindo'],
       'mark': ['5', '6'],
       'count': ['7', '8']
       }

# print(dic)
# print(dic['cairo'][0])
# print(dic.get('ca', 'does not exist'))

# dic['cairo'] = ['pretty']
# dic['cairo2'] = ['10'] # add always in the end of the dic
# dic.update({'n1': 10}) # we can use with more than one key

# dic['num'] = dic.pop('count')
# del dic['num']
# print(dic)
# print(dic.keys())
# print(dic.values())

# for i in dic:
#     print(i) # keys
#     print(dic[i]) # values

# for k, v in dic.items():
#     print(f'{k} - {v}')
#
# dic.pop('count')
# print(dic.values())

# dic.popitem()
# print(dic.values())

# if '2' in dic:           # we verify if that key is in the dic
#     print('found it')
# else:
#     print('none')

# if ['7', '8'] in dic.values():
#     print('found it')
# else:
#     print('none')

# keys = 0
# value = 0
# new_dic = dict.fromkeys(keys, value)
# print(new_dic)

# l1 = [1, 2, 3, 4]
# l2 = ['a', 'b', 'c', 'd']
# dic2 = {}
#
# for i in range(len(l2)):
#     dic2[l1[i]] = l2[i]
# # print(dic2)
#
# dic3 = {**dic, **dic2}
# print(dic3)
#
# dic.clear()
# print(dic)