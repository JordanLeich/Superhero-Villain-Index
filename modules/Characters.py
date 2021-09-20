import time
from PIL import Image


class Character:
    def __init__(self, name, age, status, creator, team, durability, energy, fighting, intelligence, speed, strength, powers, power_ranking, image_path):
        self.name = name
        self.age = age
        self.status = status
        self.creator = creator
        self.team = team
        self.durability = durability
        self.energy = energy
        self.fighting = fighting
        self.intelligence = intelligence
        self.speed = speed
        self.strength = strength
        self.powers = powers
        self.power_ranking = power_ranking
        self.image_path = image_path

    def print_hero(self):
        print('Name: ' + self.name + '\n'
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

