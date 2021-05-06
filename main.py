import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Rectangle for birds
    for i in range(250, 300):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    # Rectangle for cactus
    for i in range(275, 325):
        for j in range(563, 680):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("The dino game about to start in 3 sec")
    time.sleep(3)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))
'''
        # Draw the Rectangle for birds
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 170
        
        # Draw the Rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 680):
                data[i, j] = 0

        image.show() 
        break
        '''


# pip install pyautogui
# pip install pillow
# ImageGrab.grab() - function to take ss of current window
#then .show is used
# PIL module ki help se image grab karke mai dekhuga ki wha pe kala pixel hai ki ni, aur a jata hai to wha pe we will use pyautogui
# image.load se image array ke form me a jati hai, but initially if u wanna see it then its in pixel object form
# if you want to show the data i.e the image,  in the array form then use numpy module with asarray
# image is a 2-D matrix in actuall if you wanna test, then zoom in any image in photoshop.
# There are two types of images grey-scale and colored. Grey-scale means black and white , while colored means R, G, B.
# the range is btw 0 - 255 . 0 is black and 255 is white.
# we are converting images to grey- scale becoz processing is easy as compared to colored image
# jo i,j coordinates ke andar ka area hai uska color black ho jayega coz we have given 0
# image.load se apan chahte hain ki baar baar image lete rhe and check kare ki khi collide to ni karrha
# in line 30, hit up karne se game start ho jayega jo ki automatic press hogi but cursor to rakhna padega, but uska kaam hi kya hai
# TERMINOLOGY - jumping and ducking
