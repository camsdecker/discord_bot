import os
from random import randint

def get_random_pic():
    path = "/home/cam/discord_bot/discord_bot/pics/"
    pic_list = os.listdir(path)
    chosen_pic_index = randint(0,len(pic_list)-1)
    chosen_pic = pic_list[chosen_pic_index]

    return path + chosen_pic