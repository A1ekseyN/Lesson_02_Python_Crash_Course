import datetime
import time
start_time = time.time()


print("Hello")
print("1_000_000")

massage = "Hello. I'm PC."
print(massage)

massage = "Second massage"
print(massage)

### Методы ###
#.title, upper, lowee
# Все символы в начале слова пишутся с заглавной title()
name = "ada lovence"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovence"
full_name = f"{first_name} {last_name}"
massage = f"\tHello, {full_name.title()}, have a good day."
print(massage)
print(f"{first_name.title()} {last_name.title()}, it's a Python lesson")

# ============================================
# Числа
# ============================================
print(((2 + 2 + 3) * 5) * 2)
print(0.1 * 2)
print((0.1 * 3))
print(14_000_000 * 2)

x, y, z = 5, 0, 0
print(x + z)

# ==============================================
# Списки
# ==============================================
list = [1, 2, 3, 4, 5]
bicycle = ["connandale", "cube", "KTM", "trek", "specialized"]
print(bicycle[2])
print(bicycle[3].title())
print(bicycle[-3].title())

massage_bike = f"I bought {bicycle[1].title()} bike in the past year. Egor bought {bicycle[4].title()}."
print(massage_bike)
bicycle[0] = "honda"
print(f"But now, I'm use {bicycle[0].title()} bike.")

bicycle.append("Vesna")
print(f"Сейчас в списке 'bicycle' вот такие велосипеды: {bicycle[1].title()}, {bicycle[0].title()}, {bicycle[3].title()}, {bicycle[4].title()}, {bicycle[5].title()}.")

motocycle = []
motocycle.append("KTM")
motocycle.append("Honda")
motocycle.append("Suzuki")
print(motocycle)

motocycle.insert(0, "Ducati")
motocycle.insert(0, "BMW")
print(motocycle)

del motocycle[0]
print(motocycle)
del motocycle[1]
print(motocycle)

popped_motocycle = motocycle.pop()
print(motocycle)
print(popped_motocycle)

last_owned_motocycle = motocycle.pop(1)
print(f"My last motocycle is {last_owned_motocycle}.")
motocycle.append("Yamaha")
motocycle_expensive = "Ducati"
motocycle.remove(motocycle_expensive)
print(f"Delete {motocycle_expensive} from list, because bike too expensive.")
print(f"Now in list we have: {motocycle}")

names_celebration = ["Anna", "Bridget", "Arnold"]
print(f"\nDead, {names_celebration[0]}, {names_celebration[1]}, {names_celebration[2]}. I invite you to my birthday. Which will take place on the 26th.")
popped_names_celebration = names_celebration.pop()
print(f"Unfortunately mr. {popped_names_celebration}, he will not be able to attend the event.")
names_celebration.append("Suzzy")
print(f"Instead, we invited the beautiful Mrs. {names_celebration[-1]}.")
print(f"Dear {names_celebration[0]}, {names_celebration[1]}, {names_celebration[2]}, I wish you a good holiday.")


###########################################
# Сортировка

# cars.sort - Постоянная сортировка списка. Обратно вернуть нельзя
# sorted(cars) - Временная сортировка

cars = ["bmw", "subaru", "audi", "vw", "toyota", "ford"]
cars.sort()
print(f"\n{cars}")
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
# reverse - просто переворячивает список, и ничего не сортирует
print(len(cars))

country = ["ukraine", "russia", "zimbabve", "germany", "brazil"]
print(country)
print(sorted(country))
print(country)
print(sorted(country))
print(country[-3].title())


################################
# Срезы - Slice
################################

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
x1 = a[slice(0, None, 7)]
x2 = a[slice(1, None, 7)]
x3 = a[slice(2, None, 7)]
x4 = a[slice(3, None, 7)]
x5 = a[slice(4, None, 7)]
x6 = a[slice(5, None, 7)]
x7 = a[slice(6, None, 7)]

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)


###################################################
# Циклы
###################################################

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()} it's a good trick.")
    print(f"I can't wait to see your next trick, dear {magician.title()}.\n")
print(f"Thanks every one. It's a great magic show.\n")

pizzas = ["mario", "carbonara", "paperonni", "four chesse", "four seasons"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!\n")

##################################################
# Range
##################################################
for value in range (1, 6):
    print(value)

# Список (list), что-то не могу разобраться зачем там нужнен символ *. И без него не работает. В книге пример, так, там все ок.
numbers = [*(range(10, 31, 2))]
print(numbers)

# Список квадратов целых чисел от 1 до 10.
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

# Второй вариант, немного более короткий. Без дополнительный переменной.
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)


# Простая статистика с числовыми списками
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

# Генераторы списков
squares = [value**2 for value in range (1, 11)]
print(squares)

# Упражнение
digits = [*range(1, 21)]
print(digits)
print(sum(digits))

# Цикл for для создания range 1 - 20.
for number in range (1, 11):
    print(number)

##################################################
# TimeDelta - Суммирование времени
##################################################

#from datetime import timedelta
#a = timedelta(hours=2, minutes=5, seconds=17)
#b = timedelta(hours=2, minutes=5, seconds=17)
#print(a)
#print(b)
#c = a + b
#print(c)

#################################
# Slices
#################################

players = ["alina", "martina", "alice", "jacob", "bob"]
print(players[0:3])
print(players[1:4])
print(players[:5])

print("\nHere are the first players in my team:")
for player in players[:3]:
    print(player.title())


my_foods = ["pizza", "french frei", "soup", "ice cream", "coffe"]
friend_foods = my_foods[:]
# При использовании конструкции friend_foods = my_foods[:] происходит копирование списка, и его можно дополнительно изменять, как два разных списка.
# При использовании конструкции friend_foods = my_foods - будет просто копия списка.

my_foods.append("borch")
friend_foods.append("tea")

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

print(f"The first three items in the list are: {my_foods[:3]}.")
print(f"Three items from the middle of the list are: {my_foods[1:-2]}.")
print(f"The last three items in the list are: {my_foods[-3:]}.\n")

friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append("tomato")
friend_pizzas.append("el crudo")

print(pizzas)
print(friend_pizzas)

print("\nMy favorite pizzas:")
for pizz in pizzas:
    print(pizz.title())

print("\nMy friend favorite pizzas:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())


#######################################################
# Кортежи - Tuples
# Кортеж - это токой же список, как и list, то его нельзя редактировать
# Изменить кортеж можно присвоив ему новое значение
#######################################################
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

my_t = (3,)
print(my_t)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (300, 50)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)

print("\nFirst menu variation:")
dishes = ("salat", "soup", "ice cream", "pizza", "coffe")
for dish in dishes:
    print(dish.title())

print("\nSecond menu variation:")
dishes = ("salat", "soup", "ice cream", "buritoo", "tee")
for dish in dishes:
    print(dish.title())


money = 10
while money > 0: # Запускаем цикл
    print("We have %s dollars" % money)
    money -= 1
print("No more money. Time to work.")


########################################
# if
########################################

# Скрипт, который пишет названиея бренда большими, все остальные, просто с заглавной.
cars = ["bmw", "vw", "subaru", "toyota"]

# car == "bmw":
# Символ == (равно ли значение). Проверки используется символ ==.
# Если используется один знак "=", то переменной присваивается значение. А символн "==", проверка равно ли.
# Проверка производится с учетом регистра. bmw и BMW - не равны.
# if работает по принципе True / False. Если значение верно, тогда True, в других условиях False.

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# !=
# Проверка не равества через символ !=. Символ ! применяется для отрицания.
# В данном примере прошла проверка на переменную anchovises. Ее не обнаружено, и пишет сообщение, что такой переменной не найдено.
# При сравнении двух переменных, если они разные, тогда возвращается True. Если переменные одинаковые - False. И не выполняет код после if.
requested_topping = "mushrooms"
if requested_topping != "anchovis":
    print("\nHold the anchovises.")

