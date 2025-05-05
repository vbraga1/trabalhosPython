# print("Hello")
# num_char = len("Hello")
# print(num_char)
#
# def minha_funcao():
#     print("Hello")
#     print("Bye")
#
# minha_funcao()

#-----------------------------------------------------------------------------------------------------------------------

# CÓDIGO DO JOGUINHO DO LABIRINTO E DO ROBÔ
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# while not at_goal():
#     if front_is_clear() and not wall_on_right():
#         turn_right()
#         move()
#         while front_is_clear():
#             move()
#     elif not wall_on_right() and wall_in_front:
#         turn_right()
#         move()
#         if front_is_clear() and wall_on_right():
#             move()
#         elif is_facing_north() and front_is_clear():
#             move()
#         elif not wall_on_right():
#             turn_right()
#             move()
#     elif not wall_on_right() and not at_goal():
#             turn_right()
#             move()
#     elif wall_in_front() and wall_on_right():
#         turn_left()
#     elif wall_in_front() and not wall_on_right():
#         turn_right()
#         move()
#     else:
#         move()