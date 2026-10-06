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
    factor_of_contrast = f_of_c #(standart is 1)
    is_full_width = True
    black = 1 # (standart is 15 or 30)
    is_looping = False
    is_clearing = False # (only for is_looping=True)
    # Включает поддержку ANSI-последовательностей в Windows принудительно
    if sys.platform == "win32":
        os.system('') 

    def get_average_color(img, x, y, w, h):
        rr=0
        rg=0
        rb=0

        for i in range(h):
            for j in range(w):
                rr+=pix[x+j, y+i][0]
                rg+=pix[x+j, y+i][1]
                rb+=pix[x+j, y+i][2]
        
        return ((rr//(w*h)), (rg//(w*h)), (rb//(w*h)))

    input("Position the console as you like and and press Enter. ")
    print("Choose the pic.")
    if is_looping:
        while True:
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
                k = image_width/console_width*2
            else:
                k = max([image_width/console_width*2, image_height/console_height])


            console_image_width = math.floor(image_width/k)
            console_image_height = math.floor(image_height/k)

            console = Console(color_system="truecolor", force_terminal=True)
            a = Text()

            n_y = 0

            for y in range(console_image_height):
                for x in range(console_image_width-1):


                    rgb_color = get_average_color(image, math.floor(x*k), math.floor(y*k), math.floor(k), math.floor(k))
                    if rgb_color[0] + rgb_color[1] + rgb_color[2] < black:
                        a.append("  ")
                    else:
                        a.append("██", style=f"rgb({rgb_color[0]},{rgb_color[1]},{rgb_color[2]})")
                a.append("\n")
                n_y = y
            for i in range(console_height-n_y):
                a.append("\n")
            console.print(a,end="")

            sleep(0.1)
            input()
            if (is_clearing):
                os.system('cls||clear')
    else:
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
            k = image_width/console_width*2
        else:
            k = max([image_width/console_width*2, image_height/console_height])


        console_image_width = math.floor(image_width/k)
        console_image_height = math.floor(image_height/k)

        console = Console(color_system="truecolor", force_terminal=True)
        a = Text()

        n_y = 0

        for y in range(console_image_height):
            for x in range(console_image_width-1):


                rgb_color = get_average_color(image, math.floor(x*k), math.floor(y*k), math.floor(k), math.floor(k))
                if rgb_color[0] + rgb_color[1] + rgb_color[2] < black:
                    a.append("  ")
                else:
                    a.append("██", style=f"rgb({rgb_color[0]},{rgb_color[1]},{rgb_color[2]})")
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