# Сравнение чисел

# age = 18
# age == 18
# age > 18
# age =< 18

answer = 17
if answer != 41:
    print("Ответ не верный.")
else:
    print("Ответ верный.")

# and - При использовании if можно использовать конструкцию and. Пример:
# if age_01 == 18 and age_02 == 18:
age_01 = 21
age_02 = 17
if age_01 > 18 and age_02 > 18:
    print("\nЧисла больше 18.")
else:
    print("\nЧисла меньше 18.")


# or -. Конструкция or проверяет или истинно хотя бы одно условие. Если истинно одно или более условий, тогда - True. Иначе - False.
age_03 = 21
age_04 = 17
if age_03 > 16 or age_04 > 19:
    print("Хотя бы одно число из двух более 18.")
else:
    print("Числа меньше 18.")

### in - Проверка или список содержит определенное значение.
requested_topping = ["mushrooms", "onions", "cheese"]
if "mushrooms" in requested_topping:
    print("\nMushrooms request in request toppin - True")

# "paperoni" in request_topping
# False

### not - Проверка отсутствия значения в списке.
# Просходит проверка пользователя, или он состоит в блок листе.
banned_users = ["anna", "marie", "joe"]
user = "marie"
if user not in banned_users:
    print(f"\n{user.title()} can white a post at forum. ")
else:
    print(f"\n{user.title()} can't post massage, because user in block list.")


# True / False - Логические выражения.
game_active = True
can_edit = False

car = "subaru"
print("\nIs car == 'subaru'? I predict - True")
print(car == "subaru")

car = "audi"
print("Is car == 'bmw'? I predict - False.")
print(car == "bmw")

###################################
# Упражнения
###################################

stroke_list = ["bmw"]
for stroke in stroke_list:
    if stroke == "bmw":
        print(stroke_list)

car_details = ["motor", "gearbox", "wheels"]
detail = "window"
if detail not in car_details:
    print(f"\nДетали {detail.title()} нет на складе.")

if detail in car_details:
    print(f"Деталь - {detail.title()} есть на складе. И можно ее получить.")
else:
    print(f"Детали - {detail.title()}, снова нет на скаладе. Обратитесь, с понедельника.")

numbers = 18
if numbers >= 19:
    print(f"\nЧисло больше или равно 18")
else:
    print(f"\nЧисло меньше {numbers - 1}")


############################################
# if
############################################

# if
age = 19
if age >= 18:
    print("\nYou can vote.")
    print("Are you registred for vote?")

# if / else
age = 17
if age >= 18:
    print("\nYou can vote.")
    print("Are you registred for vote?")
else:
    print("\nSorry, but Johny, you too young for vote.")

# if / else / elif
# elif - Проверка 2х и более комбинаций. Код проверяется до тех пор пока не будет истинный результат.
# elif - Дополнительная проверка, если нужно добавить больше 2х условий для выполнения. elif - это аналог еще одного if.
# elif - можно использовать несколько конктрукци с elif
# else - Если условия if и elif не выполняются, тогда выполняется - else.
# else - Не обязательно использовать. Можно использовать как if, так и if / elif

age = 65
if age < 4:
    print("\nYour admission cost is $0.")
elif age < 18:
    print("\nYour admission cost is $25.")
elif age > 64:
    print("\nYour admission cost is $14.")
else:
    print("\n\nYour admission cost is $50.")

# Так же можно использовать более компактную кострукцию:
age = 65
price = []
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age > 64:
    price = 15
#else:
#    price = 50
print(f"Second price for you - {price}$.")

# if - Если нужно проверить все условия, тогда лучше использовать только if, без elif и esle.
requested_topping = ["mushrooms", "cheese", "pepperoni"]
if "mushrooms" in requested_topping:
    print("\nAdditing mushrooms")
if "cheese" in requested_topping:
    print("Additing cheese")
if "pepperoni" in requested_topping:
    print("Additing pepperoni")
print("Finishing your pizza.")

##############################
# Упражнение

alien_color = ["green", "yellow", "red"]
points = []
if "green" in alien_color:
    print(f"\nYou have earned 5 points.")

if "blue" in alien_color:
    print(f"\nYou have earned points.")


if "blue" in alien_color:
    print(f"\nYou have earned 5 points.")
else:
    print(f"\nYou have earned 10 points.")


if "yellow" and "green" in alien_color:
    print(f"\nYou have earned 5 points.")
else:
    print(f"\nYou have earned 10 points.")


if "blue" in alien_color:
    print(f"\nYou have earned 5 points score.")
elif "purple" in alien_color:
    print(f"\nYou have earned 10 points score.")
else:
    print(f"\nYou have earned 15 points score.")


age = 65
if age <= 2:
    print("\nЧеловек - младенец.")
elif age <= 4:
    print("\nЧеловек - малыш.")
elif age <= 12:
    print("\nЧеловек - ребенок.")
elif age <= 19:
    print("\nЧеловек - подросток.")
elif age <= 64:
    print("\nЧеловек - взрослый.")
else:
    print("\nЧеловек - пожилой.")


favotire_fruits = ["apple", "citrus", "mango"]
if "apple" in favotire_fruits:
    print("\nApple is my favorite fruit.")
if "citrus" in favotire_fruits:
    print("Citrus is my favorite fruit.")
if "mango" in favotire_fruits:
    print("Mango is my favorite fruit.")
if "Peanch"in favotire_fruits:
    print("Peanch is my favorite fruit.")
print("\n")

###################################
# Множественные списки
###################################
# Множественные списки в цикле for списка, можно делать выборку, и использовать команды if / else / elif.
# В примере идет выборка или в списке есть необходимые ингридиенты. И идет вывод информации. Есть такой топиг, или его нет.

available_toppings = ["mushrooms", "olives", "green paper", "pepperoni", "pineaple", "extra cheese"]
requested_toppings = ["mushrooms", "french freis", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding - {requested_topping}")
    else:
        print(f"Sorry, but we don't have - {requested_topping}")
print("Finished making your pizza.")


#######################################
# Упражнения
#######################################

forum_users = ["arnold", "jessy", "bob", "suzzy"]
login_users = ["admin", "arnold", "jessy", "bob", "suzzy"]
admin_user = ["admin"]

for user in admin_user:
    if user in login_users:
        print(f"\nHello, {user.title()}, thx for logining again. Do You wan't to see statistics?")
    else:
        print(f"Hello, {user.title()}, thx for logining again.")

for user in forum_users:
    if user in login_users:
        print(f"Hello, {user.title()}, thx for logining again.")


for user in admin_user:
    if user in login_users:
        print(f"\nHello, {user.title()}, thx for logining again. Do You wan't to see statistics?")
    else:
        print(f"Hello, {user.title()}, thx for logining again.")


# Очистка списка. Затем выводим сообщение, что нужно зарегестрировать новых пользователей
# Проверка пустой ли список
hello_admin = ["lusy", "jessy"]
if len(hello_admin) > 0:
    hello_admin.clear()

if len(hello_admin) == 0:
    print("\nWe need to register some users.")
print("\n")


# Проверка имени пользователя с учетом регистра. Что бы пользователи использовали уникальные имена.
corrent_users = ["Arnold", "jenny", "Jessy", "carolina", "angelica"]
corrent_users_small_registr = [x.lower() for x in corrent_users] # Копия списка в нижнем регистре.
new_users = ["arnold", "jenny", "syzzy", "vladislav", "bond"]

for user in corrent_users_small_registr:
    if user in new_users:
        print(f"Name {user} already used. Try a different name.")
    else:
        print(f"Registration user - {user} completed successfully.")


##########################################
# Числительные окончания: 1-й, 2-й, 3-й. 1st, 2nd, 3rd
##########################################

numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for number_list in numbers_list:
    if number_list == "1":
        print(f"{number_list}st")
    elif number_list == "2":
        print(f"{number_list}nd")
    elif number_list == "3":
        print(f"{number_list}rd")
    else:
        print(f"{number_list}th")
print("\n")

###########################################
# Словари
###########################################
# В словаре может находится несколько значений, которые потом можно вызывать.
# Пара ключ значение в списке, раздеются запятыми. Может быть любое кол-во ключей.
# Пустые словари используют для того, что бы пользователь мог вводить данные. Либо, для генерируемых значений.

# alien.py

alien_0 = {"color": "green"}
print(alien_0["color"].title())

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

print(alien_0)

# В словарь добавляются новые значения. В данном примере - это координаты.
# Значения сохраняются в словаре по порядку.
alien_0["x_position"] = 0
alien_0["y_position"] = 25
# После добавления значений, словарь содержит уже 4 значения: цвет, количество очков и координаты цели.
print(alien_0)

# Можно создавать пустые словари
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

# Изменения значений в словаре.
# Важно. Нужно помнить про использование " " и ' '. А то, могу т быть ошибки, из-за не правильного расставления кавечек.
# В примере указано, что цвет - "green".
alien_0 = {"color": "green"}
print(f"Alien color is {alien_0['color']}.")

alien_0["color"] = "yellow"
print(f"Now, alien color is {alien_0['color']}.")

# Параметр speed влияет на скорость.
alien_0 = {"x_position": 0, "y_position": 25, "speed": "slow"}
print(f"Original position: {alien_0['x_position']}")

# Пришелец перемещается вправо.
# Вычисляем велечину перемещения на основании текущей скорости.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
elif alien_0["speed"] == "fast":
    x_increment = 3
else:
    x_increment = 4

# Происходит смещение корабля по позиции. Новая позиция равно сумме старой позиции и новой.
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']} ")


################################################
# Удаление пар ключей в словаре. Выполняется командой del.
# Пара-ключ удаляется безвозвратно из словаря.
################################################

alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)


