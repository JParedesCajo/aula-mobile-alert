import cv2


def main():
    print("Buscando cámaras disponibles...\n")

    for index in range(6):
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)

        if cap.isOpened():
            ret, frame = cap.read()

            if ret:
                print(f"[OK] Cámara disponible en índice {index}")
            else:
                print(f"[AVISO] Índice {index} abre, pero no entrega imagen")

            cap.release()

        else:
            print(f"[NO] Sin cámara en índice {index}")


if __name__ == "__main__":
    main()