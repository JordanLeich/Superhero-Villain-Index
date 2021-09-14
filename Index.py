import sys
import webbrowser
from modules.Heroes import *
from modules.Villains import *
from modules import colors


def create_heroes():
    Superman = Hero('Superman', 'Immortal age/mid 20 or 30s', 'alive', 'DC', 'Justice League',
                    'super strength, flight, invulnerability, super speed, heat vision, freeze breath, x-ray vision, '
                    'superhuman hearing, healing factor',
                    13000, 'images/portraits/superman.jpg')
    Batman = Hero('Batman', 48, 'alive', 'DC', 'Justice League', 'no superpowers', 145, 'images/portraits/batman.jpg')
    Thor = Hero('Thor', 1500, 'alive', 'Marvel',
                'Avengers',
                'superhuman strength, speed, agility, durability and immunity to most diseases', 493000,
                'images/portraits/thor.jpg')
    Hulk = Hero('Hulk', 49, 'alive', 'Marvel', 'Avengers', 'strength ', 6900, 'images/portraits/hulk.jpg')
    Daredevil = Hero('Daredevil', 25, 'alive', 'Marvel', 'none',
                     'Superhuman senses Echolocative radar sense Skilled acrobat, martial artist, and stick fighter '
                     'Utilization of specially-designed billy club',
                     83, 'images/portraits/daredevil.jpg')
    Deadpool = Hero('Deadpool', 'immortal, over 800', 'alive', 'Marvel', 'none',
                    'accelerated healing factor',
                    115, 'images/portraits/deadpool.jpeg')
    Wolverine = Hero('Wolverine', 'over 200', 'alive', 'Marvel', 'X-Men',
                     'superhuman strength and reflexes, enhanced senses and tracking abilities, and a special healing'
                     ' power that also slows his aging.',
                     79, 'images/portraits/wolverine.jpg')
    Captain_America = Hero('Captain America', 99, 'unknown', 'Marvel', 'Avengers',
                           'Peak-Human Condition, Accelerated Healing Factor, Enhanced Intelligence, Longevity',
                           94, 'images/portraits/captainamerica.jpg')
    Iceman = Hero('Iceman', 'unknown', 'alive', 'Marvel', 'X-Men',
                  'ability to manipulate ice and cold by freezing water vapor around him',
                  517, 'images/portraits/iceman.jpg')
    Human_Torch = Hero('Human Torch', 'mid 20s', 'alive', 'Marvel', 'Fantastic Four',
                       'engulf his entire body in flames, fly, absorb fire harmlessly into his own body, and control '
                       'any nearby fire by sheer force of will',
                       126, 'images/portraits/humantorch.jpg')
    Nightcrawler = Hero('Nightcrawler', 'mid 20s', 'dead but has been resurrected many times', 'Marvel', 'X-Men',
                        'superhuman agility, the ability to teleport, and adhesive hands and feet',
                        514, 'images/portraits/nightcrawler.jpg')
    Hawkeye = Hero('Hawkeye', '47', 'dead', 'Marvel', 'Avengers',
                   'Master archer and marksman Expert tactician, acrobat and hand-to-hand combatant Using a variety of '
                   'trick arrows As Goliath: Superhuman strength and durability Size and mass manipulation',
                   51, 'images/portraits/hawkeye.jpg')
    Doctor_Strange = Hero('Doctor Strange', '42', 'alive', 'Marvel', 'Avengers',
                          'Mastery of magic Utilizes mystical artifacts, such as the Cloak of Levitation and the Eye '
                          'of Agamotto Genius-level intellect Skilled martial artist Gifted physician and surgeon',
                          8600, 'images/portraits/drstrange.jpg')
    Cyclops = Hero('Cyclops', '36', 'dead', 'Marvel', 'X-Men',
                   'Emits powerful beams of energy from his eyes',
                   108, 'images/portraits/cyclops.jpg')
    Spiderman = Hero('Spiderman', '28', 'dead', 'Marvel', 'Avengers',
                     'Peter was bitten by a radioactive spider. The spider bite gave Peter spider-like powers with'
                     'super strength and reflexes',
                     200, 'images/portraits/spiderman.jpg')

    return [Superman, Batman, Thor, Hulk, Daredevil, Deadpool, Wolverine, Captain_America, Iceman, Human_Torch,
            Nightcrawler, Hawkeye, Doctor_Strange, Cyclops, Spiderman]


def create_villains():
    Thanos = Hero('Thanos', '1000', 'dead', 'Marvel', 'unknown',
                  'all types of poison, disease, and telepathic attack',
                  7600, 'images/portraits/thanos.jpg')
    Loki = Hero('Loki', 1000, 'deceased', 'Marvel', 'none',
                'strength, durability, and longevity far superior to humans', 616, 'images/portraits/loki.jpg')

    return [Loki, Thanos]


def start():  # sourcery no-metrics
    choice = int(input('''(1) Search the superhero index
(2) Search the villain index  
(3) Extras
(4) Exit Program

Which option would you like to pick: '''))
    print()

    if choice == 1:
        choice = str(input('Enter a superhero name: '))
        print()
        heroes = create_heroes()
        for h in heroes:
            if h.name.lower() == choice.lower():
                Hero.print_hero(h)
                time.sleep(2)
                choice = str(input('Would you like to view a photo of this superhero (yes / no): '))
                print()
                if choice.lower() in ['y', 'yes', 'sure']:
                    Hero.show_image(h)
                    time.sleep(2)
                    start()
                elif choice.lower() in ['n', 'no', 'nope']:
                    time.sleep(1)
                    start()
                else:
                    error_message()
        if choice.lower() != h.name.lower():
            print(colors.red + 'Superhero name not found!', colors.reset, '\n')
            time.sleep(2)
            start()
        else:
            error_message()
    elif choice == 2:
        choice = str(input('Enter a villain name: '))
        print()
        villains = create_villains()
        for v in villains:
            if v.name.lower() == choice.lower():
                Villain.print_villain(v)
                time.sleep(2)
                choice = str(input('Would you like to view a photo of this villain (yes / no): '))
                print()
                if choice.lower() in ['y', 'yes', 'sure']:
                    Villain.show_image(v)
                    time.sleep(2)
                    start()
                elif choice.lower() in ['n', 'no', 'nope']:
                    time.sleep(1)
                    start()
                else:
                    error_message()
        if choice.lower() != v.name.lower():
            print(colors.red + 'Villain name not found!', colors.reset, '\n')
            time.sleep(2)
            start()
        else:
            error_message()
    elif choice == 3:
        choice = int(input('''(1) View project releases/newest changes
(2) Credits
(3) Return to main menu
(4) Exit Program

Which option would you like to pick: '''))
        print()
        if choice == 1:
            webbrowser.open('https://github.com/JordanLeich/Superhero-Index/releases')
            time.sleep(2)
            start()
        elif choice == 2:
            webbrowser.open('https://github.com/JordanLeich/Superhero-Index/graphs/contributors')
            time.sleep(2)
            start()
        elif choice == 3:
            start()
        elif choice == 4:
            sys.exit()
        else:
            error_message()
    elif choice == 4:
        sys.exit()
    else:
        error_message()


def error_message():
    print(colors.red + 'Error found!\n', colors.reset)
    time.sleep(2)
    start()


if __name__ == '__main__':
    running = True

    if running:
        start()
    else:
        running = False
        print(colors.red + 'Fatal running error found!\n', colors.reset)
        time.sleep(2)
        sys.exit()
