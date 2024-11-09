from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом."

    def get_name(self):
        return "меч"

class Bow(Weapon):
    def attack(self):
        return "стреляет из лука."

    def get_name(self):
        return "лук"

class Axe(Weapon):
    def attack(self):
        return "размахивает топором."

    def get_name(self):
        return "топор"

# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.get_name()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}")

# Класс для монстра
class Monster:
    def __init__(self, name):
        self.name = name
        self.is_defeated = False

    def defeat(self):
        self.is_defeated = True
        print(f"{self.name} побежден!")

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    if fighter.weapon:
        fighter.attack()
        monster.defeat()
    else:
        print(f"У {fighter.name} нет оружия для боя!")

# Создадим объекты и продемонстрируем бой
def main():
    # Создание бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Включение различных видов оружия
    sword = Sword()
    bow = Bow()
    axe = Axe()

    # Демонстрация боя с различными видами оружия
    fighter.change_weapon(sword)
    battle(fighter, monster)

    # Находим нового монстра для следующей битвы
    monster = Monster("Монстр")  # Новый монстр для следующего боя

    fighter.change_weapon(bow)
    battle(fighter, monster)

    # Находим другого нового монстра
    monster = Monster("Монстр")  # Новый монстр для следующего боя

    fighter.change_weapon(axe)
    battle(fighter, monster)

if __name__ == "__main__":
    main()