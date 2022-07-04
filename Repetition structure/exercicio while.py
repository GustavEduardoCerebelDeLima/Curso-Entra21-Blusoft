# Question 5
# simulate a bank
# 3 accounts
# 3 diffrents passwords
# Check balance
# Pay the bill
# deposit to account
# Withdraw
# get out

# from random import randint
#
# while True:
#     check_balance, pay_the_bill, deposit_to_account, withdraw, get_out = 0, 0, 0, 0, 0
#     account = input("which is your account? (1) CAIXA account (2) BB account (3) NUbank account: ")
#     if account == '1':
#         CApassword = input("what is your password in CAIXA?: ")
#     elif account == '2':
#         BBpassword = input("what is your password in BB?: ")
#     elif account == '3':
#         NUpassword = input("what is your password in NUbank?: ")
#     else:
#         print("choose the option again")
#         account = input("which is your account? (1) CAIXA account (2) BB account (3) NUbank account: ")
#
#     if CApassword == "c1a2":
#         option = input("What do you want to do? (1) Check balance (2) Pay the bill (3) deposit to account (4) Withdraw (5) get out: ")
#     else:
#         print("The password is incorrect! Try it again")
#         CApassword = input("what is your password in CAIXA?: ")
#
#     if NUpassword == "b1b2":
#         option = input("What do you want to do? (1) Check balance (2) Pay the bill (3) deposit to account (4) Withdraw (5) get out: ")
#     else:
#         print("The password is incorrect! Try it again")
#         NUpassword = input("what is your password in CAIXA?: ")
#
#
#     if BBpassword == "b1b2":
#         option = input("What do you want to do? (1) Check balance (2) Pay the bill (3) deposit to account (4) Withdraw (5) get out: ")
#     else:
#         print("The password is incorrect! Try it again")
#         BBpassword = input("what is your password in CAIXA?: ")
#
#
#     if option == "1" and CApassword == "c1a2":
#         check_balance = randint(-10000, 10000)
#         print(f"Your balance is: {check_balance}")
#
#     if option == "2" and CApassword == "b1b2":
#         check_balance = randint(-10000, 10000)
#         print(f"Your balance is: {check_balance}")
#
#     if option == "3" and CApassword == "n1u2":
#         check_balance = randint(-10000, 10000)
#         print(f"Your balance is: {check_balance}")


# Question 8
# num_list, even_year, odd_year, years_future, years_past = [], 0, 0, 0, 0
#
# while True:
#     while True:
#         num = input("type the year: ")
#         num_list.append(num)
#         if num == "done":
#             break
#     num_list2 = num_list.remove("done")
#     num_list = list(map(int, num_list))
#
#     for i in range(len(num_list)):
#         if (num_list[i] % 4 == 0 and num_list[i] % 400 == 0) or num_list[i] % 100 != 0:
#             print(f"{num_list[i]} is a leap year")
#         else:
#             print(f"{num_list[i]} is a not leap year")
#
#         if num_list[i] % 2 == 0:
#             even_year += 1
#         else:
#             odd_year += 1
#
#         if num_list[i] < 2022:
#             years_future += 1
#         else:
#             years_past += 1
#     print(f"\nYears in the future: {years_future}")
#     print(f"Years in the past: {years_past}\n")
#     print(f"Even years: {even_year}")
#     print(f"Odds years: {odd_year}")
#     option = input("\nDo you want to continue? (1) YES (2) NO: ").upper()
#     if option != "YES":
#         break
