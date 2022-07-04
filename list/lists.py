list = [1, 2, 3, 4]
list2 = [1, 3, 4]
list3 = ["cairo", "is", "pretty"]
list4 =['a', 'r', 'a', 'r', 'a']


# list.extend(list2) == list.append(list2)
# list.insert(1, {"cairo"}) specific position
# list.remove(1) # the first value
# list.pop(0) # position or last element
# list.clear() == / list = [] == del list[:] / # clear the whole list
# list3.sort() == alphabetic order or size order
# list3.sort(reverse=True) == reverse of the order
# print(list4.count('a')) return how many times the element appears in the list
# list4.reverse() put the reverse order of the elements in a list
list.extend(list2)
print(list)