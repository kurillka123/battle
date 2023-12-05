import os
from random import randint


def game():
    healing_potion = 0
    player_name = input("Как вас зовут? ")
    player_level = 1000
    player_hp = 50 * player_level
    player_xp = 0
    player_money = 1000

    visit_rock(player_name, player_hp, player_money, player_xp, player_level)

def visit_rock(player_name, player_hp, player_money, player_xp, player_level, ):
    os.system("cls")
    print("_________________________")
    print("1 = начать игру")
    print("2 = уйти")
    print("3 = пойти в магазин")
    print("4 = сыграть в казино")
    print("_________________________")
    option = input("Введите номер ответа и нажмите ENTER ")
    if option == "1":
        while True:
            from random import randint
            player_hp * player_level
            anemy_name = ("Петя")
            anemy_level = 1
            anemy_hp = 50 * anemy_level
            print(player_name, "сразится проитив", anemy_name)
            while True:
                input('нажмите ENTER тобы сделать ход')
                plaer_attak = randint(1, 10) * player_level
                anemy_hp -= plaer_attak
                print(player_name, 'ударил', anemy_name, 'на', plaer_attak, 'жизней')
                print('у', anemy_name, 'осталось', anemy_hp, 'жизней')
                if anemy_hp <= 0:
                    print(player_name, 'победил')
                    player_xp += anemy_level
                    print(player_name, 'получил', anemy_level, 'опыта')
                    player_money += 15
                    print('у вас', player_money, "монет")
                    visit_rock(player_name, player_hp, player_money, player_xp, player_level)
                    if player_xp % 10 == 0:
                        player_level += player_xp // 10
                        player_xp += anemy_level  % 10
                        print(player_name, 'получил', plaer_level, 'уровень')
                        break        
                anemy_attak = randint(0, 10) * anemy_level
                player_hp -= anemy_attak
                print(anemy_name, 'ударил', player_name, 'на', plaer_attak, 'жизней')
                print('у', player_name, 'осталось', player_hp, 'жизней')
                if player_hp <= 0:
                    print(player_name, 'проиграл')
                    input('нажмите ENTER чтобы начать с начала')
                    print('-----------------------------------')
                    game()
                    break 
                enemy_attack = randint(0, 10) + anemy_level
                player_hp -= enemy_attack
                print(anemy_name, "ударил", player_name, "на", enemy_attack, "жизней")
                print("У", player_name, "стало", player_hp, "жизней")    
                break        
            print("бой окончен")
            
    elif option == "2":
        print('вы вышли из игры')
        game()
#---------------------------------------------------------#        
    elif option == "3":
        while True:
            print('------------------------------------')
            print("Вот список всех товаров")
            print("0 - уйти")
            print("1 - Восстановить все хп = 25 монет")
            print('2 - добавить 1 уровень = 30 монет')
            print('3 - повысить максимальное количество хп = 50 монет')
            print('4 - купить зелье лечения = 10 монет')
            buy = input("Что будем делать?")
            print('------------------------------------')
            if buy == "0":
                visit_rock(player_name, player_hp, player_money, player_xp, player_level)
            elif buy == "1":
                if player_money >= 25 and player_hp < 100:
                    player_money -= 25
                    player_hp = 10 * player_level
                    print("у вас", player_hp, "хп")
                    print(player_money, "монет")
            elif buy == '2':
                if player_money >= 29:
                    player_money -= 30
                    player_level += 1
                    print('у вас', player_level, 'уровень')
            elif buy == '3':
                if player_money >= 49:
                    player_money -= 50
                    player_hp = 100 * player_level
                    print('у вас 100 жизней')
            elif buy == '4':
                if player_money >= 9:
                    player_money -= 10
                    healing_potion += 1
                    print('у вас 100 жизней')
#--------------------------------------------------------------------------#                  
    elif option == "4":
        while player_money > 0:
                print("_________________________")
                print("1 = будем")
                print("2 = уйти")                     
                print("_________________________")
                play_activ = input("Будем играть или уйдём?")
                if play_activ == "1":           
                    from random import randint
                    print("_________________________")
                    print("1 = сыграть в кубик")
                    print("2 = сыграть в рулетку")
                    print("3 = уйти")                     
                    print("_________________________")
                    play = input("Во что хотите сыграть?")
                    if play == '1':
                        bet = int(input("Сколько поставить?"))
                    if bet >= 1:
                        if play == "1":
                            player_1 = randint(1, 6)
                            player_2 = randint(1, 6)

                            print("игрок выбросил", player_1 )
                            print("компьютер выбросил", player_2 )

                            if player_1 > player_2:
                                player_money += bet * 2
                                print(player_money, "монет")
                                print("Вы победили")
                            elif player_1 < player_2:
                                player_money -= bet
                                print(player_money, "монет")
                                print("Победил комьпьютер")
                            else:
                                print("ничья")
                                print(player_money, "монет")

                        elif play == "2":
                            color = randint(1, 2)
                            stavka = input("на какой цвет хотите поставить? (красный/чёрный) ")
                            if color == 1:
                                print("красный")
                                if  stavka == "красный":
                                    player_money += bet * 2
                                elif stavka == "чёрный":
                                    player_money -= bet
                                    print(player_money, "монет")
                            elif color == 2:
                                print("чёрный")
                                if  stavka == "красный":
                                    player_money -= bet
                                    print(player_money, "монет")
                                elif stavka == "чёрный":
                                    player_money += bet * 2
                                    print(player_money, "монет")
                    elif play == "3":
                        visit_rock(player_name, player_hp, player_money, player_xp, player_level)
                    else:
                        print("нету такого числа")       
                elif play_activ == "2":
                    visit_rock(player_name, player_hp, player_money, player_xp, player_level)


game()
