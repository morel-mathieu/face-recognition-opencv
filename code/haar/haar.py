# https://github.com/Morel-Mathieu/face-recognition-OpenCv

import numpy as np
import glob
import cv2
import os

# Fonction permettant de redimensionner l'ensemble des images négatives que l'on a dans le dossier negatives
def resizeNeg():
    neg_link = glob.glob("../../rsc/haar/negatives/*.jpg")
    a = 1
    for i in neg_link:
        img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img, (100, 100))
        cv2.imwrite("../../rsc/haar/negatives_resize/"+str(a)+".jpg", resized_image)
        a += 1


# Fonction permettant de redimensionner l'ensemble des images positives
def resizePos():
    neg_link = glob.glob("../../rsc/haar/positives/*.jpg")
    a = 1
    for i in neg_link:
        img = cv2.imread(i, cv2.COLOR_BGR2RGB)
        resized_image = cv2.resize(img, (50, 50))
        cv2.imwrite("../../rsc/haar/positives_resize/p"+str(a)+".jpg", resized_image)
        a += 1


# Fonction permettant de créer le fichier indiquant le chemin de chaque image négative
def create_neg():
    for file_type in ['negatives_resize']:

        for img in os.listdir(file_type):
            line = file_type+'/'+img+'\n'
            with open('bg.txt', 'a') as f:
                f.write(line)


# Fonction permettant de créer le fichier indiquant le chemin de chaque image positive ainsi que la zone dans laquelle se trouve l'élément qu'on recherche
def create_pos():
    for file_type in ['positives_resize']:
        for img in os.listdir(file_type):
            line = file_type+'/'+img+' 1 0 0 50 50\n'
            with open("info.dat", 'a') as f:
                f.write(line)
