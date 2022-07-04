# # part 1
# list2 = []
#
# while True:
#     while True:
#         list1 = input("type a list ('done' you can stop):  ")
#         if list1 == "done":
#             break
#         list2.append(list1)
#     list2.sort()
#     print(list2)
#     list2.sort(reverse=True)
#     print(list2)
#     list2 = list(map(int, list2))
#     soma = sum(list2)
#     print(soma)
#     mean = sum(list2) / len(list2)
#     print(mean)

# part 2
# list1 = []
# while True:
#         while True:
#             name = str(input("type the names: "))
#             if name == "done":
#                 break
#             list1.append(name)
#         list1.sort()
#         print(list1)
#         list1.sort(reverse=True)
#         print(list1)
#         print(f"We registered: {len(list1)} people")
#         print(list1.count("carlos"))

# part 3

# list1, integer, float_num, string_, bool_ = [], 0, 0, 0, 0
#
# while True:
#     while True:
#         aleatory = input("type something aleatory value: ")
#         if aleatory == "done":
#             break
#         list1.append(aleatory)
#
#     for i in range(len(list1)):
#         try:
#             list1[i] = int(list1[i])
#             integer += 1
#         except:
#             try:
#                 list1[i] = float(list1[i])
#                 float_num += 1
#             except:
#                 try:
#                     if list1[i] == "True" or list1[i] == "False":
#                         bool_ += 1
#                     else:
#                         string_ += 1
#                 except:
#                     print("error")
#                     break
#
#     list1.reverse()
#     print(list1)
#     print(f"\nIntegers: {integer}")
#     print(f"Floats: {float_num}")
#     print(f"Strings: {string_}")
#     print(f"Bools: {bool_}\n")

