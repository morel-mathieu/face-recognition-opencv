# https://github.com/Morel-Mathieu/face-recognition-OpenCv

import cv2
import pickle
import numpy as np

color_ok = (0,255,0)
color_ko = (0,0,255)
color_info = (255,255,255)
name_image = 0

face_cascade = cv2.CascadeClassifier("../../rsc/haarcascade_frontalface_alt2.xml")
if (face_cascade.empty()):
    print("Erreur de chargement du fichier ! :(")
    quit()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    # Vérifier le load
    labels = {v:k for k, v in og_labels.items()}

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) # L'entrée vidéo de mon ordinateur portable (0, cv2.CAP_DSHOW)

while True:
    if (cam.isOpened() == True):
        retcam, frame = cam.read() # Fonction qui retunr une valeur et l'image dans frame
        temps = cv2.getTickCount() # Ici on prend une mesure de temps pour calculer les fps

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Passage de l'image en gris pour faciliter détection

        # detectMultiScale renvoi 4 valeurs, x, y du rectangle contient l'objet
        # minNeighbors regarde si sur une couche voisine l'objet existe
        face = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
        for x,y,w,h in face:
            visage_film = gray[y:y+h, x:x+w] # On récupère que le visage gris de la webcam
            id, conf = recognizer.predict(visage_film)

            # Plus l'indice est bas plus le visge sera bon (généralement entre 80 et 100)
            if conf <= 80 :
                color = color_ok
                name = labels[id] # On va chercher dans le tableau formaté du fichier pickle

            else:
                color = color_ko
                name = "Inconnu"

            text = name + " Indice confiance : " + "{:5.2f}".format(conf)
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_PLAIN, 1, color_info, 1, cv2.LINE_AA)

            # On dessine un rectangle : start, end, color, taille_trait
            cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)

            # Relache le flux vidéo et quit le programme
            if cv2.waitKey(1) == ord("q"):
                cam.release()
                cv2.destroyAllWindows()
                print("Au revoir !")
                quit()

            fps = cv2.getTickFrequency()/(cv2.getTickCount()-temps) # Calcul fps
            # Affichage : Image, text en float, pos, font, taille_trait, couleur, type, trait
            cv2.putText(frame, "[FPS : {:05.2f}]".format(fps), (10,30), cv2.FONT_HERSHEY_PLAIN, 1, color_info, 1)
            cv2.putText(frame, "Quitter 'q'", (10,10), cv2.FONT_HERSHEY_PLAIN, 1, color_info, 1)

            cv2.imshow('Face Detection', frame)

    else:
        print("Erreur à l'ouverture de la webcam ! :(")
