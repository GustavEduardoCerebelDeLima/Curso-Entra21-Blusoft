# def triangle():
#     l = []
#     try:
#         for i in range(1, 4):
#             side = float(input(f"type the size of the first side{i} of a triangle: "))
#             l.append(side)
#             if (l[0] + l[1]) >= l[2] or (l[1] + l[2]) >= l[0] or (l[0] + l[2]) >= l[1] and l[0] == l[1] != l[2] or l[0] == l[2] != l[1] or l[2] == l[1] != l[0]:
#                 return"This is a isosceles triangle!"
#             elif (l[0] + l[1]) >= l[2] or (l[1] + l[2]) >= l[0] or (l[0] + l[2]) >= l[1] and l[0] == l[1] == l[2]:
#                 return "this is a equilateral triangle"
#             elif (l[0] + l[1]) >= l[2] or (l[1] + l[2]) >= l[0] or (l[0] + l[2]) >= l[1] and l[0] != l[1] != l[2]:
#                 return "this is a scalene triangle"
#             else:
#                 return"this not a triangle"
#     except:
#         pass

#======================================================================================================

# ex 2 def
# def letter(word, times):
#     return word.count(times)

#======================================================================================================

#ex 3 def
# def rev(num):
#     return num[::-1]

#======================================================================================================

#ex 4 def
# def digits(num):
#     cont = 0
#     for i in num:
#         cont += 1
#     return cont

#======================================================================================================

# ex 5 lista defs

# import random
# import time
#
# while True:
#     points = 0
#     bot_points = 0
#     play_list = []
#
#     for i in range(3):
#         jkp = input("Let's play JOKENPO! best of 3! choose between rock, paper, scissors: ")
#         play_list.append(jkp)
#         try:
#             if play_list[0] == play_list[1] or play_list[1] == play_list[2]:
#                 print("you CAN NOT choose rock 2 times!")
#                 break
#         except:
#             pass
#
#
#         print("JO...", end="")
#         time.sleep(1)
#         print("KEN...", end="")
#         time.sleep(1)
#         print("PO")
#
#
#         def choice():
#             if jkp == f"rock":
#                 return f"\nyou choose ROCK! Let's see what's the opponent choose!\n"
#             elif jkp == "paper":
#                 return f"\nyou choose PAPER! Let's see what's the opponent choose!\n"
#             elif jkp == "scissors":
#                 return f"\nyou choose SCISSORS! Let's see what's the opponent choose!\n"
#
#
#         jpk_list = ["rock", "paper", "scissors"]
#         bot = random.choice(jpk_list)
#
#
#         def winner():
#             if bot == jkp:
#                 return "\ntied the game!"
#             elif jkp == "rock" and bot == "paper" or jkp == "paper" and bot == "scissors" or jkp == "scissors" and bot == "rock":
#                 return "\nyou LOST the turn!"
#             else:
#                 return "\nyou WON the turn!"
#
#
#         print(f"{choice()}")
#         print(f"the opponent choice was {bot.upper()}!")
#         print(f"{winner()}! Let's play another turn\n")
#
#         if bot == jkp:
#             continue
#         elif jkp == "rock" and bot == f"paper" or jkp == "paper" and bot == "scissors" or jkp == "scissors" and bot == "rock":
#             points += 1
#         else:
#             bot_points += 1
#
#     print(f"you got {points}! and the bot got {bot_points}")
#     if points > bot_points:
#         print("YOU WON THE GAME!")
#     elif points == bot_points:
#         print("THE GAME TIED!")
#     else:
#         print("THE BOT WON THE GAME!")
#
#     option = input("\ndo you want to keep playing? (1) YES (2) NO: ").upper()
#     if option != "YES":
#         break

