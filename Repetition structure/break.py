counter = 1
total = 0

while True:
    total = 2**counter
    print(total)
    counter += 1
    if total > 100:
        break
# break is used to stop the while
