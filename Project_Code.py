import random


def gen_energy():
    energy_max = random.randint(2, 6)
    first_player_energy, second_player_energy = energy_max, energy_max
    return [f'У каждого игрока максимально может быть {energy_max} энергии.', first_player_energy,
            second_player_energy, energy_max]

def gen_rounds():
    num_of_rounds = random.randint(2, 8)
    while True:
        rounds = ''
        for i in range(num_of_rounds):
            rounds += str(random.randint(0, 1))
            if i != num_of_rounds - 1:
                rounds += ', '
        if rounds.count('1') != 0 and rounds.count('0') != 0:
            break
    return [f'В дробовике {rounds.count('1')} боевых и {rounds.count('0')} холостых дроби.', rounds]

def gen_items():
    number_of_items = random.randint(2, 4)
    first_player_items = ''
    second_player_items = ''
    for i in range(number_of_items):
        first_player_items += random.choice(['Лупа', 'Пила', 'Сигареты', 'Пиво', 'Наручники'])
        second_player_items += random.choice(['Лупа', 'Пила', 'Сигареты', 'Пиво', 'Наручники'])
        if i != number_of_items - 1:
            first_player_items += ', '
            second_player_items += ', '
    return [f'Предметы первого игрока: {first_player_items}.', f'Предметы второго игрока: {second_player_items}.',
            first_player_items + ', Дробовик', second_player_items + ', Дробовик']

