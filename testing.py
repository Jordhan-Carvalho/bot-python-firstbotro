import time
from PIL import ImageGrab, ImageOps
from numpy import *
import pyautogui
import pydirectinput
import os
from random import randint

DELAY_BETWEEN_COMMANDS = 1.00

class Coordinates():
    charCenter = (956, 536)

def main():
    initializePyAutoGUI()
    countdownTimer()

    # while True:
    #     imageGrab()
    for i in range(0,250):
        position = getStartingPos()
        print("Alvo encontrado, tentando atacar")
        pyautogui.click(position)
        time.sleep(0.1)
        pyautogui.click(position)
        print("Fim esperando 10 segs")
        time.sleep(10)



def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True

def countdownTimer():
    print("Starting", end="")
    for i in range(0, 5):
        print(".", end="")
        time.sleep(1)
    print("Go")

def reportMousePosition(seconds = 10):
    for i in range(0, seconds):
        print(pyautogui.position())
        time.sleep(1)

def holdKey(key, seconds = 1.00):
    pyautogui.keyDown(key)
    time.sleep(seconds)
    pyautogui.keyUp(key)
    time.sleep(DELAY_BETWEEN_COMMANDS)

# Make a box in the screen and sum the RBG pixel values in greyScale
# from https://www.youtube.com/watch?v=skC3QblU4lg&t=5s
def imageGrab():
    box = (1073, 380, 1305, 564)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())

def getStartingPos():
    # loop over images until one is found, then return the index of the found
    # image
    print("Procurando")
    images_to_check = [
            'presente_small_1.png',
            'presente_small_2.png',
            'presente_small_3.png',
            'presente_small_4.png',
            'presente_small_5.png',
            'presente_small_6.png',
    ]    
    image_pos = None
    possiveis_caminhos = [(531, 869), (1481, 504), (1079, 161), (447, 391)]
    numeroDeAndadas = 0
    while image_pos is None:
        print("Loop do while image_post is none")
        if numeroDeAndadas > 15:
            print("teleportar")
            holdKey('f1')
            numeroDeAndadas = 0
        randomNum = randint(0, 3)
        pyautogui.click(possiveis_caminhos[randomNum])
        for index, image_filename in enumerate(images_to_check):
            print(f"Procurando imagem {index}")
            script_dir = os.path.dirname(__file__)
            needle_path = os.path.join(
                script_dir, 
                'needles', 
                image_filename
            )
            image_pos = pyautogui.locateOnScreen(needle_path,  grayscale=True, confidence=.9)
            if image_pos != None:
                print(f"Achou imagem dentro do for loop{image_pos}")
                x = image_pos.left + (image_pos.width / 2)
                y = image_pos.top + (image_pos.height / 2)
                return (x, y)
        numeroDeAndadas += 1
        # andar alguma vezes depois usar asa de mosca
    print(image_pos)



    # print("inicio")
    # script_dir = os.path.dirname(__file__)
    # needle_path = os.path.join(
    #     script_dir, 
    #     'needles', 
    #     'orc_lady_small.png'
    # )
    # # to confidence to work have to install pip install opencv_python
    # image_pos = pyautogui.locateOnScreen(needle_path, grayscale=False, confidence=.7)

    # possiveis_caminhos = [(531, 869), (1481, 504), (1079, 161), (447, 391)]
    # numeroDeAndadas = 0

    # while image_pos is None:
    #     print("Procurando alvo")
    #     if numeroDeAndadas > 15:
    #         holdKey('f1')
    #         numeroDeAndadas = 0
    #     randomNum = randint(0, 3)
    #     pyautogui.click(possiveis_caminhos[randomNum])
    #     image_pos= pyautogui.locateOnScreen(needle_path, grayscale=False, confidence=.7)
    #     numeroDeAndadas += 1
    #     # andar alguma vezes depois usar asa de mosca

    # print(numeroDeAndadas)
    # print("fim")
    # # centralizar o click
    # x = image_pos.left + (image_pos.width / 2)
    # y = image_pos.top + (image_pos.height / 2)
    # return (x, y)

if __name__ == "__main__":
    main()  