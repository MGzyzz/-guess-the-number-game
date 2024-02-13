import random
import sys

def binarySearch():
    low = 1
    high = 100
    count = 0
    print("В игре принимаются команды greater/less. В случае правильного угадонного числа пропишите команду yes")
    while low <= high:
        count += 1
        mid = low + (high - low)//2
        choose = input(f"is it: {mid} ")
        if choose == "yes":
            print(f"Число угадано, это {mid}. Попыток понадобилось: {count}\n")
            return count

        elif choose == "greater":
            low = mid + 1

        elif choose == "less":
            high = mid - 1

    return -1



def computer_number():
    random_number = random.randint(1,100)

    print("Компьютер загадал число, постарайтесь угадать его\n")
    count = 0
    while True:
        person = input("Напишите число\n")
        count += 1
        if int(person) == random_number:
            print(f"Число угадано, это {random_number}. Попыток понадобилось: {count}\n")
            return count


        elif int(person) > random_number:
            print("less")

        elif int(person) < random_number:
            print("greater")


def calculation_of_the_result(count_one: int, count_two: int):
    print(f"\nКоличество попыток у игрока: {count_two}\n")
    print(f"Количество попыток у компьютера: {count_one}\n")
    if count_one > count_two:
        return print("Победил пользователь!\n")
    elif count_one == count_two:
        return print("Ничья!\n")
    else:
        return print("Победил компьютер!\n")

def competition():
    person = input("Выберите количество раундов. По умолчанию всегда стоит 3 раунда\n")
    count = 1
    count_person = 0
    count_computer = 0
    random_number = random.randint(1,100)
    if random_number < 50:
        print("\nПервый ход у пользователя\n")
        first_move = 1
    else:
        print("\nПервый ход у компьютера\n")
        first_move = 2

    if person == "":
        person = 3

    while count <= int(person):
        print(f"Раунд {round()}")
        if first_move == 1:
            print(f"\n===== ход пользователя =====\n")
            count_person = binarySearch()
            first_move = 2
            count += 1
        elif first_move == 2:
            print(f"\n===== ход компьютера =====\n")
            count_computer = computer_number()
            first_move = 1
            count += 1


    print("\n===== Конец Игры =====\n")
    calculation_of_the_result(count_person, count_computer)
    main_binare()



def main_binare():
    choose = input("Добро пожаловать в игру: Выбор идет по индексам ниже или вы можете написать команду exit для выхода с игры\n[1]Компьютер \n[2]Игрок\n[3]Соревнование\n")
    while True:
        match choose:
            case "1":
                print("Загадайте число")
                binarySearch()
                main_binare()
            case "2":
                computer_number()
                main_binare()
            case "3":
                competition()
            case "exit":
                sys.exit()
            case _:
                print("Некорректный выбор, попробуйте еще раз")
                continue

main_binare()


