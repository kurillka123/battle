from random import randint

plaer_name ='вася'
plaer_level = 1
plaer_hp = 50
plaer_xp = 0
plaer_money = 5
game bank = 0
while True:
    print('-----------------------')
    print('1 - начать битву')
    print('2 - уйти')
    print('3 - купить предметы')
    print('4 - сыграть в кости')
    option = input('Введите номер ответа и нажмите ENTER:')
    if option == '1':

        anemy_name ='петя'
        anemy_level = 1
        anemy_hp = 50
        while True:
            input('нажмите ENTER тобы сделать ход')
            plaer_attak = randint(0, 10) * plaer_level
            anemy_hp -= plaer_attak
            print(plaer_name, 'ударил', anemy_name, 'на', plaer_attak, 'жизней')
            print('у', anemy_name, 'осталось', anemy_hp, 'жизней')
            if anemy_hp <= 0:
                print(plaer_name, 'победил')
                plaer_xp += anemy_level
                print(plaer_name, 'получил', anemy_level, 'опыта')
                if plaer_xp % 10 == 0:
                    plaer_level += plaer_xp // 10
                    plaer_xp += anemy_level  % 10
                    print(plaer_name, 'получил', plaer_level, 'уровень')
                    break        
            anemy_attak = randint(0, 10) * anemy_level
            plaer_hp -= anemy_attak
            print(anemy_name, 'ударил', plaer_name, 'на', plaer_attak, 'жизней')
            print('у', plaer_name, 'осталось', plaer_hp, 'жизней')
            if plaer_hp <= 0:
                print(plaer_name, 'проиграл')
                break 
    elif option == '2':
        print(plaer_name, 'ушел')
        break
    elif option == '3':
        print(plaer_name, 'пришёл к продавцу')
        print('выбор покупок')
        print('-------------------------------')
        print('1 - зелье опыта = 30 трюков')
        print('2 - ')
    elif option == '4'
        #todo: провурить ставку, >0, НЕ БОЛЬШЕ моих денег
        if plaer_money > 0:
            game bank = input('введите сумму ставки')
            
    
