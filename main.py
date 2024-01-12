import cv2

def turn_on_camera():
    # Cette fonction permet d'allumer la caméra
    cap = cv2.VideoCapture(0) # 0 = premier port de caméra, 1 = deuxième port de caméra, etc.
    while True:
        ret, frame = cap.read() # Lecture d'un frame
        if not ret:
            break
        cv2.imshow('Caméra en direct', frame) # Affichage du frame
        if cv2.waitKey(1) & 0xFF == ord('q'): # Appuyez sur la touche 'q' pour arrêter
            break
    cap.release() # Libération des ressources
    cv2.destroyAllWindows() # Fermeture de toutes les fenêtres

def turn_off_camera():
    # Cette fonction permet d'éteindre la caméra
    cv2.destroyAllWindows() # Fermeture de toutes les fenêtres

if __name__ == "__main__":
    # Allumer la caméra
    turn_on_camera()

    # Éteindre la caméra
    turn_off_camera()