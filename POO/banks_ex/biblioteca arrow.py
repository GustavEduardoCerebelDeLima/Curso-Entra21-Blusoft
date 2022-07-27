import arrow

date = arrow.now()
print(date)

date = arrow.now().format('DD/MM/YYYY')
print(date)

date = arrow.now().format('HH:mm')
print(date)

date = arrow.get(25) # it is reaching in seconds
print(date)

date_1 = arrow.get('2003-09-24 09:45:48', 'YYYY-MM-DD HH:mm:ss')
date_2 = arrow.get('2022-07-14 16:40:20', 'YYYY-MM-DD HH:mm:ss')
diff = date_2 - date_1
print(diff)
