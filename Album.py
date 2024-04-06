import os
from random import randint
import requests

class Album:
    def __init__(self, dir):
        self.dir = dir

    def addPic(self, pic):
        r = requests.get(pic)
        with open(self.dir + pic.filename, 'wb') as f:
            f.write(r.content)

    def getRandomPic(self):
        path = self.dir
        pic_list = os.listdir(path)
        chosen_pic_index = randint(0,len(pic_list)-1)
        chosen_pic = pic_list[chosen_pic_index]
        pic_path = path + chosen_pic
        return pic_path