# Словарь с однотипными объектами.
# Словарь можно разбить по ключам - к примеру по именам.
# В конце рекомендуется поставить "," (запятую), что бы было проще добавить переменные в словарь.

favorite_languages = {
    "jen": "python",
    "rodion": "javascript",
    "roma": "c++",
    "artem": "javas",
}
# Так же можно присвоить списку определенное значение.
language_artem = favorite_languages["artem"].title()
print(f"\nArtem favorite language is {language_artem}.")


#####################################
# get()
# get() - Используется, при условии, что в [] может не быть значения. И тогда программа выдаст сообщение, что необходимых данных нет.
# В данном примере используется: "No points value assigned."
# При использовании get(), и ест не указан специальный аргумент, то, вернется None.
#####################################

alien_0 = {"color": "green", "speed": "slow"}
point_value = alien_0.get("points", "No points value assigned.")
point_value_1 = alien_0.get("health")
print(point_value)
print(f"В этом примере сделан запрос на не существующий аргумент. И возвращается: \n{point_value_1}.")

# Упражнения

women = {"first_name": "Anna",
       "last_name": "de Amarr",
       "age": "21",
       "city": "amarr"
       }
print(f"\nHello, my name is {women['first_name'].title()} {women['last_name'].title()}, I am {women['age']} years old. \nAnd I live in {women['city'].title()} city, in Amarria.")

favorite_numbers = {"aleksey": 96,
                    "allehandro": 16,
                    "leha": 25,
                    "murzik": 56,
                    "roma": 69,
                    }
print(f"\nЛюбимые числа у людей такие: \nAleksey - {favorite_numbers['aleksey']} \nAllehandro - {favorite_numbers['allehandro']} \nLeha - {favorite_numbers['leha']} \nMurzik - {favorite_numbers['murzik']} \nRoma - {favorite_numbers['roma']}.")

user_0 = {"username": "allehandro",
          "first_name": "aleksey",
          "last_name": "niko",
          }

# Перебор всех пар-ключей.
# Для перебора можно создать переменную в которой будет хранится ключ и значение пары-ключа.
print("\n")
for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

#print("\n")

# Так же переменным можно создать короткие значения.
# В примере key заменено на k, Value заменено на v.

for k, v in user_0.items():
    print(f"\nKey {k}")
    print(f"Value {v}")

print("\n")

# В переменной name сохраняется имя, а в переменной languege сохраняется переменная языка программирования.
favorite_languages = {
    "jen": "python",
    "roma": "ruby",
    "rodion": "javascrtipt",
    "artem": "java",
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite languege is {language.title()}.")

print("\n")

# Перебор всех ключей в словаре. Все ключи последовательно будут сохранены в переменной name.
# Метод .keys используется для того, что бы упростить чтение кода.

favorite_languages = {
    "jen": "python",
    "roma": "ruby",
    "rodion": "javascrtipt",
    "artem": "java",
    }

for name in favorite_languages.keys():
    print(name.title())

# Так же для перебора можно использовать более простую конструкцию:
for name in favorite_languages:
    print(f"В этом месте я использую более простую конструкцию для вывода имен: {name.title()}")


# Перебор по ключевым словам.

friends = ["rodion", "artem", "roma", "jen"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you live {language}")

# Можно выводить сообщение, если ключа нет в списке. Через конструкцию not in.
    if "erin" not in favorite_languages.keys():
        print(f"\nErin not in list wit favorite langueges.")

# Сортировка ключей методом sorted(). Можно применять и другие методы сортировки.
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}. Тут мы применили метод сортировки по алфавиту.")

# Перебор всех значений в словаре
# values - можно использовать для перебора всех значений в словаре, без вызова имен.
print("\nThe following languages have been mentioned.")
for langueges in favorite_languages.values():
    print(langueges.title())

# set() - Можно использовать, что бы в слове не было повторений.
print("\nProgramming languege without repeats:")
for languege in set(favorite_languages.values()):
    print(languege.title())


##################################################
# Упражнения
##################################################
rivers = {
    "ukraine": "dnerp",
    "egypt": "nile",
    "poland": "visla",
    "slovakia": "dunai",
    "kazakhstan": "ural"
}

print(f"\nThe river {rivers['egypt'].title()} flows throuth Egypt.")

print("\nПеречислены названия стран:")
for river in rivers:
    print(river.title())

print("\nПеречислены названия рек:")
for river in rivers.keys():
    print(river)

print("\n")


favorite_languages = {
    "jen": "python",
    "jen": "c#",
    "roma": "ruby",
    "rodion": "javascrtipt",
    "artem": "java",
    }

for name in (favorite_languages.keys()):
    if name in favorite_languages:
        print(f"{name.title()}, thanks for your vote.")


##############################################
# Вложения
##############################################
# aliens.py

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Создание пустого списка для хранения пришельцев.

aliens = []

# Создание 30 зеленых пришельцев
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)
print("...")

# Вывод количества созданных пришельцев.
print(f"Total number of aliens: {len(aliens)}.")

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
    elif alien["color"]  == "yellow":
        alien["color"] = "red"
        alien["points"] = 15
        alien["speed"] = "fast"

# Вывод первых 5 пришельцев
for alien in aliens[0:5]:
    print(alien)
print("...")


# Список в словаре
# pizza.py
# Сохранение информации о заказанной пицце
pizza = {
    "crust": "trick",
    "toppings": ["mushrooms", "extra cheese"],
}

# В этом примере берется информация из списка, и словаря, и объединяется в одно строку.
# Описание заказа
print(f"You order a pizza {pizza['crust']} - crust pizza "
    "with the following toppings:")
for topping in pizza["toppings"]:
    print("\t" + topping.title())
print("\n")

# favorite langueages.py
# У каждого имени может быть несколько любимых языков, и следующей конструкцией можно их вызвать.
# Так же видно, что каждое имя выводится с отступами
# Можно усовершенстовать конструкция так, что бы была проверка сколько любимых языков у каждого участника. Правда, вообще, хз, как это сделать.

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "heskel"],
}

