from colorama import Fore, Back, Style, init
import os

init()


def pos():
    while True:
        num = str(input("Введите координату: "))
        pos = num.split()

        if any(c.isalpha for c in num) == True:
            print(Fore.RED + '\nВ данных значениях не должно содержатся букв и символов\n')
            continue

        if len(pos) > 6:
            print(Fore.RED + "\nПревышено количество значений. Имеются только X Y Z и повороты rX rY и наклон rZ для некоторых функций \n")
            continue

        return pos
        break

print(pos())