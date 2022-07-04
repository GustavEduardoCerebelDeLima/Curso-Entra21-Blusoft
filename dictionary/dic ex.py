
# def situation():
#     if dic['mean'] <= 7 and dic['mean'] >= 10:
#         return "Situation: you haven't passed"
#     elif dic['mean'] < 0 or dic['mean'] > 10:
#         return"Invalid"
#     else:
#         return "Situation: you have passed"
#
#
# dic = {'name': input('type your name: '),
#        'mean': float(input('type your mean: '))
#        }
#
# print(f"Classmate: {dic['name']}")
# print(f"Mean: {dic['mean']}")
# print(f"{situation()}")

#==============================================EX2=====================================================================

# from random import randint
# from operator import itemgetter
#
# dic = {}
# for i in range(1, 5):
#     dic[f'player{i}'] = randint(1, 6)
#
# new_dic = sorted(dic.items(), key=itemgetter(1), reverse=True)
#
# for i, dic in enumerate(new_dic):
#     print(f'{i + 1} - {new_dic[i]}')

#==============================================EX3=====================================================================

dic = {'name': input('type your name: '),
       'age': 2022 - int(input('type the year you was born: ')),
       'CTPS': int(input('type the number of your work card: (if you dont have one, type 0) ')),
       'sex': int(input('type what sex you are (1) male (2) female: '))
       }


if dic['CTPS'] != 0:
       dic['wage'] = float(input('type the wage you got: '))
       dic['hiring'] = int(input('type the year of the hiring you got: '))
else:
       print("unemployed")

if dic['sex'] == 1 and dic['CTPS'] != 0:
       if (dic['age'] - dic['hiring']) >= 65 or (2022 - dic['hiring']) < 35:
              print(f"you can get your retirement")
       # else:
       #        print(f"{(2022 - dic['hiring']) - }")
elif dic['sex'] == 2:
       print(f"{62 - dic['hiring']} to get your retirement")

