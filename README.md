# Game-Fighter-Monster
Задача проекта: Разработать простую игру, 
где игрок может использовать различные типы оружия
для борьбы с монстрами. Программа должна быть 
спроектирована таким образом, чтобы легко можно
было добавлять новые типы оружия, 
не изменяя существующий код бойцов или механизм боя.

## Исходные данные:
- Есть класс `Fighter`, представляющий бойца.

- Есть класс `Monster`, представляющий монстра.

- Игрок управляет бойцом и может выбирать для 
него одно из вооружений для боя.

## Особенности игры:
Создан абстрактный класс для оружия

Создан абстрактный класс `Weapon`, 
который содержит абстрактный метод `attack()`.

Реализованны конкретные типы оружия

- Созданы несколько классов, унаследованных 
от `Weapon`(`Sword` и `Bow`). 
Каждый из этих классов
реализует метод `attack()` своим уникальным способом.
- Модифицирован класс `Fighter`
Класс `Fighter`добавлен в поле, которое 
хранит объект класса `Weapon`.

- Добавлен метод `changeWeapon()`,
который позволяет изменить оружие бойца.

### Реализация боя:

- Реализован простой механизм для демонстрации боя
между бойцом и монстром, исходя из выбранного оружия.

- новые типы оружия можно легко добавлять, 
не изменяя существующие классы бойцов и механизм боя.

**[Программа выводит результат боя в консоль.]()**

### _Пример результата:_

Боец выбирает меч.

Боец наносит удар мечом.

Монстр побежден!

Боец выбирает лук.

Боец наносит удар из лука.

Монстр побежден!