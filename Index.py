import sys
import webbrowser
from random import randint
from character_info import all_characters
from modules import colors
from modules.Characters import *


# finds character inside of dictionary
def get_character(character):
    if character.lower() in all_characters:
        return all_characters[character.lower()]
    else:
        return None  # character not found


# to prompt users to fix their mistakes in a yes/no question
def yes_or_no_choice(input_text):
    while (text_choice := str(input(input_text)).lower()) not in ['n', 'no', 'nope']:
        print()
        if text_choice in ['y', 'yes', 'sure']:
            return True
        else: # prompt user to fix mistake made
            user_error("Invalid choice, please say either 'yes' or 'no'\n")
    print()
    return False


# returns character if found or None if not found
# handles if character not found and would like to add character to text doc
def find_character(character_choice):
    character = get_character(character_choice)
    if not character:
        user_error('Superhero/Villain name not found!\n')
        input_text = 'Would you like to request developers to add this character: '
        if yes_or_no_choice(input_text):
            request_a_character(character_choice)
    return character


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


def one_vs_one(player_one, player_two):
    # Checks which fighter has a higher fighting stat to get a slight bonus
    one_stat_total, one_name = player_one.total_stats(), player_one.get_name()
    two_stat_total, two_name = player_two.total_stats(), player_two.get_name()
    one_f_stat, two_f_stat = player_one.get_stat("Fighting"), player_two.get_stat("Fighting")
    if one_f_stat > two_f_stat:
        return character_fight(one_stat_total, one_name, two_stat_total, two_name, True)
    elif one_f_stat < two_f_stat:
        return character_fight(two_stat_total, two_name, one_stat_total, one_name, True)
    # equal fighting stat there is a random bonus given to each fighter that is added to their total
    elif one_f_stat == two_f_stat:
        return character_fight(one_stat_total, one_name, two_stat_total, two_name, False)


def two_vs_two(team1char1, team1char2, team2char1, team2char2):
    # grab stats for each of the teams
    team1power = team1char1.total_stats() + team1char2.total_stats()
    team2power = team2char1.total_stats() + team2char2.total_stats()

    if team1power > team2power:  # apply bonuses to teams the same way we did for 1v1
        return character_fight(team1power, 'Team 1', team2power, 'Team 2', True)
    elif team1power < team2power:
        return character_fight(team2power, 'Team 2', team1power, 'Team 1', True)
    elif team1power == team2power:
        return character_fight(team1power, 'Team 1', team2power, 'Team 2', False)


# Pick a random 2 characters to fight in the list
# Remove the loser in the list of active characters
# Evaluate for the winner and repeat until only 1 character left
def free_for_all(ffa_characters):
    remove_char_index = 0
    while len(ffa_characters) > 1:
        # reset the fighting characters
        char_one_index = char_two_index = randint(0, len(ffa_characters) - 1)
        char1 = char2 = ffa_characters[char_one_index]
        while char2 == char1:
            char_two_index = randint(0, len(ffa_characters) - 1)
            char2 = ffa_characters[char_two_index]

        fight_winner = one_vs_one(char1, char2)

        if fight_winner == char2.get_name():
            remove_char_index = char_one_index
        elif fight_winner == char1.get_name():
            remove_char_index = char_two_index
        else: # if draw then choose random loser
            remove_char_index = [char_one_index, char_two_index][randint(0, 1)]

        del ffa_characters[remove_char_index] # remove loser from available characters

    return ffa_characters[0] # winner will always be last character in array


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
        while selecting:
            char_name = input('Enter a character name for the free for all: ')
            print()
            char_name = find_character(char_name)
            ffa_characters.append(char_name)
            if len(ffa_characters) > 3:
                selecting = yes_or_no_choice('Select another character (yes / no): ')

        # Start free for all
        winner = free_for_all(ffa_characters)
        print(colors.green + 'The winner is...' + winner + '!', colors.reset, '\n')
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
        characters = get_character(choice)
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
            if yes_or_no_choice('List characaters in the Superhero/Villain index? '):
                print(', '.join(sorted([x.capitalize() for x in all_characters.keys()])))
                print('\n')
            
            choice = str(input('Enter a Superhero/Villain name: '))
            print()
            character = find_character(choice)
            if character:
                print(character)
                time.sleep(1)
                if yes_or_no_choice('Would you like to view a photo of this character: '):
                    character.show_image()
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
    print(colors.red, message, colors.reset)


if __name__ == '__main__':
    start()