def game():
    round_num = 1  # Номер раунда
    first_player_points = 0  # Очки первого игрока
    second_player_points = 0  # Очки второго игрока
    cuffs_on_first_player = False  # Надеты ли наручники на первого игрока True - да, False - нет
    cuffs_on_second_player = False  # Надеты ли наручники на второго игрока True - да, False - нет
    double_damage = False  # True - двойной урон после использования пилы, False - обычный одинарный урон
    for i in range(3):
        who_is_shooting = random.choice([True, False])  # True - Первый игрок, False - Второй игрок
        if round_num == 1:
            print('Начинаем первый раунд!')
        elif round_num == 2:
            print('Начинаем второй раунд! Текущий счёт игры: \n'
                  f'Первый игрок: {first_player_points}, Второй игрок: {second_player_points}.')
        else:
            print('Начинаем третий раунд! Текущий счёт игры: \n'
                  f'Первый игрок: {first_player_points}, Второй игрок: {second_player_points}.')
        gen_energy_val = gen_energy()
        print(gen_energy_val[0])
        gen_rounds_val = gen_rounds()
        print(gen_rounds_val[0])
        gen_items_val = gen_items()
        print(gen_items_val[0])
        print(gen_items_val[1])
        while True:
            if len(gen_items_val[2].split(', ')) == 1 and len(gen_items_val[3].split(', ')) == 1:
                gen_items_val = gen_items()
                print('У кого-то закончились предметы! Но ничего, вот вам новые:\n',
                      f'{gen_items_val[0]}\n', gen_items_val[1])
            if len(gen_rounds_val[1]) < 1:
                gen_rounds_val = gen_rounds()
                print('В дробовике закончились дроби! Сейчас перезарядим...\n'
                      f'{gen_rounds_val[0]}')
            if who_is_shooting:
                print('Ход первого игрока.')
                choice = input('Выберите и введите ниже предмет, который хотите использовать из ниже перечисленных:\n'
                               f'{gen_items_val[2]}.\n'
                               'Выбор вводить сюда: ')
                if choice == 'Лупа':
                    if gen_items_val[2].count('Лупа') > 0:
                        if (gen_rounds_val[1].split(', '))[0] == '0':
                            print('Текущая дробь холостая!')
                        else:
                            print('Текущая дробь боевая!')
                        gen_items_val[2] = gen_items_val[2].replace('Лупа, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Пила':
                    if gen_items_val[2].count('Пила') > 0:
                        double_damage = True
                        print('Теперь урон дробовика удвоен!')
                        gen_items_val[2] = gen_items_val[2].replace('Пила, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Сигареты':
                    if gen_items_val[2].count('Сигареты') > 0:
                        if gen_energy_val[1] == gen_energy_val[3]:
                            print('Вы не можете использовать сигареты, так как у вас максимальное количество зарядов!\n'
                                  'Выберите что-нибудь другое.')
                        else:
                            gen_energy_val[1] += 1
                            print(f'Одна энергия востановленна! Теперь у вас {gen_energy_val[1]} энергии.')
                            gen_items_val[2] = gen_items_val[2].replace('Сигареты, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Пиво':
                    if gen_items_val[2].count('Пиво') > 0:
                        current_round = (gen_rounds_val[1].split(', '))[0]
                        if current_round == '0':
                            gen_rounds_val[1] = gen_rounds_val[1].replace('0', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            print('Вы сбросили из магазина холостую дробь.')
                        else:
                            gen_rounds_val[1] = gen_rounds_val[1].replace('1', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            print('Вы сбросили из магазина боевую дробь.')
                        gen_items_val[2] = gen_items_val[2].replace('Пиво, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Наручники':
                    if gen_items_val[2].count('Наручники') > 0:
                        cuffs_on_second_player = True
                        print('Теперь на второго игрока надеты наручники и он пропускает следующий ход.')
                        gen_items_val[2] = gen_items_val[2].replace('Наручники, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Дробовик':
                    shoot_choice = input('Введите ниже, в кого вы хотите выстрелить.\n'
                                         'Варианты: В себя, В противника.\n'
                                         'Выбор вводить сюда: ')
                    if shoot_choice == 'В себя':
                        if (gen_rounds_val[1].split(', '))[0] == '0':
                            print('Вам повезло, дробь холостая. Вы можете сделать ещё один ход.')
                            if double_damage:
                                print('Но вы использовали пилу понапрасну! Двойной урон анулирован.')
                                double_damage = False
                            gen_rounds_val[1] = gen_rounds_val[1].replace('0', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                        else:
                            print('Вам не повезло, в дробовике была боевая дробь.')
                            gen_rounds_val[1] = gen_rounds_val[1].replace('1', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            if double_damage:
                                gen_energy_val[1] -= 2
                                double_damage = False
                                if gen_energy_val[1] < 1:
                                    print('Второй игрок победил!')
                                    second_player_points += 1
                                    round_num += 1
                                    break
                                else:
                                    print(f'У вас осталось {gen_energy_val[1]} энергии.')
                                    if cuffs_on_second_player:
                                        print(
                                            'Но есть и хорошие новости! Вы ходите ещё раз, так как надели наручники на противника.')
                                        cuffs_on_second_player = False
                                    else:
                                        who_is_shooting = False
                            else:
                                gen_energy_val[1] -= 1
                                if gen_energy_val[1] < 1:
                                    print('Второй игрок победил!')
                                    second_player_points += 1
                                    round_num += 1
                                    break
                                else:
                                    print(f'У вас осталось {gen_energy_val[1]} энергии.')
                                    if cuffs_on_second_player:
                                        print(
                                            'Но есть и хорошие новости! Вы ходите ещё раз, так как надели наручники на противника.')
                                        cuffs_on_second_player = False
                                    else:
                                        who_is_shooting = False
                    elif shoot_choice == 'В противника':
                        if (gen_rounds_val[1].split(', '))[0] == '0':
                            print('Вам не повезло, в дробовике была холостая дробь.')
                            gen_rounds_val[1] = gen_rounds_val[1].replace('0', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            if double_damage:
                                print('Но вы также не смогли нанести двойной урон противнику, и теперь он анулируется.')
                                double_damage = False
                            if cuffs_on_second_player:
                                print('Вы ходите ещё раз, так как надели наручники на противника.')
                                cuffs_on_second_player = False
                            else:
                                who_is_shooting = False
                        else:
                            print('Вам повезло, в дробовике была боевая дробь.')
                            gen_rounds_val[1] = gen_rounds_val[1].replace('1', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            if double_damage:
                                gen_energy_val[2] -= 2
                                double_damage = False
                                if gen_energy_val[2] < 1:
                                    print('Первый игрок победил!')
                                    first_player_points += 1
                                    round_num += 1
                                    break
                                else:
                                    print(f'У второго игрока осталось {gen_energy_val[2]} энергии.')
                                    if cuffs_on_second_player:
                                        print('Вы ходите ещё раз, так как надели наручники на противника.')
                                        cuffs_on_second_player = False
                                    else:
                                        who_is_shooting = False
                            else:
                                gen_energy_val[2] -= 1
                                if gen_energy_val[2] < 1:
                                    print('Первый игрок победил!')
                                    first_player_points += 1
                                    round_num += 1
                                    break
                                else:
                                    print(f'У второго игрока осталось {gen_energy_val[2]} энергии.')
                                    if cuffs_on_second_player:
                                        print('Вы ходите ещё раз, так как надели наручники на противника.')
                                        cuffs_on_second_player = False
                                    else:
                                        who_is_shooting = False
                    else:
                        print('Вы сделали неверный ввод, попробуйте ещё раз.')
                else:
                    print('Такого выбора не существует, попробуйте ещё раз.')
            else:
                print('Ход второго игрока.')
                choice = input('Выберите и введите ниже предмет, который хотите использовать из ниже перечисленных:\n'
                               f'{gen_items_val[3]}.\n'
                               'Выбор вводить сюда: ')
                if choice == 'Лупа':
                    if gen_items_val[3].count('Лупа') > 0:
                        current_round = (gen_rounds_val[1].split(', '))[0]
                        if current_round == '0':
                            print('Текущая дробь холостая!')
                        else:
                            print('Текущая дробь боевая!')
                        gen_items_val[3] = gen_items_val[3].replace('Лупа, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Пила':
                    if gen_items_val[3].count('Пила') > 0:
                        double_damage = True
                        print('Теперь урон дробовика удвоен!')
                        gen_items_val[3] = gen_items_val[3].replace('Пила, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Сигареты':
                    if gen_items_val[3].count('Сигареты') > 0:
                        if gen_energy_val[2] == gen_energy_val[3]:
                            print('Вы не можете использовать сигареты, так как у вас максимальное количество зарядов!\n'
                                  'Выберите что-нибудь другое.')
                        else:
                            gen_energy_val[2] += 1
                            print(f'Одна энергия востановленна! Теперь у вас {gen_energy_val[2]} энергии.')
                            gen_items_val[3] = gen_items_val[3].replace('Сигареты, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Пиво':
                    if gen_items_val[3].count('Пиво') > 0:
                        current_round = (gen_rounds_val[1].split(', '))[0]
                        if current_round == '0':
                            gen_rounds_val[1] = gen_rounds_val[1].replace('0', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            print('Вы сбросили из магазина холостую дробь.')
                        else:
                            gen_rounds_val[1] = gen_rounds_val[1].replace('1', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            print('Вы сбросили из магазина боевую дробь.')
                        gen_items_val[3] = gen_items_val[3].replace('Пиво, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Наручники':
                    if gen_items_val[3].count('Наручники') > 0:
                        cuffs_on_first_player = True
                        print('Теперь на первого игрока надеты наручники и он пропускает следующий ход.')
                        gen_items_val[3] = gen_items_val[3].replace('Наручники, ', '', 1)
                    else:
                        print('У вас в инвентаре нет такого предмета! Выберите что-нибудь другое.')
                elif choice == 'Дробовик':
                    shoot_choice = input('Введите ниже, в кого вы хотите выстрелить.\n'
                                         'Варианты: В себя, В противника.\n'
                                         'Выбор вводить сюда: ')
                    if shoot_choice == 'В себя':
                        if (gen_rounds_val[1].split(', '))[0] == '0':
                            print('Вам повезло, дробь холостая. Вы можете сделать ещё один ход.')
                            if double_damage:
                                print('Но вы использовали пилу понапрасну! Двойной урон анулирован.')
                                double_damage = False
                            gen_rounds_val[1] = gen_rounds_val[1].replace('0', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                        else:
                            print('Вам не повезло, в дробовике была боевая дробь.')
                            gen_rounds_val[1] = gen_rounds_val[1].replace('1', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            if double_damage:
                                gen_energy_val[2] -= 2
                                double_damage = False
                                if gen_energy_val[2] < 1:
                                    print('Первый игрок победил!')
                                    first_player_points += 1
                                    round_num += 1
                                    break
                                else:
                                    print(f'У вас осталось {gen_energy_val[2]} энергии.')
                                    if cuffs_on_first_player:
                                        print(
                                            'Но есть и хорошие новости! Вы ходите ещё раз, так как надели наручники на противника.')
                                        cuffs_on_first_player = False
                                    else:
                                        who_is_shooting = True
                            else:
                                gen_energy_val[2] -= 1
                                if gen_energy_val[2] < 1:
                                    print('Первый игрок победил!')
                                    first_player_points += 1
                                    round_num += 1
                                    break
                                else:
                                    print(f'У вас осталось {gen_energy_val[2]} энергии.')
                                    if cuffs_on_first_player:
                                        print(
                                            'Но есть и хорошие новости! Вы ходите ещё раз, так как надели наручники на противника.')
                                        cuffs_on_first_player = False
                                    else:
                                        who_is_shooting = True
                    elif shoot_choice == 'В противника':
                        if (gen_rounds_val[1].split(', '))[0] == '0':
                            print('Вам не повезло, в дробовике была холостая дробь.')
                            gen_rounds_val[1] = gen_rounds_val[1].replace('0', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            if double_damage:
                                print('Но вы также не смогли нанести двойной урон противнику, и теперь он анулируется.')
                                double_damage = False
                            if cuffs_on_first_player:
                                print('Вы ходите ещё раз, так как надели наручники на противника.')
                                cuffs_on_first_player = False
                            else:
                                who_is_shooting = True
                        else:
                            print('Вам повезло, в дробовике была боевая дробь.')
                            gen_rounds_val[1] = gen_rounds_val[1].replace('1', '', 1)
                            if gen_rounds_val[1].count(', ') > 0:
                                gen_rounds_val[1] = gen_rounds_val[1].replace(', ', '', 1)
                            if double_damage:
                                gen_energy_val[1] -= 2
                                double_damage = False
                                if gen_energy_val[1] < 1:
                                    print('Второй игрок победил!')
                                    second_player_points += 1
                                    round_num += 1
                                    break
                                else:
                                    print(f'У второго игрока осталось {gen_energy_val[1]} энергии.')
                                    if cuffs_on_first_player:
                                        print('Вы ходите ещё раз, так как надели наручники на противника.')
                                        cuffs_on_first_player = False
                                    else:
                                        who_is_shooting = True
                            else:
                                gen_energy_val[1] -= 1
                                if gen_energy_val[1] < 1:
                                    print('Второй игрок победил!')
                                    second_player_points += 1
                                    round_num += 1
                                    break
                                else:
                                    print(f'У второго игрока осталось {gen_energy_val[1]} энергии.')
                                    if cuffs_on_first_player:
                                        print('Вы ходите ещё раз, так как надели наручники на противника.')
                                        cuffs_on_first_player = False
                                    else:
                                        who_is_shooting = True
                    else:
                        print('Вы сделали неверный ввод, попробуйте ещё раз.')
                else:
                    print('Такого выбора не существует, попробуйте ещё раз.')
    if first_player_points > second_player_points:
        print('По итогам трёх раундов побеждает первый игрок!')
    elif first_player_points < second_player_points:
        print('По итогам трёх раундов побеждает второй игрок!')
    return 'Спасибо за игру!'
game_start = game()
