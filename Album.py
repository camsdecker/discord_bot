import os
from random import randint
import requests

class Album:
    def __init__(self, dir):
        self.dir = dir
        self.pic_list = os.listdir(dir)

    def addPic(self, pic):
        r = requests.get(pic)
        with open(self.dir + pic.filename, 'wb') as f:
            f.write(r.content)

        self.pic_list.append(pic.filename)

    def getRandomPic(self):
        pic_list = self.pic_list
        dir = self.dir
        
        chosen_pic_index = randint(0,len(pic_list)-1)
        chosen_pic = pic_list[chosen_pic_index]
        pic_path = dir + chosen_pic

        pic_list.remove(chosen_pic)

        return pic_path