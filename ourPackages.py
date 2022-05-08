import cv2 as cv
import pandas as pd
import colorama
import itertools, sys
from colorama import Fore, Back
import numpy as np
import csv
import face_recognition
import os
from faceRecognize import FC
import time
from dataBase import updateDatabase
colorama.init(autoreset=True)
H = 0


def cls():
    os.system('cls')


def animate():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(10):
        time.sleep(0.5)
        sys.stdout.write(Fore.GREEN + "\rChecking in.... " + animation[i % len(animation)])
        sys.stdout.flush()
