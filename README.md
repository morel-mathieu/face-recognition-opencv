# face-recognition-OpenCv
Second year project on initiation to AI

# librairies
numpy         : https://numpy.org/
opencv-python : https://pypi.org/project/opencv-python/
glob          : https://github.com/python/cpython/blob/3.6/Lib/glob.py
os            : https://github.com/python/cpython/blob/3.10/Lib/os.py
pickle        : https://github.com/python/cpython/blob/3.10/Lib/pickle.py

# Programs

## code/
### face-recognition
#### learn.py
### haar/
#### haar.py
Ce programme permet de préparer les fichiers nécéssaires à la création de notre haar cascade.
Les images détéctées sont des .jpg, attention à votre dataset !
### face-recognition/
#### learn.py
Ce programme permet en fonction des noms des dossiers dans rsc/face-recognition-images/x/ de créer des labels qui seront affichés sur le visage de la personne reconnue dans le programme d'identification.
Il permet de générer un fichier pré-entrainé avec le local binary pattern ainsi que le modèle histogramme : https://docs.opencv.org/3.4/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html
Les images détéctées sont des .jpg, attention à votre dataset !
#### identification.py
Ce programme ouvre un flux vidéo celui de la webcam d'un ordinateur portable. Pour les webcams externes ou autre, vous pouvez vous référer à la documentation d'OpenCv/cv2.VideoCapture
## rsc/
### face-recognition-images/
Dans ce dossier, vous devez créer des dossiers dont les noms seront les labels affichés dans le programme d'identification.
Au sein de ces dossiers, par exemple : face-recognition-images/obama vous devez mettre votre dataset de photos de la personne à reconnaître.
### haar/
### negatives/
Dans ce dossier, il faut mettre son dataset d'images négatives.
### negatives_resize/
Dans ce dossier le programme haar.py va placer les images négatives redimentionnées en échelle de gris.
### positives/
Dans ce dossier, il faut mettre son dataset d'images positives.
### positives_resize/
Dans ce dossier le programme haar.py va placer les images positives redimentionnées en échelle de gris.
