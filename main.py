import json
from pathlib import Path
import keyboard

SETTINGS_PATH = Path("settings.json")
DEFAULT_SETTINGS = {
    "traning": True,
    "scrept": False,
    "two": 80
}


def load_settings():
    """Загружает настройки или создаёт файл, если его нет"""
    if not SETTINGS_PATH.exists():
        with open(SETTINGS_PATH, 'w') as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)
        return DEFAULT_SETTINGS.copy()

    with open(SETTINGS_PATH) as f:
        settings = json.load(f)

    # Добавляем недостающие параметры
    for key, value in DEFAULT_SETTINGS.items():
        if key not in settings:
            settings[key] = value

    with open(SETTINGS_PATH, 'w') as f:
        json.dump(settings, f, indent=4)

    return settings


def get_setting(key):
    """Возвращает значение настройки по ключу"""
    settings = load_settings()
    return settings.get(key)


def set_setting(key, value):
    """Устанавливает значение для указанного параметра"""
    settings = load_settings()
    settings[key] = value
    with open(SETTINGS_PATH, 'w') as f:
        json.dump(settings, f, indent=4)


def toggle_setting(key):
    """Переключает булевы параметры (True/False)"""
    settings = load_settings()
    if key in settings and isinstance(settings[key], bool):
        settings[key] = not settings[key]
        with open(SETTINGS_PATH, 'w') as f:
            json.dump(settings, f, indent=4)
    else:
        print(f"Ошибка: параметр '{key}' не найден или не boolean.")


def show_settings():
    """Выводит текущие настройки."""
    settings = load_settings()
    print("\nТекущие настройки:")
    for key, value in settings.items():
        print(f"  {key}: {value}")


def colored_print(text: str, color: str | int = "red") -> None:
    """Цветной вывод текста с названием или кодом ansi"""
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


def settings():
    while True:
        print("\n -- НАСТРОЙКИ --\nВыберите что нужно изменить")
        print(f"1 - Режим туториала: {get_setting("traning")}")
        print("0 - Выход")
        num = int(input("Введите: "))
        if num == 1:
            if get_setting("traning") == True:
                set_setting("traning", False)
            elif get_setting("traning") == False:
                set_setting("traning", True)
        elif num == 0:
            break
        else:
            colored_print("Не верный ответ. Введите одну цифру.\nПример: 1", "red")






def pos():
    while True:
        num = input("Введите координату: ")
        pos = num.split()

        if not all(c.replace('-', '').isdigit() for c in pos if c):
            colored_print('\nВ данных значениях не должно содержаться букв и символов', "red")
            continue

        if len(pos) > 6 or len(pos) < 3:
            colored_print("\nПревышено количество значений. Имеются только X Y Z и повороты rX rY и наклон rZ для некоторых функций\nНе более 6 и не меньше 3.1" + f" У вас: {len(pos)}", "red")
            continue

        return pos
        break





while True:
    colored_print("\n------------------------\nMenu", "blue")
    colored_print("1 - Скриптинг\n2 - Создать главного персонажа\n4 - Разработчик\n\n0 - Настройки\n","blue")
    num = input("Ввод: ")
    if num == "1":
        print("Скриптинг")
    elif num == "2":
        print("Создать главного персонажа")
    elif num == "4":
        print("\nПривет, я IAmRadium. Я менеджер и создатель команды HILStory\nВ тг https://t.me/Radmir394\nУ нашей команды так же сть канала тг и вк https://t.me/HILStory_LP\nЯ не профессиональный программист, а любитель пописать что-то. Вы можете следить за разработкой в https://github.com/Radium394/LightHollow\nЯ не буду против если вы поможете с этим всем. Пишите мне в тг для связи")
        print("\nНажмите любую клавишу для продолжения...\n")
        keyboard.read_key()
    elif num == "0":
        settings()
    else:
        print(" - Не верный ответ. Попробуйте снова. Введите простую цифру")

