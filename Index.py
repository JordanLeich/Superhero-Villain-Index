import sys
import webbrowser
import json
from modules.Characters import *
from modules import colors


# recursive if error
def create_characters(character_type, character_name):
    with open('characters.json', 'r') as file:
        characters = json.load(file)
    if character_name in characters[character_type]: 
        return Character(characters[character_type][character_name])
    else:
        error_message(f'{character_type.capitalize()} name not found!')
        hero_or_villian_selection(character_type)  # allow user to try again

# recursive if error
def image_handling(character, character_type):
    choice = str(input(f'Would you like to view a photo of this {character_type} (yes / no): '))
    print()
    if choice.lower() in ['y', 'yes', 'sure']:
        character.show_image()
    elif choice.lower() not in ['n', 'no', 'nope']:
        error_message('input needs to be "yes" or "no"') 
        image_handling(character, character_type) # try to show image again

def hero_or_villian_selection(character_type):
    character_choice = str(input(f'Enter a {character_type} name: '))
    print()
    character = create_characters(character_type, character_choice.lower())
    if character:
        character.print_stats()
        time.sleep(2)
        image_handling(character, character_type)
    time.sleep(2)
    
# recursive if error
def extra_menu():
    choice = int(input('''(1) View project releases/newest changes
(2) Credits
(3) Return to main menu
(4) Exit Program

Which option would you like to pick: '''))
    print()
    if choice == 1:
        webbrowser.open('https://github.com/JordanLeich/Superhero-Index/releases')
    elif choice == 2:
        webbrowser.open('https://github.com/JordanLeich/Superhero-Index/graphs/contributors')
    elif choice == 3:
        return
    elif choice == 4:
        sys.exit()
    else:
        error_message('choice should be a number between 1-4')
        extra_menu()

def error_message(error_msg):
    print(colors.red + f'Error: {error_msg}\n', colors.reset)

def main():  # sourcery no-metrics
    while True: # exit through choice 4
        choice = int(input('''(1) Search the superhero index
(2) Search the villain index  
(3) Extras
(4) Exit Program

Which option would you like to pick: '''))
        print()

        if choice == 1:
            hero_or_villian_selection('superhero')
        elif choice == 2:
          hero_or_villian_selection('villain')
        elif choice == 3:
            extra_menu()
            time.sleep(2)
            main()
        elif choice == 4:
            sys.exit()
        else:
            error_message('choice should be a number between 1-4')


if __name__ == '__main__':
    main()
