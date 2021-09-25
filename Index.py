from random import randint
import sys
import webbrowser
from modules import colors
from modules.Characters import *
from character_info import all_characters


# finds character inside of dictionary
def find_characters(character):
    if character.lower() in all_characters:
        return all_characters[character]
    else:
        return None  # character not found


# returns character if found or None if not found
# handles if character not found and would like to add character to text doc
def find_character(character):
    characters = find_characters(character)
    if not characters:
        user_error('Superhero/Villain name not found!\n')
        write_to_text_choice = str(input(
            'Would you like to request developers to add this superhero/villain '
            '(yes / no): '))
        print()
        if write_to_text_choice.lower() in ['y', 'yes', 'sure']:
            request_a_character(character)
        elif write_to_text_choice.lower() not in ['n', 'no', 'nope']:
            error_message()  # TODO prompt user to fix mistake made
    return characters


def character_total(character):  # Gets total value from all of the characters traits
    return character.durability + character.energy + character.fighting + character.intelligence + character.speed + character.strength


# characters battle it out
# generic function serving one_vs_one and two_vs_two
def character_fight(first_character, first_name, second_character, second_name, stat_not_equal):
    # bonuses randomly distributed to give the character with less fighting stats a chance
    char_one_total = first_character + randint(0, 6)
    if stat_not_equal:
        char_one_total += randint(0, 6)
    # character with lower fighting stat only gets 1 bonus but at least it cannot be a 0
    # stat_not_equal will evaluate to 1 when True, 0 when False
    char_two_total = second_character + randint(stat_not_equal, 6)
    if char_one_total > char_two_total:
        return first_name
    elif char_one_total < char_two_total:
        return second_name
    else:
        return "It's a draw!"


def one_vs_one(first_character, second_character):
    # Checks which fighter has a higher fighting stat to get a slight bonus
    character_one, one_name = character_total(first_character), first_character.name
    character_two, two_name = character_total(second_character), second_character.name
    if first_character.fighting > second_character.fighting:
        return character_fight(character_one, one_name, character_two, two_name, True)
    elif first_character.fighting < second_character.fighting:
        return character_fight(character_two, two_name, character_one, one_name, True)
    # equal fighting stat there is a random bonus given to each fighter that is added to their total
    elif first_character.fighting == second_character.fighting:
        return character_fight(character_one, one_name, character_two, two_name, False)


def two_vs_two(team1char1, team1char2, team2char1, team2char2):
    # grab stats for each of the teams
    team1power = character_total(team1char1) + character_total(team1char2)
    team2power = character_total(team2char1) + character_total(team2char2)

    if team1power > team2power:  # apply bonuses to teams the same way we did for 1v1
        return character_fight(team1power, 'Team 1', team2power, 'Team 2', True)
    elif team1power < team2power:
        return character_fight(team2power, 'Team 2', team1power, 'Team 1', True)
    elif team1power == team2power:
        return character_fight(team1power, 'Team 1', team2power, 'Team 2', False)


def free_for_all(ffa_characters):
    # sourcery skip: inline-immediately-returned-variable
    # Perform free for all battle
    # Pick a random 2 characters to fight in the list
    # Remove the loser in the list of active characters
    # Pick a random character in the list who hasn't fought yet
    # Evaluate for the winner and repeat until there is only 1 character left
    fightactive = True
    char1 = None
    char2 = None

    while fightactive:
        while char1 is None:
            char1 = ffa_characters[randint(0, len(ffa_characters) - 1)]
        while char2 is None or char2 == char1:
            char2 = ffa_characters[randint(0, len(ffa_characters) - 1)]

        # Perform fight between 2 characters and set the winner and loser
        fightwinner = one_vs_one(char1, char2)

        if fightwinner == char1.name:
            fightloser = char2.name
        elif fightwinner == char2.name:
            fightloser = char1.name
        # if its a draw then default winner to char2
        # TODO decide what to do if its a draw, maybe randomly decide between the 2 fighters.
        elif fightwinner == 'It\'s a draw!':
            fightloser = char2.name



        # check for the loser and remove from the list of available characters to fight
        for count, fighter in enumerate(ffa_characters):
            if ffa_characters[count] is not None:
                if fighter.name == fightloser:
                    ffa_characters[count] = None

        # reset the fighting characters
        char1 = None
        char2 = None

        # check if there is 1 active character left, if so its the winner
        count = 0
        for x in ffa_characters:
            if x:
                count += 1
                if count == 1:
                    fightactive = False
                else:
                    fightactive = True

    winner = fightwinner
    return winner


# recursive until character properly selected
def prompt_character_selection(input_text):
    character_choice = str(input(input_text))
    print()
    first = find_character(character_choice)
    if not first:
        return prompt_character_selection(input_text)
    return first


