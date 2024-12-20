import random

# Игрок
player = {
    "inventory": [],
    "health": 100,
}

# Уровни
levels = {
    1: {
        "description": "Вы находитесь в первом уровне. Доктор Эггман захватил животных! Найдите его и победите.",
        "enemy": "Доктор Эггман",
        "item_to_defeat": "супер-меч",
    },
    2: {
        "description": "На втором уровне вы встречаете Ёжа Шэдоу! Вам нужно найти предмет, чтобы его победить.",
        "enemy": "Ёж Шэдоу",
        "item_to_defeat": "световой меч",
    },
    3: {
        "description": "Вы на третьем уровне. Здесь загадка: 'В каком году вышла первая игра про Соника?'",
        "riddle_answer": "1991",
    },
}

# Функция для отображения инвентаря
def show_inventory():
    if player["inventory"]:
        print("Ваш инвентарь:", ", ".join(player["inventory"]))
    else:
        print("Ваш инвентарь пуст.")

# Уровень 1
def level_one():
    print(levels[1]["description"])
    show_inventory()
    
    action = input("Что вы хотите сделать? (найти меч, атаковать Эггмана): ").strip().lower()
    if action == "найти меч":
        player["inventory"].append(levels[1]["item_to_defeat"])
        print("Вы нашли супер-меч.")
    elif action == "атаковать эггмана" and levels[1]["item_to_defeat"] in player["inventory"]:
        print("Вы победили Доктора Эггмана и спасли животных!")
        return True
    else:
        print("Неверное действие. Попробуйте снова.")
    return False

# Уровень 2
def level_two():
    print(levels[2]["description"])
    show_inventory()
    
    action = input("Что вы хотите сделать? (найти меч, атаковать Шэдоу): ").strip().lower()
    if action == "найти меч":
        player["inventory"].append(levels[2]["item_to_defeat"])
        print("Вы нашли световой меч.")
    elif action == "атаковать шэдоу" and levels[2]["item_to_defeat"] in player["inventory"]:
        print("Вы победили Ёжа Шэдоу!")
        return True
    else:
        print("Неверное действие. Попробуйте снова.")
    return False

# Уровень 3
def level_three():
    print(levels[3]["description"])
    show_inventory()
    
    answer = input("Введите ваш ответ на загадку: ").strip()
    if answer == levels[3]["riddle_answer"]:
        print("Вы разгадали загадку и выбрались из яйца смерти!")
        return True
    else:
        print("Неверный ответ. Попробуйте снова.")
    return False

# Основная игра
def main():
    print("Добро пожаловать в приключение Ёжа Соника!")
    
    # Уровень 1
    while not level_one():
        pass
    
    # Уровень 2
    while not level_two():
        pass
    
    # Уровень 3
    while not level_three():
        pass

    print("Поздравляем! Вы завершили игру.")

# Запуск игры
if __name__ == "__main__":
    main()