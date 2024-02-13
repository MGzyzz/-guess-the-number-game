import random
import sys

def binarySearch():
    low = 1
    high = 100
    count = 0
    print("In the game, the commands greater/less are accepted. In case the number is guessed correctly, enter the command yes")
    while low <= high:
        count += 1
        mid = low + (high - low)//2
        choose = input(f"is it: {mid} ")
        if choose == "yes":
            print(f"The number is guessed, it is {mid}. It took {count} tries\n")
            return count

        elif choose == "greater":
            low = mid + 1

        elif choose == "less":
            high = mid - 1

    return -1

def computer_number():
    random_number = random.randint(1,100)

    print("The computer has chosen a number, try to guess it\n")
    count = 0
    while True:
        person = input("Write a number\n")
        count += 1
        if int(person) == random_number:
            print(f"The number is guessed, it is {random_number}. It took {count} tries\n")
            return count

        elif int(person) > random_number:
            print("less")

        elif int(person) < random_number:
            print("greater")

def calculation_of_the_result(count_one: int, count_two: int):
    print(f"\nThe number of tries of the player: {count_two}\n")
    print(f"The number of tries of the computer: {count_one}\n")
    if count_one > count_two:
        return print("The player won!\n")
    elif count_one == count_two:
        return print("It's a tie!\n")
    else:
        return print("The computer won!\n")

def competition():
    person = input("Choose the number of rounds. By default, there are always 3 rounds\n")
    count = 1
    count_person = 0
    count_computer = 0
    random_number = random.randint(1,100)
    if random_number < 50:
        print("\nThe first move belongs to the user\n")
        first_move = 1
    else:
        print("\nThe first move belongs to the computer\n")
        first_move = 2

    if person == "":
        person = 3

    while count <= int(person):
        print(f"Round: {count}")
        if first_move == 1:
            print(f"\n===== The player's move =====\n")
            count_person = binarySearch()
            first_move = 2
            count += 1
        elif first_move == 2:
            print(f"\n===== The computer's move =====\n")
            count_computer = computer_number()
            first_move = 1
            count += 1

    print("\n===== End of game =====\n")
    calculation_of_the_result(count_person, count_computer)
    main_binary()

def main_binary():
    choose = input("Welcome to the game: Choose from the indexes below or you can type the command exit to exit the game\n[1]Computer \n[2]Player\n[3]Competition\n")
    while True:
        match choose:
            case "1":
                print("Choose a number")
                binarySearch()
                main_binary()
            case "2":
                computer_number()
                main_binary()
            case "3":
                competition()
            case "exit":
                sys.exit()
            case _:
                print("Invalid choice, try again")
                continue

main_binary()
