import os
from random import randint

def read_message(message):
    if message.content == "/pic":
        get_random_pic()
    return

def get_random_pic():
    path = "C:/Users/camsd/Desktop/py_files/discord_bot/pics/"
    pic_list = os.listdir(path)
    chosen_pic_index = randint(0,len(pic_list)-1)
    chosen_pic = pic_list[chosen_pic_index]

    return "C:/Users/camsd/Desktop/py_files/discord_bot/pics/" + chosen_pic