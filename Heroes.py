import time
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
              'Power Ranking: ' + str(self.power_ranking) + '\n')

    def show_image(self):
        img = Image.open(self.image_path)
        img.show(self.image_path)
        time.sleep(2)