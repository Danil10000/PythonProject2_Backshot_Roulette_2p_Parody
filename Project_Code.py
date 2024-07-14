from random import randint


energy_max = randint(2, 6)
first_player_energy, second_player_energy = energy_max, energy_max
number_of_rounds = randint(2, 8)
while True:
    rounds = ''
    for i in range(number_of_rounds):
        round = randint(0, 1)
        rounds += str(round)
        if i != number_of_rounds - 1:
            rounds += ', '
    life_rounds = rounds.count('1')
    blank_rounds = rounds.count('0')
    if life_rounds != 0 and blank_rounds != 0:
        break
print(f'В дробовике {life_rounds} боевых и {blank_rounds} холостых дроби.')
if energy_max < 5:
    print(f'У каждого игрока максимально может быть {energy_max} жизни.')
else:
    print(f'У каждого игрока максимально может быть {energy_max} жизней.')
number_of_items = randint(2, 4)
first_player_items = ''
second_player_items = ''
for i in range(number_of_items):
    item = randint(0, 4)
    first_player_items += str(item)
    if i != number_of_items - 1:
        first_player_items += ', '
for i in range(number_of_items):
    item = randint(0, 4)
    second_player_items += str(item)
    if i != number_of_items - 1:
        second_player_items += ', '
#  0-лупа, 1-пила, 2-сигареты, 3-пиво, 4-наручники
first_player_items = str(first_player_items).replace('0', 'Лупа')
first_player_items = str(first_player_items).replace('1', 'Пила')
first_player_items = str(first_player_items).replace('2', 'Сигареты')
first_player_items = str(first_player_items).replace('3', 'Пиво')
first_player_items = str(first_player_items).replace('4', 'Наручники')
print(f'Предметы первого игрока: {first_player_items}.')
first_player_items += ', Дробовик'
second_player_items = str(second_player_items).replace('0', 'Лупа')
second_player_items = str(second_player_items).replace('1', 'Пила')
second_player_items = str(second_player_items).replace('2', 'Сигареты')
second_player_items = str(second_player_items).replace('3', 'Пиво')
second_player_items = str(second_player_items).replace('4', 'Наручники')
print(f'Предметы второго игрока: {second_player_items}.')
second_player_items += ', Дробовик'
who_is_shooting = True  # True - Первый игрок, False - Второй игрок
cluffs_on_first_player = False  # Надеты ли наручники на первого игрока True - да, False - нет
cluffs_on_second_player = False  # Надеты ли наручники на второго игрока True - да, False - нет
double_damage = False  # True - двойной урон после использования пилы, False - обычный одинарный урон
while True:
    if who_is_shooting:
        print('Ход первого игрока.')
        choice = input('Выберите и введите ниже предмет, который хотите использовать из ниже перечисленных:\n'
                       f'{first_player_items}.\n'
                       'Выбор вводить сюда: ')
        if choice == 'Лупа':
            if first_player_items.count('Лупа') > 0:
                current_round = (rounds.split(', '))[0]
                if current_round == '0':
                    print('Текущая дробь холостая!')
                else:
                    print('Текущая дробь боевая!')
                first_player_items = first_player_items.replace('Лупа, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Пила':
            if first_player_items.count('Пила') > 0:
                double_damage = True
                print('Теперь урон дробовика удвоен!')
                first_player_items = first_player_items.replace('Пила, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Сигареты':
            if first_player_items.count('Сигареты') > 0:
                if first_player_energy == energy_max:
                    print('Вы не можете использовать сигареты, так как у вас максимальное количество зарядов!\n'
                          'Выберите что-нибудь другое.')
                else:
                    first_player_energy += 1
                    print(f'Одна энергия востановленна! Теперь у вас {first_player_energy} энергии.')
                    first_player_items = first_player_items.replace('Сигареты, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Пиво':
            if first_player_items.count('Пиво') > 0:
                current_round = (rounds.split(', '))[0]
                if current_round == '0':
                    rounds = rounds.replace('0', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    print('Вы сбросили из магазина холостую дробь.')
                else:
                    rounds = rounds.replace('1', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    print('Вы сбросили из магазина боевую дробь.')
                first_player_items = first_player_items.replace('Пиво, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Наручники':
            if first_player_items.count('Наручники') > 0:
                cluffs_on_second_player = True
                print('Теперь на второго игрока надеты наручники и он пропускает следующий ход.')
                first_player_items = first_player_items.replace('Наручники, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Дробовик':
            shoot_choice = input('Введите ниже, в кого вы хотите выстрелить.\n'
                                 'Варианты: В себя, В противника.\n'
                                 'Выбор вводить сюда: ')
            if shoot_choice == 'В себя':
                if (rounds.split(', '))[0] == '0':
                    print('Вам повезло, дробь холостая. Вы можете сделать ещё один ход.')
                    if double_damage:
                        print('Но вы использовали пилу понапрасну! Двойной урон анулирован.')
                        double_damage = False
                    rounds = rounds.replace('0', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                else:
                    print('Вам не повезло, в дробовике была боевая дробь.')
                    rounds = rounds.replace('1', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    if double_damage:
                        first_player_energy -= 2
                        double_damage = False
                        if first_player_energy < 1:
                            print('Второй игрок победил! Спасибо за игру, и первому игроку за самоубийство.')
                            break
                        else:
                            print(f'У вас осталось {first_player_energy} энергии.')
                            if cluffs_on_second_player:
                                print('Но есть и хорошие новости! Вы ходите ещё раз, так как надели наручники на противника.')
                                cluffs_on_second_player = False
                            else:
                                print('Теперь ходит второй игрок.')
                                who_is_shooting = False
                    else:
                        first_player_energy -= 1
                        if first_player_energy < 1:
                            print('Второй игрок победил! Спасибо за игру, и первому игроку за самоубийство.')
                            break
                        else:
                            print(f'У вас осталось {first_player_energy} энергии.')
                            if cluffs_on_second_player:
                                print('Но есть и хорошие новости! Вы ходите ещё раз, так как надели наручники на противника.')
                                cluffs_on_second_player = False
                            else:
                                print('Теперь ходит второй игрок.')
                                who_is_shooting = False
            elif shoot_choice == 'В противника':
                if (rounds.split(', '))[0] == '0':
                    print('Вам не повезло, в дробовике была холостая дробь.')
                    rounds = rounds.replace('0', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    if double_damage:
                        print('Но вы также не смогли нанести двойной урон противнику, и теперь он анулируется.')
                        double_damage = False
                    if cluffs_on_second_player:
                        print('Вы ходите ещё раз, так как надели наручники на противника.')
                        cluffs_on_second_player = False
                    else:
                        print('Теперь ходит второй игрок.')
                        who_is_shooting = False
                else:
                    print('Вам повезло, в дробовике была боевая дробь.')
                    rounds = rounds.replace('1', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    if double_damage:
                        second_player_energy -= 2
                        double_damage = False
                        if second_player_energy < 1:
                            print('Первый игрок победил! Спасибо за игру.')
                            break
                        else:
                            print(f'У второго игрока осталось {second_player_energy} энергии.')
                            if cluffs_on_second_player:
                                print('Вы ходите ещё раз, так как надели наручники на противника.')
                                cluffs_on_second_player = False
                            else:
                                print('Теперь ходит второй игрок.')
                                who_is_shooting = False
                    else:
                        second_player_energy -= 1
                        if second_player_energy < 1:
                            print('Первый игрок победил! Спасибо за игру.')
                            break
                        else:
                            print(f'У второго игрока осталось {second_player_energy} энергии.')
                            if cluffs_on_second_player:
                                print('Вы ходите ещё раз, так как надели наручники на противника.')
                                cluffs_on_second_player = False
                            else:
                                print('Теперь ходит второй игрок.')
                                who_is_shooting = False
            else:
                print('Вы сделали неверный ввод, попробуйте ещё раз.')
        else:
            print('Такого выбора не существует, попробуйте ещё раз.')
    else:
        print('Ход второго игрока.')
        choice = input('Выберите и введите ниже предмет, который хотите использовать из ниже перечисленных:\n'
                       f'{second_player_items}.\n'
                       'Выбор вводить сюда: ')
        if choice == 'Лупа':
            if second_player_items.count('Лупа') > 0:
                current_round = (rounds.split(', '))[0]
                if current_round == '0':
                    print('Текущая дробь холостая!')
                else:
                    print('Текущая дробь боевая!')
                second_player_items = second_player_items.replace('Лупа, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Пила':
            if second_player_items.count('Пила') > 0:
                double_damage = True
                print('Теперь урон дробовика удвоен!')
                second_player_items = second_player_items.replace('Пила, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Сигареты':
            if second_player_items.count('Сигареты') > 0:
                if second_player_energy == energy_max:
                    print('Вы не можете использовать сигареты, так как у вас максимальное количество зарядов!\n'
                          'Выберите что-нибудь другое.')
                else:
                    second_player_energy += 1
                    print(f'Одна энергия востановленна! Теперь у вас {second_player_energy} энергии.')
                    second_player_items = second_player_items.replace('Сигареты, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Пиво':
            if second_player_items.count('Пиво') > 0:
                current_round = (rounds.split(', '))[0]
                if current_round == '0':
                    rounds = rounds.replace('0', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    print('Вы сбросили из магазина холостую дробь.')
                else:
                    rounds = rounds.replace('1', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    print('Вы сбросили из магазина боевую дробь.')
                second_player_items = second_player_items.replace('Пиво, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Наручники':
            if second_player_items.count('Наручники') > 0:
                cluffs_on_first_player = True
                print('Теперь на первого игрока надеты наручники и он пропускает следующий ход.')
                second_player_items = second_player_items.replace('Наручники, ', '', 1)
            else:
                print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
        elif choice == 'Дробовик':
            shoot_choice = input('Введите ниже, в кого вы хотите выстрелить.\n'
                                 'Варианты: В себя, В противника.\n'
                                 'Выбор вводить сюда: ')
            if shoot_choice == 'В себя':
                if (rounds.split(', '))[0] == '0':
                    print('Вам повезло, дробь холостая. Вы можете сделать ещё один ход.')
                    if double_damage:
                        print('Но вы использовали пилу понапрасну! Двойной урон анулирован.')
                        double_damage = False
                    rounds = rounds.replace('0', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                else:
                    print('Вам не повезло, в дробовике была боевая дробь.')
                    rounds = rounds.replace('1', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    if double_damage:
                        second_player_energy -= 2
                        double_damage = False
                        if second_player_energy < 1:
                            print('Первый игрок победил! Спасибо за игру, и второму игроку за самоубийство.')
                            break
                        else:
                            print(f'У вас осталось {second_player_energy} энергии.')
                            if cluffs_on_first_player:
                                print('Но есть и хорошие новости! Вы ходите ещё раз, так как надели наручники на противника.')
                                cluffs_on_first_player = False
                            else:
                                print('Теперь ходит первый игрок.')
                                who_is_shooting = True
                    else:
                        second_player_energy -= 1
                        if second_player_energy < 1:
                            print('Первый игрок победил! Спасибо за игру, и второму игроку за самоубийство.')
                            break
                        else:
                            print(f'У вас осталось {second_player_energy} энергии.')
                            if cluffs_on_first_player:
                                print('Но есть и хорошие новости! Вы ходите ещё раз, так как надели наручники на противника.')
                                cluffs_on_first_player = False
                            else:
                                print('Теперь ходит первый игрок.')
                                who_is_shooting = True
            elif shoot_choice == 'В противника':
                if (rounds.split(', '))[0] == '0':
                    print('Вам не повезло, в дробовике была холостая дробь.')
                    rounds = rounds.replace('0', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    if double_damage:
                        print('Но вы также не смогли нанести двойной урон противнику, и теперь он анулируется.')
                        double_damage = False
                    if cluffs_on_first_player:
                        print('Вы ходите ещё раз, так как надели наручники на противника.')
                        cluffs_on_first_player = False
                    else:
                        print('Теперь ходит второй игрок.')
                        who_is_shooting = True
                else:
                    print('Вам повезло, в дробовике была боевая дробь.')
                    rounds = rounds.replace('1', '', 1)
                    if rounds.count(', ') > 0:
                        rounds = rounds.replace(', ', '', 1)
                    if double_damage:
                        first_player_energy -= 2
                        double_damage = False
                        if first_player_energy < 1:
                            print('Первый игрок победил! Спасибо за игру.')
                            break
                        else:
                            print(f'У второго игрока осталось {first_player_energy} энергии.')
                            if cluffs_on_first_player:
                                print('Вы ходите ещё раз, так как надели наручники на противника.')
                                cluffs_on_first_player = False
                            else:
                                print('Теперь ходит второй игрок.')
                                who_is_shooting = True
                    else:
                        first_player_energy -= 1
                        if first_player_energy < 1:
                            print('Первый игрок победил! Спасибо за игру.')
                            break
                        else:
                            print(f'У второго игрока осталось {first_player_energy} энергии.')
                            if cluffs_on_first_player:
                                print('Вы ходите ещё раз, так как надели наручники на противника.')
                                cluffs_on_first_player = False
                            else:
                                print('Теперь ходит второй игрок.')
                                who_is_shooting = True
            else:
                print('Вы сделали неверный ввод, попробуйте ещё раз.')
        else:
            print('Такого выбора не существует, попробуйте ещё раз.')
