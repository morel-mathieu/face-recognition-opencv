# https://github.com/Morel-Mathieu/face-recognition-OpenCv

import cv2

face_cascade = cv2.CascadeClassifier("../../rsc/haarcascade_frontalface_alt2.xml")
if (face_cascade.empty()):
    print("Erreur de chargement du fichier ! :(")
    quit()

cam = cv2.VideoCapture("../../rsc/face-recognition-images/create-your-own-dataset/video/your-video.mp4") # La lecture de la vidéo

name = 0

while True:
    if (cam.isOpened() == True):
        retvid, frame = cam.read() # Fonction qui retunr une valeur et l'image dans frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Passage de l'image en gris pour faciliter détection

        # detectMultiScale renvoi 4 valeurs, x, y du rectangle contient l'objet
        # minNeighbors regarde si sur une couche voisine l'objet existe
        face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
        for x,y,w,h in face:
            # On l'enregistre
            cv2.imwrite("../../rsc/face-recognition-images/create-your-own-dataset/dataset/face-{:d}.png".format(name), frame[y:y+h, x:x+h])
            name += 1
            # On dessine un rectangle : start, end, color, taille_trait
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

            # Relache le flux vidéo et quit le programme
            if cv2.waitKey(1) == ord("q"):
                cam.release()
                cv2.destroyAllWindows()
                quit()

        for cpt in range(10):
            retvid, frame = cam.read() # On lit 40 images pour rien pour accelérer

        cv2.imshow('Découpage Vidéo', frame)

    else:
        print("Erreur à l'ouverture de la webcam ! :(")
