import time
from PIL import Image


class Character:
    def __init__(self, character_attribute):
        self.name = character_attribute['name']
        self.age = character_attribute['age']
        self.status = character_attribute['status']
        self.creator = character_attribute['creator']
        self.team = character_attribute['team']
        self.powers = character_attribute['powers']
        self.power_ranking = character_attribute['power_ranking']
        self.image_path = character_attribute['image_name']

    def print_stats(self):
        for key, value in vars(self).items():
          if key != 'image_path':
              print(f"{key.replace('_', ' ').capitalize()}: {value}")
        print('')

    def show_image(self):
        img = Image.open(f'images/portraits/{self.image_path}')
        img.show(f'images/portraits/{self.image_path}')
        time.sleep(2)
