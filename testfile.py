import os
from random import randint

path = os.getcwd() + "\pics"
pic_list = os.listdir(path)
chosen_pic_index = randint(0,len(pic_list)-1)
chosen_pic = pic_list[chosen_pic_index]
print(chosen_pic)