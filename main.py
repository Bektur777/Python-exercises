# 1.
# class Product:
#
#     def __init__(self, name, price, discount, expiration):
#         self.price = price
#         self.expiration = expiration
#         self.name = name
#         self.discount = discount
#
#     def get_name(self):
#         return f'Вид продукта {self.name}'
#
#     def get_price(self):
#         return f'Цена за продукт {self.name} = {self.price - self.discount}'
#
#     def get_expiration(self):
#         return f'Срок годность {self.expiration()}'
#
#     def get_discount(self):
#         return f'Скидка равна {self.discount}'
#
#
# class Meat (Product):
#
#     def __init__(self, price, expiration, name, discount, variety, count):
#         self.variety = variety
#         self.count = count
#         super().__init__(name, price, discount, expiration)
#
#     def get_report(self):
#         report = 'Name: {} Price: {} Discount: {} Expiration: {} Count: {}'
#         print(report.format(self.name, self.price, self.discount, self.expiration, self.count))
#
#     def get_portion(self):
#         if self.variety == 'замороженная':
#             return self.get_variety()
#         elif self.variety == 'жаренная':
#             return self.get_variety()
#         else:
#             print('Такого вида нет')
#
#     def get_count(self):
#         return f'Кол-во {self.name} {self.count}'
#
#     def get_variety(self):
#         return self.name, self.variety
#
#
# class Chicken (Meat):
#
#     def __init__(self, price, expiration, name, discount, variety, count, hot_food):
#         self.hot_food = hot_food
#         super().__init__(price, expiration, name, discount, variety, count)
#
#     def get_hot_food(self):
#         return self.name, self.hot_food
#
#
# obj1 = Product('Milk', 80, 15, '20.06.2022')
# print(obj1.get_price())
#
# obj2 = Meat(150, '20.06.2022', 'Cow', 20, 'замороженная', 100)
# obj2.get_report()
#
# obj3 = Chicken(150, '20.06.2022', 'Chicken', 20, 'замороженная', 100, 'Soup')
# print(*obj3.get_hot_food())
# print(*obj3.get_portion())


# -----------------------------------------------------------------------------------------------------------------------

#2.
# class Pass:
#
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age
#
#     def choice(self):
#         choose = input(f'Выберите путь {self._name} домой или в клуб\n').lower()
#         if choose == 'дом':
#             self._home_pass()
#         elif choose == 'клуб':
#             self.__club_pass()
#         else:
#             print('Выберите вариант из двух предложенных')
#
#     def __club_pass(self):
#         try:
#             if self.__age >= 18:
#                 print(f'Добро пожаловать в клуб {self._name}')
#             else:
#                 print('Доступ запрещен вам нет 18')
#         except:
#             raise ValueError('Было введено не число')
#
#     def _home_pass(self):
#         print(f'Добро пожаловать домой {self._name}')
#
#     def set_club(self, name, age):
#         self.__age = age
#         self._name = name
#
#     def get_club(self):
#         return self.__age, self._name
#
#
# obj = Pass("name", 18)
# obj.choice()
# print(obj.get_club())


#-----------------------------------------------------------------------------------------------------------------------

#3.
# class Strength:
#
#     def __init__(self, name, skill):
#         self.name = name
#         self.skill = skill
#
#     def attack(self):
#         return self.name, self.skill
#
#
# class Agility:
#
#     def __init__(self, name, skill):
#         self.name = name
#         self.skill = skill
#
#     def attack(self):
#         return self.name, self.skill
#
#
# class Intelicence:
#
#     def __init__(self, name, skill):
#         self.name = name
#         self.skill = skill
#
#     def attack(self):
#         return self.name, self.skill
#
#
# h1 = Strength('DragonKnight', 'Inferno')
# h2 = Agility('Phantom Assassin', 'STIFLING DAGGER')
# h3 = Intelicence('Lina', 'Light Strike Array')
#
# hero = [h1, h2, h3]
#
# for i in hero:
#     print(*i.attack())


#-----------------------------------------------------------------------------------------------------------------------
# 4.
# import random
#
#
# class Hero:
#
#     def __init__(self, name, skill, hp):
#         self.name = name
#         self.skill = skill
#         self.hp = hp
# 
#     def attack(self):
#         pass
#
#
# class Strength(Hero):
#
#     def __init__(self, name="DK", skill=25, hp=100):
#         self.name = name
#         self.skill = skill
#         self.hp = hp
#         super(Strength, self).__init__(name, skill, hp)
#
#     def attack(self):
#         return self.name, self.skill
#
#     def fight(self):
#         pass
#
#     def get_skill(self):
#         return self.skill
#
#     def get_name(self):
#         return self.name
#
#     def get_hp(self):
#         return self.hp
#
#
# class Agility(Strength):
#
#     def __init__(self, name='Lina', skill=25, hp=100):
#         self.name = name
#         self.skill = skill
#         self.hp = hp
#         super().__init__(name, skill, hp)
#
#     def attack(self):
#         self.hp -= self.skill
#
#     def fight(self):
#         a = Strength()
#         while self.hp >= 0:
#             hpRegen = random.randint(0, 1)
#             if hpRegen == 1:
#                 a.hp -= a.skill
#                 print(f'Ударил {a.get_name()}')
#                 if a.get_hp() < 0:
#                     print(f'Победа за {a.get_name()}')
#                     break
#             else:
#                 self.attack()
#                 print(f'Ударилa {self.name}')
#                 if self.hp <= 0:
#                     print(f'Победа за {self.name}')
#                     break
#
#
# obj = Agility()
# obj.fight()

