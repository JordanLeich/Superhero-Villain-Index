import sys
import time
import webbrowser

from modules import colors
from PIL import Image


class Hero:
    def __init__(self, name, age, status, creator, team, powers, power_ranking, image_path):
        self.name = name
        self.age = age
        self.status = status
        self.creator = creator
        self.team = team
        self.powers = powers
        self.power_ranking = power_ranking
        self.image_path = image_path

    def print_hero(self):
        print('Superhero Name: ' + self.name + '\n'
                                               'Age: ' + str(self.age) + '\n'
                                                                         'Status: ' + self.status + '\n'
                                                                                                    'Creator: ' + self.creator + '\n'
                                                                                                                                 'Team: ' + self.team + '\n'
                                                                                                                                                        'Powers: ' + self.powers + '\n'
                                                                                                                                                                                   'Power Ranking: ' + str(
            self.power_ranking) + '\n')

    def show_image(self):
        img = Image.open(self.image_path)
        img.show(self.image_path)
        time.sleep(2)


def create_heroes():
    Superman = Hero('Superman', 'Immortal age/mid 20 or 30s', 'alive', 'DC', 'Justice League',
                    'super strength, flight, invulnerability, super speed, heat vision, freeze breath, x-ray vision, superhuman hearing, healing factor',
                    13000, 'images/portraits/superman.jpg')
    Batman = Hero('Batman', 48, 'alive', 'DC', 'Justice League', 'no superpowers', 145, 'images/portraits/batman.jpg')
    Thor = Hero('Thor', 1500, 'alive', 'Marvel',
                'Avengers',
                'superhuman strength, speed, agility, durability and immunity to most diseases', 493000,
                'images/portraits/thor.jpg')
    Loki = Hero('Loki', 1000, 'deceased', 'Marvel', 'none',
                'strength, durability, and longevity far superior to humans', 616, 'images/portraits/loki.jpg')
    Hulk = Hero('Hulk', 49, 'alive', 'Marvel', 'Avengers', 'strength ', 6900, 'images/portraits/hulk.jpg')
    Daredevil = Hero('Daredevil', 25, 'alive', 'Marvel', 'none',
                     'Superhuman senses Echolocative radar sense Skilled acrobat, martial artist, and stick fighter Utilization of specially-designed billy club',
                     83, 'images/portraits/daredevil.jpg')
    Deadpool = Hero('Deadpool', 'immortal, over 800', 'alive', 'Marvel', 'none',
                    'accelerated healing factor',
                    115, 'images/portraits/deadpool.jpeg')
    Wolverine = Hero('Wolverine', 'over 200', 'alive', 'Marvel', 'X-Men',
                     'superhuman strength and reflexes, enhanced senses and tracking abilities, and a special healing power that also slows his aging.',
                     79, 'images/portraits/wolverine.jpg')
    Captain_America = Hero('Captain America', 99, 'unknown', 'Marvel', 'Avengers',
                           'Peak-Human Condition, Accelerated Healing Factor, Enhanced Intelligence, Longevity',
                           94, 'images/portraits/captainamerica.jpg')
    Iceman = Hero('Iceman', 'unknown', 'alive', 'Marvel', 'X-Men',
                  'ability to manipulate ice and cold by freezing water vapor around him',
                  517, 'images/portraits/iceman.jpg')
    Human_Torch = Hero('Human Torch', 'mid 20s', 'alive', 'Marvel', 'Fantastic Four',
                       'engulf his entire body in flames, fly, absorb fire harmlessly into his own body, and control any nearby fire by sheer force of will',
                       126, 'images/portraits/humantorch.jpg')
    Nightcrawler = Hero('Nightcrawler', 'mid 20s', 'dead but has been resurrected many times', 'Marvel', 'X-Men',
                        'superhuman agility, the ability to teleport, and adhesive hands and feet',
                        514, 'images/portraits/nightcrawler.jpg')
    Thanos = Hero('Thanos', '1000', 'dead', 'Marvel', 'unknown',
                  'all types of poison, disease, and telepathic attack',
                  7600, 'images/portraits/thanos.jpg')
    Hawkeye = Hero('Hawkeye', '47', 'dead', 'Marvel', 'Avengers',
                   'Master archer and marksman Expert tactician, acrobat and hand-to-hand combatant Using a variety of trick arrows As Goliath: Superhuman strength and durability Size and mass manipulation',
                   51, 'images/portraits/hawkeye.jpg')
    Doctor_Strange = Hero('Doctor Strange', '42', 'alive', 'Marvel', 'Avengers',
                          'Mastery of magic Utilizes mystical artifacts, such as the Cloak of Levitation and the Eye of Agamotto Genius-level intellect Skilled martial artist Gifted physician and surgeon',
                          8600, 'images/portraits/drstrange.jpg')
    Cyclops = Hero('Cyclops', '36', 'dead', 'Marvel', 'X-Men',
                   'Emits powerful beams of energy from his eyes',
                   108, 'images/portraits/cyclops.jpg')

    return [Superman, Batman, Thor, Loki, Hulk, Daredevil, Deadpool, Wolverine, Captain_America, Iceman, Human_Torch,
            Thanos, Nightcrawler, Hawkeye, Doctor_Strange, Cyclops]


def start():
    choice = int(input('''(1) Search the superhero/villain index
(2) Extras
(3) Exit Program

Which option would you like to pick: '''))
    print()

    if choice == 1:
        choice = str(input('Enter a superhero or villain name: '))
        heroes = create_heroes()
        for i in heroes:
            if i.name.lower() == choice.lower():
                print()
                Hero.print_hero(i)
                time.sleep(2)
                Hero.show_image(i)
                start()
        if choice.lower() != i.name.lower():
            print()
            print(colors.red + 'Superhero or villain name not found!', colors.reset, '\n')
            time.sleep(2)
            start()
        else:
            error_message()
    elif choice == 2:
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
    elif choice == 3:
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
