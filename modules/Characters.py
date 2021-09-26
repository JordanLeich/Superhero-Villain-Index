import time
from PIL import Image


class Character:
    def __init__(self, name, age, status, creator, team, durability, energy, fighting, intelligence, speed, strength,
                 powers, power_ranking, image_path):
        self.attributes = {"Name": name,
                           "Age": age,
                           "Status": status,
                           "Creator": creator,
                           "Powers": powers,
                           "Power Ranking": power_ranking
                           }
        # fighting attributes
        self.stats = {"Durability": durability,
                      "Energy": energy,
                      "Fighting": fighting,
                      "Intelligence": intelligence,
                      "Speed": speed,
                      "Strength": strength,
                      }
        # Misc attributes
        self.image_path = image_path
        self.team = team

    def __str__(self):  # print general attributes of character
        return (
            '\n'.join(': '.join([k, str(v)]) for k, v in self.attributes.items())
            + '\n'
        )

    def total_stats(self):
        return sum(self.stats.values())

    def get_stat(self, stat_name):
        return self.stats[stat_name]

    def get_name(self):
        return self.attributes["Name"]

    def show_image(self):
        img = Image.open(self.image_path)
        img.show(self.image_path)
        time.sleep(2)
