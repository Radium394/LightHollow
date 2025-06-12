import json
from pathlib import Path

SETTINGS_PATH = Path("settings.json")
DEFAULT_SETTINGS = {
    "Traning": True,
    "one": False,
    "two": 80
}

def colored_print(text: str, color: str | int = "red") -> None:
    color_map = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "purple": 35,
        "cyan": 36,
        "white": 37,
        "gray": 90,
        "bright_red": 91,
    }

    if isinstance(color, int):
        ansi_code = color
    else:
        ansi_code = color_map.get(color.lower(), 31)

    print(f"\033[{ansi_code}m{text}\033[0m")






def pos():
    while True:
        num = input("Введите координату: ")
        pos = num.split()

        if any(c.isalpha for c in num) == True:
            colored_print('\nВ данных значениях не должно содержатся букв и символов\n', 31)
            continue

        if len(pos) > 6:
            colored_print("\nПревышено количество значений. Имеются только X Y Z и повороты rX rY и наклон rZ для некоторых функций\n", "red")
            continue

        return pos
        break


pos()
while True:
    colored_print("\n------------------------\nMenu", 36)
    colored_print("1 - Скриптинг\n2 - Создать главного персонажа\n0 - Настройки\n","blue")
    num = input("Ввод: ")
    if num == "1":
        print("1 - Скриптинг")
    elif num == "2":
        print("2 - Создать главного персонажа")
    elif num == "0":
        colored_print("0 - Настройки")
    else:
        print("Не верный ответ. Попробуйте снова")

