from PIL import Image,ImageEnhance
from PIL import *
from rich.console import Console
from rich.text import Text

import math

from time import sleep

from tkinter import filedialog as fd 
def draw(f_of_c=1.25):
    
    factor_of_contrast = f_of_c #(standart is 1)



    def get_average_color(img, x, y, w, h):
        rr=0
        rg=0
        rb=0

        for i in range(h):
            for j in range(w):
                rr+=pix[x+j, y+i][0]
                rg+=pix[x+j, y+i][1]
                rb+=pix[x+j, y+i][2]
        
        rrggbb = ((rr//(w*h)) + (rg//(w*h)) + (rb//(w*h)))/3

        return (rrggbb)



    is_rev = input("Position the console as you like and and press Enter. Reverse palette? (y/n): ")
    print("Choose the pic.")
    name= fd.askopenfilename() 


    image = Image.open(name).convert('RGB')  # Открываем изображение
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(factor_of_contrast)
    image_width = image.size[0]  # Определяем ширину
    image_height = image.size[1]  # Определяем высоту
    pix = image.load()  # Выгружаем значения пикселей

    console_width = int(input("Width (letters): "))


    k = image_width/console_width



    console_image_width = math.ceil(image_width/k)
    console_image_height = math.ceil(image_height/k)


    a = ""

    n_y = 0
    with open("pol.txt", "r", encoding="utf-8") as file:
        pol = file.readline().strip('\n')
    if pol == "":
        pol = ' .`^*-~+=:;>rilkdb#MW8&%$@'
    k_p = 256 / len(pol)
    if is_rev == "y":
        pol = pol[::-1]

    for y in range(math.ceil(console_image_height/2)):
        for x in range(console_image_width-1):
            rgb_color = get_average_color(image, math.floor(x*k), math.floor(y*k*2), math.floor(k), math.floor(k))
            
            ch = pol[int(rgb_color // k_p)]
            
            
            a+= ch

        a+="\n"
        n_y = y


    with open("out.txt", "w", encoding="utf-8") as file:
        file.write(a)

    print("done =(*_*)=")
    input()

if __name__ == '__main__':
    draw()