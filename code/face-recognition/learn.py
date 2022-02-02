# https://github.com/Morel-Mathieu/face-recognition-OpenCv

import cv2
import os
import numpy as np
import pickle

cpt = 0

dir_image = "../../rsc/face-recognition-images/"
current_id = 0
list_label = {}

tab_label = []
train_images = []
tab_images_rm_flou = []


for root, dirs, files in os.walk(dir_image):
    if(len(files)): # Je n'ai pas d'images dans ../images_classees
        label = root.split("/")[-1] # Ici on récupère le nom de l'objet qui est le nom du dossier
        for file in files:
            if file.endswith("png"): # On s'assure de ne prendre que les images .png
                chemin = os.path.join(root, file)

                if not label in list_label:
                    list_label[label]=current_id
                    current_id += 1

                name = list_label[label]

                image = cv2.resize(cv2.imread(chemin, cv2.IMREAD_GRAYSCALE), (110,110)) # J'en profite pour resize mes images

                flou = cv2.Laplacian(image, cv2.CV_64F).var() # Laplacian me donne un indice de netteté


                if (flou < 230):
                    print("La photo " + str(chemin) + " est trop flou : " + str(flou))
                    cpt += 1
                    tab_images_rm_flou.append(chemin)
                else:
                    train_images.append(image) # les indices correspondent aux noms & ux visages
                    tab_label.append(name) # Contient le nom des images stockées dans le tableau d'au dessus


with open("labels.pickle", "wb") as f: # Un id et un label
    pickle.dump(list_label, f)

tab_images_rm_flou = np.array(tab_images_rm_flou)
if (tab_images_rm_flou.size == cpt): # Je verifie qu'il y ai bien autant de liens dans le tableau que le compteur
    for lien in tab_images_rm_flou:
        os.remove(lien)


tab_label = np.array(tab_label)
train_images = np.array(train_images)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(train_images, tab_label)
recognizer.save("trainner.yml")
