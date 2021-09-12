import sys
import time
from modules import colors


class Hero:
    def __init__(self, name, age, status, creator, team, powers, power_ranking):
        self.name = name
        self.age = age
        self.status = status
        self.creator = creator
        self.team = team
        self.powers = powers
        self.power_ranking = power_ranking

    def print_hero(self):
        print('Superhero Name: ' + self.name + '\n'
              'Age: ' + str(self.age) + '\n'
              'Status: ' + self.status + '\n'
              'Creator: ' + self.creator + '\n'
              'Team: ' + self.team + '\n'
              'Powers: ' + self.powers + '\n'
              'Power Ranking: ' + str(self.power_ranking))

def create_heroes():
    Superman = Hero('Superman', 'Immortal age/mid 20 or 30s', 'alive', 'DC', 'Justice League',
                    'super strength, flight, invulnerability, super speed, heat vision, freeze breath, x-ray vision, superhuman hearing, healing factor',
                    448000)
    Batman = Hero('Batman', 48, 'alive', 'DC', 'Justice League', 'no superpowers', 145)
    Thor = Hero('Thor', 1500, 'alive', 'Marvel',
                'Avengers',
                'superhuman strength, speed, agility, durability and immunity to most diseases', 493000)
    Loki = Hero('Loki', 1000, 'deceased', 'Marvel', 'none',
                'strength, durability, and longevity far superior to humans', 616)
    Hulk = Hero('Hulk', 49, 'alive', 'Marvel', 'Avengers', 'strength ', 6900)
    Daredevil = Hero('Daredevil', 25, 'alive', 'Marvel', 'none',
                     'Superhuman senses Echolocative radar sense Skilled acrobat, martial artist, and stick fighter Utilization of specially-designed billy club',
                     83)
    Deadpool = Hero('Deadpool', 'immortal, over 800', 'alive', 'Marvel', 'none',
                    'accelerated healing factor',
                    115)
    Wolverine = Hero('Wolverine', 'over 200', 'alive', 'Marvel', 'X-Men',
                     'superhuman strength and reflexes, enhanced senses and tracking abilities, and a special healing power that also slows his aging.',
                     79)
    Captain_America = Hero('Captain America', 99, 'unknown', 'Marvel', 'Avengers',
                           'Peak-Human Condition, Accelerated Healing Factor, Enhanced Intelligence, Longevity',
                           94)
    heroes = [Superman, Batman, Thor, Loki, Hulk, Daredevil, Deadpool, Wolverine, Captain_America]
    return heroes


def start():
    choice = str(input('Enter a superheros name: '))
    heroes = create_heroes()
    for i in heroes:
        if i.name == choice:
            Hero.print_hero(i)

    # TODO once a superhero name is inputted, print out all the details about that hero.


if __name__ == '__main__':
    running = True

    if running:
        start()
    else:
        print(colors.red + 'Error found!', colors.reset)
        time.sleep(2)
        sys.exit()