for name, langueges in favorite_languages.items():
    print(f"{name.title()}'s favorite langueges are:")
    for language in langueges:
        print(f"\t{language.title()}")


# Словарь в словаре. Можно хранить словать в словаре. Но, так довольно усложняется код, и его восприятие.
# В примере ниже в словарь users вложен словарь с именами first, last, location.
#
# many_users.py
users = {
    "aenstein": {
        "first": "albert",
        "last": "enstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    }
 }

for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

###################################################
# Упражнения
###################################################
mans = {
    "arnold": {
        "first": "arnold",
        "last": "schwarzenegger",
        "location": "california",
    },
    "jonny": {
        "first": "jonny",
        "last": "walker",
        "location": "washington",
    },
    "orlando":{
        "first": "orlando",
        "last": "bloom",
        "location": "kentenberry",
    },
}

for username, user_info in mans.items():
    #print(f"Известная личность: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"
    print(f"{full_name.title()} проживает в городе {location.title()}.")


pets = {
    "arni":
        {"name_owner": "richard", "dog_breed": "doberman"},
    "alex":
        {"dog_name": "alex", "name_owner": "jerry", "dog_breed": "shepherd"},
    "maria":
        {"dog_name": "maria", "name_owner": "bussi", "dog_breed": "cocker"},
    }

for pet, value in pets.items():
    name_owner = "name_owner"
    print(f"Cобака породы {value['dog_breed']} по имени {pet.title()}, ее воспитал {value['name_owner'].title()}.")


favorite_places = {
    "Киев": "Алексей",
    "Буковель": ["Алексей", "Егор", "Женя",],
    "Драгобрат": ["Алексей", "Егор"],
}

for city, favorite_place in favorite_places.items():
    print(f"{city.title()}, является одним из любимых мест для {favorite_place}.")

favorite_numbers = {
    "aleksey": "96, 16, 25",
    "leha": "25, 44",
    "roma": "69, 64, 68",
}

for key, value in favorite_numbers.items():
    numbers = value
    print(f"У {key.title()} есть любимые числа, и они: {numbers}.")

cities = {
    "киев": {
        "country": "украине",
        "population": 3000000,
        "fact": "столица украины"
    },
    "трускавец": {
        "country": "украине",
        "population": 20,
        "fact": "люди пью воду"
    },
    "венеция": {
        "country": "италии",
        "population": 50000,
        "fact": "это город на воде"
    },
}

for city, value in cities.items():
    print(f"\nВ городе {city.title()}, который находится в {value['country'].title()}, проживает {value['population']:,.0f} людей. ")
    print(f"Так же интересный факт про {city.title()}, в городе {value['fact']}.")


###############################################
# Вввод данных и циклы while
# while
###############################################

# input() - Позволяет пользователю ввводить данные. И затем работать с ними.
# inpet() - Все данные интерпретирует в строку.
# Желательно оставлять пользователю подсказку, что бы он, точно, правильно вводил нужные данные. И программа дальше работала правильно.
### В этой части обучения, где вводимые данные через input() - помечены #, что бы программа не запрашивала миллион данных.

#massage = input("\nTell me some thing, and I will repeat back it to youd: ")
#print(massage)

#name = input("\nPlease enter your name: ")
#print(f"Hello, {name}. Have a good day, and have fun!")
# += С помощью этой конструкции можно дополнять переменную.

prompt = "\nHello, dear. Tell us who you are, and we can personalize the massage for you."
prompt += "\nWhat is your first name? "
#name = input(prompt)
#print(f"\nHello, {name.title()}. Fly save.")


# int() - Эта строка для преобразования строки в численное значение.
# int() - integer()

#age = input("\nСколько вам лет? ")
#age = int(age)
#print(f"Мне {age} года.")

if age >= 18:
    print(f"На данный момент вам {age} года, и вы можете голосовать на референдуме.")
else:
    print(f"На данный момент вам {age} года. Вы еще не достигли совершеннолетия.")


# Оператор вычисления остатка.
# % - Используется для того, что бы узнать остаток от числа.

#even_or_odd.py - Чётное или не чётное число.

#number = input("\nВведите число, и программа определит чётное число или не чётное: ")
#number = int(number)

if number % 2:
    print(f"Число {number} чётное.")
else:
    print(f"Число {number} не чётное.")


############################################
# Упражнения
############################################
# input - стоит #-нный, что бы не вводить миллион разных данных.

print("\nКакую машины вы бы хотели приобрести?")
#car_for_sale = input(f"Я хочу купить у вас: ")
#print(f"Сейчас проверю какие модели {car_for_sale} у нас есть в наличии.")


print("\nДобрый день. На скольких к вам забронировать стол?")
#reserve_table = input(f"Я хочу забронировать стол на человек: ")
#reserve_table = int(reserve_table)

#if reserve_table <= 8:
#    print(f"\nПроходите, у нас есть для вас свободный стол.")
#else:
#    print(f"\nК сожалению вам нужно будет подождат 15 минут. Скоро стол освободится.")


#######################################
# while - цикл
######################################
# for - цикл, который выполняется один раз
# while - цикл выполняется до тех пор, пока условие истинно

# counting.py

print("\nВ этом цикле добавляется +1.")
number_while = 1
while number_while <= 5:
    print(number_while)
    number_while += 1


# parrot.py
# Описан код как остановить выполнение цикла while с помощью строки 'quit'.
# != - проверка - равно ли?

# Пример программы, где нужно вписать нужный текст "quit", что бы программа прекратила выполнение.
#prompt = "\nTell me something, and I will repeat back it to you:"
#prompt += "\nEnter 'quit' to end the programm. "
#message = ""
#while message != 'quit':
#    message = input(prompt)
#    if message != "quit":
#        print(message)
#print("Завершение программы.")


# Флаги
# Прекращение работы программы по флагу. Принцип похожий как выше.
# На сколько понимаю, то флагами можно активировать различные части программного кода.

# Программа работает, но закоментированна.
#prompt = "\nTell me something, and I will repeat back it to you:"
#prompt += "\nEnter 'quit' to end the programm. "

#active = True
#while active:
#    message = input(prompt)

#    if message == "quit":
#        active = False
#    else:
#        print(message)
#print("Завершение программы.")


# break - команда прерывания цикла. Позволяет управлять тем, какая часть кода выполняется, а какая нет.
#cities.py

# Программа работает, но закоментированна.
#prompt = "\nPlease enter the name of city you have visited:"
#prompt += "\n(Enter 'quit', then you are finished). "

#while True:
#    city = input(prompt)

#    if city == 'quit':
#        break
#    else:
#        print(f"I'd love to go to {city.title()}.")
#print("Программа завершена.")


# continue - Команда продолжения цикла.
#counting.py

print("\nКоманда - continue.")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


# Предотвращение зацикливания. Закицливание цикла.
# В конце есть x += 1. Что увеличивает счётчик, и не дает зацилится циклу.
# x в виде 1, не изменяется, что и зацикливает цикл.

x = 1
while x < 5:
    print(x)
    x += 1

# Бесконечный цикл.
#x = 1
#while x < 5:
#    print(x)
###  x += 1

############################################
# Упражнения
############################################

#topping_pizza = ""

#print("\nКакой топинг, вы хотите добавить к пицце? ")
#print("Если вы закончили пормирование заказа, нажмите 'quit'.")

#while True:
#    order = input(topping_pizza)

#    if order == 'quit':
#        print("Закончено формирование заказа.")
#    else:
#        print("Какой еще топинг вы хотите добавить?")


#years_film_ask = "\nСколько вам лет? "

#active = True

#while active:
#    age_film = input(years_film_ask)
#    age_film = int(age_film)

#    if age_film <= 3:
#        print("Для вас билет бесплатный.")
#    elif age_film <= 12:
#        print("Для вас стоимость билета - 10 $.")
#    elif age_film > 12:
#        print("Для вас стоимость билета - 15 $.")




#prompt = "\nTell me something, and I will repeat back it to you:"
#prompt += "\nEnter 'quit' to end the programm. "

#active = True
#while active:
#    message = input(prompt)

#    if message == "quit":
#        active = False
#    else:
#        print(message)
#print("Завершение программы.")


###############################################
# while - работа со списками и словарями
###############################################
# Проверка пользователей. Нам нужно 3 списка: 2 для проверки и 1 пустой список, для хранения проверенных пользователей.

unconfirmed_users = ["alice", "brian", "candice"]
confirmed_users = []

# Проверям каждого пользователя, пока в списке остаются не проверенные пользователи.
# Проверенные пользователи перемещаются в списко confirmed_users = []

while unconfirmed_users:
    corrent_user = unconfirmed_users.pop()

    print(f"Verifite user: {corrent_user.title()}.")
    confirmed_users.append(corrent_user)

# Вывод всех проверенных пользователей.
print(f"\nThe following users gave been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Удаление всех вхождений из списка. Можно удалить конкретное значение из списка по названию.
# remove() - используется для удаления конкретного значения из списка или словаря

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

# Пример ниже показывает, что можно удалить конкретные значения по циклу while.
while "cat" in pets:
    pets.remove("cat")

print(pets)

#################################################################
# Заполнение анкеты. Вводится даные имени, и название горы, куда пользователь пойдет в путешествие.
#################################################################
# mountain_poll.py
responces = {}

# Установка флага продолжения опроса
#polling_active = True

#while polling_active:
    # Запрос имени пользователя и его ответа.
#    name = input(f"\nWhat is your name? ")
#    responce = input("Which mountain would you like to climb someday? ")

    # Ответ сохраняется в словаре.
#    responces[name] = responce

    # Проверка продолжения опроса.
#    repeat = input('Would you like to let another person respond? (yes / no) ')
#    if repeat == "no":
#        polling_active = False

# Опрос завершен, вывести результаты.
#print(f"\n --- Poll Results --- ")
#for name, responce in responces.items():
#    print(f"{name.title()} would like to climb {responce.title()}.")


# Упражнения про отпуск с вводом имени, а затем города.

#vacation_polling = {}

# Флаг для голосования
#polling_active = True

#while polling_active:
    # Запрос имени пользователя для голосования.
#    name = input("Как вас зовут? ")
#    vacation_poll = input("Куда вы хотите поехать в отпуск? ")

#    vacation_polling[name] = vacation_poll

#    repeat = input("Вы хотите продолжить проведения опроса? (да / нет). ")
#    if repeat == "нет":
#        polling_active = False

#print("\n --- Результаты голосования: --- ")
#for name, vacation_poll in vacation_polling.items():
#    print(f"{name.title()} поедет в отпуск в {vacation_poll.title()}.")


################################################
# Функции
################################################
# С помощью функций можно описывать много задач, а затем их последовательно выводить.
# def - описывает функции.
# Функцию можно вызывать несколько раз во время выполнения программы.

def greet_user():
    """Выводит простое приветские пользователя."""
    print("\nHello.")

# Вывод функции.
greet_user()


# Вызов функции приветствия с передаваеной информацией.
def greet_user(username):
    print(f"Hello {username.title()}!")

greet_user('jessie')

# Упражнение

def display_message(display_name):
    print(f"Hello {display_name.title()}!")

display_message('world')

# Еще одно упражнение с функцией def.
def favorite_book(book):
    print(f"My favorite book is {book.title()}.")

favorite_book("Alice in Wonderland")


# Позиционные аргументы. В функцию можно передавать несколько аргументов. К примеру название породы и имя питомца.
# pets.py

def describe_pet(animal_type, pet_name):
    """Выводит информацию про домашнее животное."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "jessica")

# Второй вызов функции.
describe_pet("dog", "arni")


#################################################
# Именованные аргументы. Можно добавить в функцию уточнение по поводу аргументов, что бы не было путанницы.
# При использовании именованных аргументов, их порядок не важен.
# Важно правильно написать аргементы. Что бы программа понимала куда и чему, что относится.
# pets.py

def describe_pet(animal_type, pet_name):
    """Вывод информации о животном"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type="hamstel", pet_name="jorry")

# Аргументы можно прописать "По умолчанию", что бы не прописывать их постоянно.
# То, есть один или все аргументы, можно описать, и они будут использоватся по умолчанию.

# Прописан аргумент animal_type=
# Важный момент. pet_name нужно ставить в начало фукции, ибо по другому не работает.
# Если задавать парамент pet_name еще раз, то значение по умолчанию будет игнорироваться.

def describe_pet (pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="Wallie")


# Эквивалентные вызовы функции.
# В примере ниже идет подставление разных вариаций работы функции.
print("==========================================")

# Собака
describe_pet("Willie")
describe_pet(pet_name="Bobbie")

# Хомяк по именни Garry.
describe_pet("garry", "hamster")
describe_pet(pet_name="larry", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="bobbie")


#####################################################
# Упражнения
####################################################

def make_shirt(size="m", text="i love Ukraine"):
    print(f"\nЯ хочу купить футболку с размером {size.title()} и надписью: {text.title()}.")

make_shirt()
make_shirt(size="s", text="stop war!!!")


def describe_city(city="kiev", country="ukraine"):
    print(f"\n{city.title()} is a capital of {country.title()}.")

describe_city()
describe_city(city="paris", country="france")


#########################################################
# Возвращаемое значение.
# return - может возвращать обработанное значение в точку, где начала выполняться функция.

# Возвращение простого значения.
# formatted_name.py

# В функции ниже происходит форматирование имени музыканта. Так, что бы оно потом выводилось в переменной.
def get_formatted_name(first_name, last_name):
    """Возвращает отформатированное имя"""
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name.title()

musician = get_formatted_name("jimmi", "hendrix")

print(musician)


# Не обязательные аргументы.
# Там же можно добавить аргумент, который, либо, будет использоваться, либо, не будет. middle_name=""
# В примере не обязательный элемент стоит в конце функции def. А во время ее выполнения, этот элемент можно подставить в любую точку.

def get_formatted_name(first_name, last_name, middle_name=""):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimmi", "hendrix")
print(musician)

musician = get_formatted_name("jimmi", "hendrix" , "lee")
print(f"\nВариант написания имения с 'middle_name': \n{musician}.")


# Возвращение словаря.
# Так же можно работать в функция со словарями.
# person.py

def build_person (first_name, last_name):
    """Возвращает информацию о человеке"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimmi', 'hendrix')
print(musician)

# Кроме того, функцию можно дополнять и другими данными. К примеру возраст.
# Почему-то данный код у меня не работает. Ругается на переменную age=. Такое ощущение, что часть этой переменной использовалась раньше.
# Проверил в новом окне, не понятно. Не работает.

def build_person (first_name, last_name):
    """Добавляем возраст к функции."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

#musician = build_person('jimmi', 'hedrix', age=34)
#print(musician)


##################################################
# Использование цикла while в функции.
##################################################

# greeter.py

def get_formatted_name(first_name, last_name):
    """Возврщает отформатированное имя"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# Бесконечный цикл.
# Постоянно спрашивает имя, и выводит его.

#while True:
    print("\nPlease, entrer your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


# Похожий цикл while, но с добавлением возможности остановить цикл.

def get_formatted_name(first_name, last_name):
    """"""
    full_name  = f"{first_name} {last_name}"
    return full_name.title()

#while True:
#    print(f"\nPlease enter your name: ")
#    print(f"(or enter 'q' for quit.)")

#    f_name = input("Enter first name: ")
#    if f_name == 'q':
#        break

#    l_name = input("Enter last name: ")
#    if l_name == 'q':
#        break

#    formatted_name = get_formatted_name(f_name, l_name)
#    print(f"\nHello, {formatted_name}.")


######################################
# Упражнения - 156 page
######################################

def city_country(city, country):
    print(f"{city.title()}, {country.title()}.")

city_country('santiago', "chile")
city_country('paris', 'france')
city_country('new york', "usa")

# Это упражнение не получается до конца сделать. Что-то я его не совсем понимаю.
def make_album(name_album, description_music):
    album = {'scorpions': name_album, 'how much is the fish': description_music}
    if number:
        album['number'] = album
    return album

musical_group = make_album(name_album="scorpions", description_music="how much is the fish")


#def make_album(name, description):
#    album = f"{name} {description}"
#    return album.title()

#while True:
#    print("\nДанный скрипт для названий и описания музыкальных групп:")
#    print("Или введите 'q' для завершения работы программы.")

#    m_name = input("\nВведите название группы: ")
#    if m_name == 'q':
#        break

#    descr = input("Введите описание для группы: ")
#    if descr == 'q':
#        break

#    group_description = make_album(m_name, descr)

#print(f"Вы ввели следующие названия музыкальных групп и их описание:\n{group_description}")


# Передача списка. Можно вызывать и использовать имена в функция, используя списки.
# В начале определяется список, затем он передается в функцию.

#greet_users.py

def greet_users(names):
    """Вывод приветствия для каждого пользователя."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usersnames = ["hanna", 'josep', 'bobbie']
greet_users(usersnames)


# Изменение списка в функции. Функция изменяет список, и закрепляет изменения.
# printing_models.py

# Список моделей, которые нужно напечатать.
unprinted_designs = ['phone model', 'car', 'moto']
completed_models = []

# Цикл последовательно передают каждую модель для печати, до конца списка.
# После печати каждая модель перемещается в список completed_modles.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}.")
    completed_models.append(current_design)

# Ввод всех готовых моделей.
print(f"\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model.title())

print("===========================")
# Тот же код, но с использованием функций - def

def print_models(unprinted_designs, completed_models):
    """
    Иммитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в список completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print(f"\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model.title())

unprinted_designs = ['raven', 'dominix', 'titan']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# Запрет изменения списка функции.
# Для того, что бы оставался исходный список, можно работать с его копией. Копию мы можем вызвать вот так:
# print_models(unprinted_designs[:], completed_models)
# То, есть мы используем [:] для создания копии списка.


# Упражнения

short_masseges = ['\nHello', 'Bongiorno', 'Привет']

def show_message():
    print(short_masseges[0])
    print(short_masseges[1])
    print(short_masseges[2])

show_message()

# Упражнение 2
# Не могу разобраться, почему не работает. В общем, хз.

#short_masseges = ['\nHello my dier', 'Bongiorno, gaspaccio', 'Привет, чё там, как оно?']

#def sent_message(message, sented_messages):
#    while message:
#        sented_message = short_messages.pop()
#        print(f"Отправлено сообщение: {sented_messages}.")
#        sented_messages.append(sented_message)

#short_messages = ['Hello my dier', 'Bongiorno, gaspaccio', 'Привет, чё там, как оно?']
#sented_messages = []

#sent_message(sented_messages)


# Передача произвольного набора аргументов
# Можно передавать не определенного кол-ва аргументов, с помощью *.
# *toppings - создает кортеж, который может упаковывать как одно значение, так и несколько.

# pizza.py

def make_pizza(*toppings):
    """Вывод списков заказанных топингов"""
    print(toppings)

make_pizza('papperoni')
make_pizza('mushrooms', 'cheese', 'tomato')


# Цикл, который выводит несколько значений из функций
def make_pizza(*toppings):
    """Вывод списков заказанных топингов"""
    print(f"\nВы заказали пиццу с:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('meat')
make_pizza('eggs', 'four_cheese', 'mushrooms')


# Позиционные аргументы с произвольными наборами функций
# Можно вызвать один аргумент в одном числе. К примеру размер пиццы. И втором аргументе вызвать большое кол-во значений. К примеру названия топингов

def make_pizza(size, *toppings):
    """Выводит описание пиццы"""
    print(f"\nMaking a {size} inch pizza with the following topings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'mazarella')
make_pizza(23, 'mushrooms', 'cheese', 'green paper')


# Использование произвольного набора именованных аргументов
# user_profile.py
# ** две звездочки создают пустой словарь с именем user_info, и упаковывают в него все пары-ключ.
# Затем к парам-ключам можно обращаться как к обычному словарю

def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'enstein',
                             location='princton',
                             field='physics')

print(user_profile)


# Упражнения

def sendwich(ingredients):
    print(f"\nМы сделаем сендвич со следующими игредиентами:")
    print(f'- {ingredients}')

sendwich('cheese')


def sendwich(*ingredients):
    print(f"\n Мы сделаем несколько сендвичей, с игридиентами:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

sendwich('hamon', 'cucumber', 'tomato')


def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('roxanna', 'harryson',
                             location='london',
                             field='mathematics')

print(user_profile)


# Нужно не забывать указывать **, а то по другому не работает.
# ** (две звездочки) создают пустой словарь.
def car_information(brand, model, **car_info):
    """Строит словарь с информацией об автомобилях"""
    car_info['brand_name'] = brand
    car_info['model_name'] = model
    return car_info

car_profile = car_information('subaru', 'outback',
                            color='green',
                            tow_package="No")

print(car_profile)


########################################################
# Хранение функций в модулях
########################################################
# С помощью модулей можно отделять функции от основного кода програмы. И разлелять их на файлы.

# Импортирование всего модуля.
# Можноо написать функции, сохранить ее в отдельный файл. И вызвать ее через import.
# Затем использовать обычный возов функции.
# Фактически происходит копирование функций из одного файла в другой файл.

# Пример:
# import pizza.py - импортирует функционал файла в другой файл
# pizza.make_pizzas() - вызывает функцию в файле. Так же можно в нее записывать и другие переменные.
# Для того, что бы вызвать модуль из импортированного файла, то нужно написать имя модуля pizza.
# а затем вызвать функцию .make_pizzas()


# Импортирование конкретных функций из модуля (файла).
# Так же можно импортировать разные функции разделяя их запятыми

# from имя_модуля import имя_функции
# from имя_модуля import имя_функции, другая_функция, третья_функция

# Пример импортирования функции из модуля
from pizza import make_pizza

print("\nИмпортированная функция из модуля - pizza.")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Назначение псевдонима для функции - псевдоним (alias)
# Это нужно если уже есть функции с таким именем, или что бы название было более понятным.

# Псевдоним (alias) - назначается во время импортирования функции
# Для пепейменовывания функции используется - as
# В примере ниже перейменовывется функция из make_pizza в mp

from pizza import make_pizza as mp

print("\nПерейменовывание функции из модуля - pizza.")
mp(18, 'red paper')
mp(23,"blue cheese", 'eggs', 'extra meat')


# Назначение псевдонима для модуля
# Так же можно назначить псевдоним и для всего модуля
# При импортировании указывае as и новое название модуля
# Используется, что бы название функций лучше читалось, и что бы не отвлекаться на название модулей

import pizza as p

print("\nПсевдоним для модуля")
p.make_pizza(16, 'mushrooms')
p.make_pizza(55, 'cucumber', 'potato', 'onion')


# Импортирование всех функций модуля
# * Импортирует все функции из модуля

# При копировании всех функций из модуля, можно использовать все функции по имени без использования точечной записи.
# Лучше не использовать этот метод при использовании написаных модулей сторонними разработчиками. Ибо, не понятно какие именно они функции используют.
# Если используются одинаковые имена в функциях, то происходит заменаю.

from pizza import *

print("Импортирование всех функций из модуля с помощью *.")

make_pizza(19, 'strawberry')
make_pizza(90, 'cheese', 'tomato', 'cucumber')


# Стилевое оформление функций
# Для правильного оформления нужно использовать _ (нижнее подчеркивание)
# Давать функциям имена, которые отображают то, что делает функция
# Имена должны быть короткими и понятными

# Можно давать комментарии функциям, что бы было понятно что делает функция
# При использовании = (знака равенства) между '=' и значениями пробле не ставится

# Команды import вставляются в начале файла с кодом. Исключение, когда в начале есть комментарии. После можно вставлять import.


#################################
# 9 - Классы
#################################

# Создание класса
# Dog() - Классы обозначаются с Большой буквы.

# dog.py

class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name.title()} rolled over!")


# Метод __init__
# Функция, которая является частью класса называется - метод.
# Вызывается с двумя __ по бокам. Если поставить _ (один), то работать не будет.
# Парамет self обязателен в определении метода.

# Создание экземпляра класса
# Класс это инструкция по созданию экземпляров

# Ниже мы используем класс Dog, и добавляем к ней информацию о имени и возрасте собаки.

my_dog = Dog('willie', 6)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog's {my_dog.name}, is {my_dog.age} years old.")


# Обращение к атрибутам

# my_dog.name - Этот атрибут показывает имя собаки
# my_dog.age - Вызывает атрибут, который указывает возраст собаки.


# Вызов метода
# Мы можем вызвать отдельные методы из класса.

my_dog.sit()
my_dog.roll_over()


# Создание нескольких экземпляров. Тут мы создадим еще одну собаку.

my_dog = Dog('willie', 6)
your_dog = Dog('bobbie', 17)

print(f"\nMy dog {my_dog.name.title()} living with me. And have {my_dog.age} years old.")
print(f"Your dog {your_dog.name.title()} there living?")
print(f"{your_dog.name.title()} is {your_dog.age} years old. Cool")

print("\nCan your do sit?")
your_dog.sit()

print(f"\nMy dog {my_dog.name.title()} at {my_dog.age} age can:")
my_dog.sit()
my_dog.roll_over()


# Упражнения

class Restaraunt():
    def __init__(self, restaraunt_name, cuisine_type):
        self.name = restaraunt_name
        self.type = cuisine_type

    def open_restaraunt(self):
        """Выводит сообщение о том или открыт ресторан"""
        print(f"На данный момент ресторан {self.name.title()} открыт.")

restaraunt = Restaraunt('родной край', 'работает')

print(f"\nДобро пожаловть в ресторан {restaraunt.name.title()}.")


# Вызов метода. Про то, что ресторан открыт.
restaraunt.open_restaraunt()

# Еще несколько других ресторанов
# Вроде не сильно сложно с этими методами, но сложно
restaraunt_02 = Restaraunt("mcDonald's", "работает")
restaraunt_03 = Restaraunt("генацвале", "не работает")

print(f"\nВ Жт есть ресторан {restaraunt_02.name.title()} и в данный момент он {restaraunt_02.type}.")
print(f"Так же ресторан {restaraunt_03.name.title()} в данный момент - {restaraunt_03.type}.")

restaraunt_02.open_restaraunt()

#!!!!
# self. - Очень важно подставлять self. там где это нужно, а не все подряд переменные. А то код может правильно не работать, и давать не верные результаты.
# self.

class User():
    def __init__(self, first_name, last_name, login):
        self.first = first_name
        self.last = last_name
        self.login = login

    def describe_user(self):
        """Выводит сообщение с описанием пользователя"""
        print(f"\nПользователь с логином {self.login}:"
              f"\n- {self.first.title()} {self.last.title()}")

    def greet_user(self):
        print(f"Hello, dear {self.first.title()} {self.last.title()}.")

    def hello(self):
        print(f"\nHello {self.first.title()}.")

user_allehandro = User('aleksey', 'niko', 'allehandro')
user_marcus = User('marcus', 'polo', 'marco')

print(f"\nHello, dear {user_allehandro.first.title()} {user_allehandro.last.title()}, your login in the game: {user_allehandro.login.title()}.")

user_allehandro.hello()
user_allehandro.describe_user()
user_allehandro.greet_user()

user_marcus.hello()
user_marcus.describe_user()
user_marcus.greet_user()


# Работа с классами и экземплярами
# Класс car

# car.py

class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year

    def get_discriptive_name(self):
        """Возвращает аккуратно отформатирование описание."""
#       """В книге есть ошибка. Нужно указывать model, а не manufacturer"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
your_new_car = Car('bmw', 'f30', 2015)
print(my_new_car.get_discriptive_name())
print(your_new_car.get_discriptive_name())


# Назначение атрибуту значения по умолчанию
# Скопировал clss Car(), что бы добавить дополнительные значения.

class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        """Возвращает аккуратно отформатирование описание."""
        #       """В книге есть ошибка. Нужно указывать model, а не manufacturer"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        """Выводит пробег машины в км."""
        print(f"Пробег у машины - {self.odometer_reading} км.")


my_new_car = Car('audi', 'a4', 2019)
your_new_car = Car('bmw', 'f30', 2015)
my_new_car.read_odometr()

my_new_car.odometer_reading = 96156 # В этом месте изменяю значение с 0, на новое значение в видел 96156.

print(my_new_car.get_discriptive_name())
print(your_new_car.get_discriptive_name())

print(f"\nВ данный момент мы смотрим {my_new_car.make.title()} {my_new_car.model.title()} {my_new_car.year} года выпуска. С пробегом {my_new_car.odometer_reading} км.")


# Изменение значений атрибутов с использованием методов.
# Можно написать метод, который будет брать значение, и подставлять его в функцию.

class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        """Возвращает аккуратно отформатирование описание."""
        #       """В книге есть ошибка. Нужно указывать model, а не manufacturer"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        """Выводит пробег машины в км."""
        print(f"Пробег у машины - {self.odometer_reading} км.")

    def odometer_update(self, mileage):
        """Устанавливает новое значение на одометре"""
        # Так же можно добавить защиту от скручивания пробега.
        # По сути это обычная проверка на > или < число, чем то, которое было изначально
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете скрутить пробег на машине.")

my_new_car = Car('audi', 'a4', 2019)
your_new_car = Car('bmw', 'f30', 2015)
print(my_new_car.get_discriptive_name())
print(your_new_car.get_discriptive_name())

my_new_car.odometer_update(98343)
my_new_car.read_odometr()


# Изменение абрибута с приращиванием.
# Используется, когда нужно к атрибуду добавить определенное значение,  а не постоянно задавать новые значения.

class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        """Возвращает аккуратно отформатирование описание."""
        #       """В книге есть ошибка. Нужно указывать model, а не manufacturer"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        """Выводит пробег машины в км."""
        print(f"Пробег у машины - {self.odometer_reading} км.")

    def odometer_update(self, mileage):
        """Устанавливает новое значение на одометре"""
        # Так же можно добавить защиту от скручивания пробега.
        # По сути это обычная проверка на > или < число, чем то, которое было изначально
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете скрутить пробег на машине.")

    def increment_odometr(self, miles):
        """Увеличивает значение одометра на определенное значение."""
        self.odometer_reading += miles

# Описание машины
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_discriptive_name())

# Задаеться пробег для машины
my_used_car.odometer_update(23500)
my_used_car.read_odometr()

# Добавляем до пробега +100 км
my_used_car.increment_odometr(100)
my_used_car.read_odometr()


# Упражнения (180 страница)
# Что-то, я не особо понимаю как выполнить эти упражнения. Видно их нужно делать сразу после того как прошел, а не на следующий день

#class Restaraunt():
#    def __init__(self, number, served):
#        """Ресторан. Определение кол-ва обслуженных клиентов"""
#        self.number = number
#        self.number_served = 0

#    def restaraunt(self):
#        print(f"Количество обслуженных клиентов ресторана сегодня - {self.number_served}")


# Наследование
# Используется если есть уже написанный класс. Только с другими аргументами

# Electric_car.py

class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        """Возвращает аккуратно отформатирование описание."""
        #       """В книге есть ошибка. Нужно указывать model, а не manufacturer"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        """Выводит пробег машины в км."""
        print(f"Пробег у машины - {self.odometer_reading} км.")

    def odometer_update(self, mileage):
        """Устанавливает новое значение на одометре"""
        # Так же можно добавить защиту от скручивания пробега.
        # По сути это обычная проверка на > или < число, чем то, которое было изначально
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете скрутить пробег на машине.")

    def increment_odometr(self, miles):
        """Увеличивает значение одометра на определенное значение."""
        self.odometer_reading += miles

# Наследование
# В скобках при создании класса указан класс с которого берется информация.
# Если класс-потомок в отдельном файле, то и код класс-родителя, тоже, нужно переносить в этот новый файл.
# super() - специальная функция, которая позволяет вызвать метод родительского класса.
# Класс-родитель называется супер-классом. А класс-потомок - подклассом.

# Бляха, как в этом всем разобраться, запомнить и потом использовать весь этот код.

class Electriccar(Car):
    """Представляет аспекты машины, которые специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)

my_tesla = Electriccar('tesla', 'model s', 2019)
print(my_tesla.get_discriptive_name())


# Определение атрибутов и методов класса-потомка
# Здесь мы добавляем атрибуты, которые отличают два класса друг от друга

class Electriccar(Car):
    """Представляет аспекты машины, которые специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        # Затем инициализирует атрибуты, специфические для электромобиля.
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Выводит информацию о эмкости аккумулятора."""
        print(f"This car has a {self.battery_size} kWh battery.")

my_tesla = Electriccar('tesla', 'model s', 2019)
my_tesla.describe_battery()


# Переопределение методов классов-родителя
# Переопределяет методы, если в классе-потомке нужно использовать подобный метод, но другой.

# В методе fill_gas_tank указывается, что у электромобилей нет бензобака.
# Другими словами этот медот для электрических машин не стоит использовать.

class Electriccar(Car):
    """Представляет аспекты машины, которые специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        # Затем инициализирует атрибуты, специфические для электромобиля.
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Выводит информацию о эмкости аккумулятора."""
        print(f"This car has a {self.battery_size} kWh battery.")

    def fill_gas_tank(self):
        """У электромобилей нет бензобака"""
        print(f"У электромобилей нет бензобака")

my_tesla = Electriccar('tesla', 'model s', 2019)
my_tesla.fill_gas_tank()


# Экземпляры как атрибуты.
# Для того, что бы код класса постоянно не увеличивался, часть класса можно записать отдельно, а затем вызвать его как атрибут в нужном классе.

class Car():
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_discriptive_name(self):
        """Возвращает аккуратно отформатирование описание."""
        #       """В книге есть ошибка. Нужно указывать model, а не manufacturer"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometr(self):
        """Выводит пробег машины в км."""
        print(f"Пробег у машины - {self.odometer_reading} км.")

    def odometer_update(self, mileage):
        """Устанавливает новое значение на одометре"""
        # Так же можно добавить защиту от скручивания пробега.
        # По сути это обычная проверка на > или < число, чем то, которое было изначально
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете скрутить пробег на машине.")

    def increment_odometr(self, miles):
        """Увеличивает значение одометра на определенное значение."""
        self.odometer_reading += miles


class Battery():
    """Простая модель аккумулятора"""
    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describer_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size} kWh battery.")

    def get_range(self):
        """Выводит примерный запас хода на заряде аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} mile on full charge.")


class Electriccar(Car):
    """Представляет аспекты машины, которые специфические для электромобилей."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        # Затем инициализирует атрибуты, специфические для электромобиля.
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = Electriccar('tesla', 'model s', 2021)
my_tesla.battery.describer_battery()
my_tesla.battery.get_range()

# Данный код постоянно усложняется, и вообще, становится сложно понимать что куда. Особенно, написать такое, кажется, уже не реальным.
# Вроде +- понимаю сам принцип как это работает, но вот написать, кажется не реальным.

# Упражнения не делал, ибо они какие-то очень сложные.



# Импортирование классов.
# Классы так же можно хранить в модулях, а затем их импортировать обратно в код.

# Импортирование одного класса
# Классы скопированы в файлы car.py и my_car.py

# Хранение нескольких классов в модуле.

# Импортирование всего модуля

# Импортирование всех классов из модуля
# Иногда может оказаться что классы, которые хранятся в разных модулях зависят друг от драга.
# И нужно ипортировать необходимый класс в нужный модуль.

# Использование псевдонимов
# Если имена длинные и спложные, то для них можно использовать псевдонимы

# from electric_car import Electriccar as EC


# Стандартная библиотека Python
# random
# Это библиотеки, которые можно подключать к программе через import. В PyCharm это работает через установку файлов.

from random import randint
print(randint(1,6))


# Упражнения

# Что-то с упражениями у меня стало все сложно, и они нормально не работают

class Die():
    def __init__(self, sides=6):
        print(randint(1, sides))
        self.sides = sides

    def roll_die(self, times):
        self.times = times
        times = 10
        while times < 1:
            print(randint(1, times))
            times = times - 1
        return roll_die()

print(Die())
print(Die.roll_die)


# Лотерея - Упражнение
# Упрежнение с лотерейными билетами и подсчетом вариаций.

print("\n=============================")

# Подбираемое число для лотерейного билета
lottery_a = randint(1, 10)
lottery_b = randint(1, 10)
lottery_c = randint(1, 10)

# Загаданное число для лотерейного билета
my_lottery_a = randint(1, 10)
my_lottery_b = randint(1, 10)
my_lottery_c = randint(1, 10)

lottery = (lottery_a, lottery_b, lottery_c)
my_lottery = (my_lottery_a, lottery_b, lottery_c)
lottery_counter = 0

print(f'Выпало: {lottery}')
print(f'Мое число: {my_lottery}')

while lottery != my_lottery:
    lottery_counter += 1
    lottery = (randint(1, 10), randint(1, 10), randint(1, 10))
    print(f"\nМое число: {my_lottery}")
    print(f"Выпало: {lottery}")
    print(f'Число попыток: {lottery_counter:,.0f}.')


# Оформление классов
# Классы записываются с верхней буквы
# В именах классов не делаются пробелы
# Каждый класс должен иметь строку описания, в которой объясняется, что именно делает данный класс
# Описание класса производится с помощью """ """

# Имена экземпляров и модулей записываются в нижнем реестре, а слова разделяются нижними подчеркиваниями.


########################################################
# Файлы и исключения
########################################################

# Чтение всего файла.
# Открываем файл и читаем его содержимое

# Файл можно открыть с помощью функции open()
# Содержимое файла помещается в переменную file_object
# Конструкция with открывает и закрывает файл когда это нужно программе
# Конструкция .read читает содержимое файла

# При чтении файла методом .read, добавляется пустая строка в конец файла.
# Что бы не было пустой строки нужно использовать метод rstrip()
# print(contents.rstrip())

# file_reader.py
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print('\nЧисло pi составляет:')
print(contents.rstrip())


# Пути к файлам
# Если передать простую команду open(), то файл будет найден в каталоге, в котором выполняется программа.

open('pi_digits.txt')

# Так же Python может искать файлы по другим путям. Если нужный файл не находится в одной папке с программой.
# Python может искать файлы по относительному пути.

#with open('folder/pi_digits.txt') as file_object:


# Так же можно использовать абсолютные пути, если относительный путь для файла не работает.
# Так же путь можно записать в переменную

# file_path = '/home/ehmatthes/other_files/folder/pi_digits.txt'
# with open(file_path) as file_object


# Чтение по строкам
# Для последовательной обработки каждой строки нужно воспользоваться циклом for

filename = 'pi_digits.txt'

with open('pi_digits.txt') as file_object:
    for line in filename:
        print(line.rstrip())


# Создание списка строк по содержимому файла








# Page 200


# Повторить break & continue
# page 158 - С помощью этого метода можно реализовать AutoClocker для Project Discovery.

#print("\n--- %s seconds ---" % (time.time() - start_time))
