from PIL import Image,ImageEnhance
from PIL import *
from rich.console import Console
from rich.text import Text

import math

from time import sleep

import os

import tkinter as tk
from tkinter import filedialog as fd 

import sys
def draw(f_of_c=1.25):
    from PIL import Image,ImageEnhance
from PIL import *
from rich.console import Console
from rich.text import Text

import math

from time import sleep

import os

import tkinter as tk
from tkinter import filedialog as fd 



import sys
def draw(f_of_c=1.25):
    factor_of_contrast = f_of_c #(standart is 1.25)
    is_full_width = True
    k_w = 1
    # Включает поддержку ANSI-последовательностей в Windows принудительно
    if sys.platform == "win32":
        os.system('') 

    def get_average_color(img, x, y, w, h):
        
        rr=0
        rg=0
        rb=0

        for i in range(max(h,1)):
            for j in range(max(w,1)):
                try:
                    rr+=pix[x+j, y+i][0]
                    rg+=pix[x+j, y+i][1]
                    rb+=pix[x+j, y+i][2]
                except:
                    rr+=128
                    rg+=128
                    rb+=128
        return (int(min(255,rr//max(w*h,1)*k_w)), int(min(255,rg//max(w*h,1)*k_w)), int(min(255,rb//max(w*h,1)*k_w)))



    is_rev = input("Position the console as you like and and press Enter. ")
    print("Choose the pic.")
    name= fd.askopenfilename() 


    image = Image.open(name).convert('RGB')  # Открываем изображение
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(factor_of_contrast)
    image_width = image.size[0]  # Определяем ширину
    image_height = image.size[1]  # Определяем высоту
    pix = image.load()  # Выгружаем значения пикселей

    console_width = os.get_terminal_size().columns
    console_height = os.get_terminal_size().lines

    if is_full_width:
        k = image_width/console_width
    else:
        k = max([image_width/console_width, image_height/console_height])


    console_image_width = math.floor(image_width/k)
    console_image_height = math.floor(image_height/k)

    console = Console(color_system="truecolor", force_terminal=True)
    a = Text()

    n_y = 0
    with open("pol.txt", "r", encoding="utf-8") as file:
        pol = file.readline().strip('\n')
    if pol == "":
        pol = ' .`^*-~+=:;>rilkdb#MW8&%$@'

    if is_rev == "y":
        pol = pol[::-1]

    for y in range(0, math.floor(console_image_height/2)):
        for x in range(console_image_width-1):
            rgb_color = get_average_color(image, math.floor(x*k), math.floor(y*k*2), math.floor(k), math.floor(k))

            a.append("█", style=f"rgb({rgb_color[0]},{rgb_color[1]},{rgb_color[2]})")

        a.append("\n")
        n_y = y
    for i in range(console_height-n_y):
        a.append("\n")
    console.print(a,end="")

    sleep(0.1)
    # print(repr(a))
    input()


if __name__ == '__main__':
    draw()
