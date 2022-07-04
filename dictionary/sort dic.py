from operator import itemgetter

dic = {'1': 1,
       '2': 2,
       '3': 3
       }

new = sorted(dic.items(), key=itemgetter(1), reverse=True)
print(new)
#
# for i, j in enumerate(new): # == to for i, j in range(len(new)
#     print()

