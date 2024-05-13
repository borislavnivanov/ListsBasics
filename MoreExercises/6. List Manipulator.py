# import typing
#
# even_numbers: list = []
# odd_numbers: list = []
#
#
# def even_odd(base_list: typing.List[int]) -> None:
#     global even_numbers, odd_numbers
#     even_numbers = [number for number in base_list if number % 2 == 0]
#     odd_numbers = [number for number in base_list if number % 2 != 0]
#
#
# def exchange_index(start_list: typing.List[int], _index: int) -> list:
#     if 0 <= _index < len(start_list):
#         exchanged_list = start_list[_index + 1:]
#         exchanged_list = exchanged_list + start_list[:_index + 1]
#         even_odd(exchanged_list)
#         return exchanged_list
#     else:
#         print('Invalid index')
#         return start_list
#
#
# def max_even_odd(base_list: typing.List[int], mode: str) -> None:
#     global even_numbers, odd_numbers
#     if mode == 'even':
#         if len(even_numbers) != 0:
#             max_num = max(even_numbers)
#             if base_list.count(max_num) == 1:
#                 print(base_list.index(max_num))
#             else:
#                 print(base_list[::-1].index(max_num))
#         else:
#             print('No matches')
#     elif mode == 'odd':
#         if len(odd_numbers) != 0:
#             max_num = max(odd_numbers)
#             if base_list.count(max_num) == 1:
#                 print(base_list.index(max_num))
#             else:
#                 print(base_list[::-1].index(max_num))
#         else:
#             print('No matches')
#
#
# def min_even_odd(base_list: typing.List[int], mode: str) -> None:
#     global even_numbers, odd_numbers
#     if mode == 'even':
#         if len(even_numbers) != 0:
#             min_num = min(even_numbers)
#             if base_list.count(min_num) == 1:
#                 print(base_list.index(min_num))
#             else:
#                 print(base_list[::-1].index(min_num))
#         else:
#             print('No matches')
#     elif mode == 'odd':
#         if len(odd_numbers) != 0:
#             min_num = min(odd_numbers)
#             if base_list.count(min_num) == 1:
#                 print(base_list.index(min_num))
#             else:
#                 print(base_list[::-1].index(min_num))
#         else:
#             print('No matches')
#
#
# def first_count_even_odd(base_list: typing.List[int], count: int, mode: str):
#     global even_numbers, odd_numbers
#     if mode == 'even':
#         if len(even_numbers) == 0:
#             print(even_numbers)
#         elif count <= len(base_list):
#             print(even_numbers[0:min(count,len(even_numbers))])
#         else:
#             print('Invalid count')
#     else:
#         if mode == 'odd':
#             if len(odd_numbers) == 0:
#                 print(odd_numbers)
#             elif count <= len(base_list):
#                 print(odd_numbers[0:min(count,len(odd_numbers))])
#             else:
#                 print('Invalid count')
#
#
# def last_count_even_odd(base_list: typing.List[int], count: int, mode: str):
#     global even_numbers, odd_numbers
#     if mode == 'even':
#         if len(even_numbers) == 0:
#             print(even_numbers)
#         elif count <= len(base_list):
#             print(even_numbers[-min(count, len(even_numbers)):])
#         else:
#             print('Invalid count')
#     else:
#         if mode == 'odd':
#             if len(odd_numbers) == 0:
#                 print(odd_numbers)
#             elif count <= len(base_list):
#                 print(odd_numbers[-min(count, len(odd_numbers)):])
#             else:
#                 print('Invalid count')
#
#
# text = str.split(input(), ' ')
# numbers = []
# for string in text:
#     numbers.append(int(string))
# even_odd(numbers)
#
# while True:
#     com = input()
#     if com == 'end':
#         print(numbers)
#         break
#     else:
#         com = str.split(com, ' ')
#
#     if com[0] == 'exchange':
#         numbers = exchange_index(numbers, int(com[1]))
#     elif com[0] == 'max':
#         max_even_odd(numbers, com[1])
#     elif com[0] == 'min':
#         min_even_odd(numbers, com[1])
#     elif com[0] == 'first':
#         first_count_even_odd(numbers, int(com[1]), com[2])
#     else:
#         first_count_even_odd(numbers, int(com[1]), com[2])

numbers = [int(integer) for integer in input().split()]
command = input().split()

while command[0] != "end":
    even_numbers = [even for even in numbers if even % 2 == 0]
    odd_numbers = [odd for odd in numbers if odd % 2 != 0]

    if command[0] == "exchange":
        if 0 <= int(command[1]) < len(numbers):
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print(f'Invalid index')

    elif command[0] == "max":
        if command[1] == "even" and even_numbers:
            print((len(numbers) - numbers[::-1].index(max(even_numbers)) - 1))
        elif command[1] == "odd" and odd_numbers:
            print((len(numbers) - numbers[::-1].index(max(odd_numbers)) - 1))
        else:
            print('No matches')

    elif command[0] == "min":
        if command[1] == "even" and even_numbers:
            print((len(numbers) - numbers[::-1].index(min(even_numbers)) - 1))
        elif command[1] == "odd" and odd_numbers:
            print((len(numbers) - numbers[::-1].index(min(odd_numbers)) - 1))
        else:
            print('No matches')

    elif command[0] == "first":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even_numbers[0:int(command[1])])
            else:
                print(odd_numbers[0:int(command[1])])
        else:
            print(f"Invalid count")

    elif command[0] == "last":
        if 0 < int(command[1]) <= len(numbers):
            if command[2] == "even":
                print(even_numbers[-int(command[1]):])
            else:
                print(odd_numbers[-int(command[1]):])
        else:
            print(f"Invalid count")
    command = input().split()

print(numbers)