# recursive if improper input selected in menu to prompt user
def versus():
    # Prompt for battle mode:
    mode = input('(1) 1v1\n'
                 '(2) 2v2\n'
                 '(3) Free for all\n'
                 '(4) Return to Main Menu\n\n'
                 'Which versus battle mode would you like to pick: ')
    print()
    if mode == '1':
        print(colors.green + '1v1 mode selected\n', colors.reset)
        first_character = prompt_character_selection('Enter a Superhero/Villain name: ')
        second_character = prompt_character_selection('Enter another Superhero/Villain name: ')

        print('Now starting the battle!\n')
        time.sleep(1)
        winner = one_vs_one(first_character, second_character)
        print(colors.green + 'The winner is... ' + winner + '!\n', colors.reset)

    elif mode == '2':
        print(colors.green + '2v2 mode selected\n', colors.reset)
        # Prompt for characters on team 1
        team1char1 = prompt_character_selection('Enter first character for team 1: ')
        team1char2 = prompt_character_selection('Enter second character for team 1: ')
        # Prompt for characters on team 2
        team2char1 = prompt_character_selection('Enter first character for team 2: ')
        team2char2 = prompt_character_selection('Enter second character for team 2: ')
        winning_team = two_vs_two(team1char1, team1char2, team2char1, team2char2)
        print(colors.green + 'The winner is... ' + winning_team + '!\n', colors.reset)

    elif mode == '3':
        # Prompt for character select , store in a list and then prompt for more characters
        print(colors.green + 'Free for all mode selected\n', colors.reset)
        ffa_characters = []
        selecting = True
        while selecting or len(ffa_characters) < 3:
            char_name = input('Enter a character name for the free for all: ')
            print()
            char_name = find_character(char_name)
            ffa_characters.append(char_name)
            if len(ffa_characters) < 3:
                continue
            keep_selecting = input('Select another character (yes / no): ')
            print()
            if keep_selecting.lower() in ['y', 'yes', 'sure']:
                selecting = True
            elif keep_selecting.lower() in ['n', 'no', 'nope']:
                selecting = False

        # Start free for all
        winner = free_for_all(ffa_characters)
        print(colors.green + 'The winner is :' + winner, colors.reset, '\n')
    elif mode == '4':
        print('Returning the Main Menu\n')
    else:  # any choice besides those listed
        print('Invalid choice, please choose an option\n')
        versus()
    time.sleep(2)


def request_a_character(choice):
    with open("characters_to_add.txt", "a") as f:  # file closes when outside this code block
        f.write(str(choice) + '\n')
    print(colors.green + 'Name has been added to the list! You can now go to '
                         'https://github.com/JordanLeich/Superhero-Villain-Index, fork the project, create '
                         'a pull request, and your text file with hero/villain names will be reviewed by '
                         'the developers.\n', colors.reset)
    time.sleep(3)


# will be recursive when an error - so to prompt user with menu and fix their error
def extras_menu():
    choice = input('(1) View project releases/newest changes\n'
                   '(2) Credits\n'
                   '(3) Request a hero/villain to be added\n'
                   '(4) Return to main menu\n'
                   '(5) Exit Program\n\n'
                   'Which option would you like to pick: ')
    print()
    if choice == '1':
        webbrowser.open('https://github.com/JordanLeich/Superhero-Index/releases')
        time.sleep(2)
    elif choice == '2':
        webbrowser.open('https://github.com/JordanLeich/Superhero-Index/graphs/contributors')
        time.sleep(2)
    elif choice == '3':
        choice = str(input('Enter the name of the hero/villain you would like added: '))
        print()
        characters = find_characters(choice)
        if characters:
            user_error('This hero/villain is already included in the index!\n')
        else:
            request_a_character(choice)
    elif choice == '5':
        sys.exit()
    elif choice != '4':  # any choice besides those listed or return menu
        print('Invalid choice, please choose one of the available options\n')
        extras_menu()


def start():  # sourcery no-metrics
    while True:
        choice = input('(1) Search the Superhero/Villain index\n'
                       '(2) Versus battles\n'
                       '(3) Extras\n'
                       '(4) Exit Program\n\n'
                       'Which option would you like to pick: ')
        print()
        if choice == '1':
            choice = str(input('Do you want look at the Superhero/Villain list? '))
            print()
            if choice.lower() in ['y', 'yes', 'sure']:
                listOfHero = list(all_characters.keys())
                listOfHero.sort()
                for x in listOfHero:
                    print(x.capitalize(), end=', ')
                print('\n')
            elif choice.lower() not in ['n', 'no', 'nope']:
                # handle improper input -- anything besides 'no'
                error_message()
            choice = str(input('Enter a Superhero/Villain name: '))
            print()
            characters = find_character(choice)
            if characters:
                characters.print_hero()
                time.sleep(2)
                choice = str(
                    input('Would you like to view a photo of this Superhero/Villain (yes / no): '))
                print()
                if choice.lower() in ['y', 'yes', 'sure']:
                    characters.show_image()
                elif choice.lower() not in ['n', 'no', 'nope']:
                    # handle improper input -- anything besides 'no'
                    error_message()
                time.sleep(1)
        elif choice == '2':
            versus()
        elif choice == '3':
            extras_menu()
        elif choice == '4':
            sys.exit()
        else:  # any choice besides those listed
            print('Invalid choice, please choose an option\n')


# to notify user of an error they made
def user_error(message):
    print(colors.red + message, colors.reset)


def error_message():
    print(colors.red + 'Error found!\n', colors.reset)
    time.sleep(2)


if __name__ == '__main__':
    start()
