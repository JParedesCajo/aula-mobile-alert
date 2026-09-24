import os
import cv2


CAMERA_URL = os.getenv("CAMERA_URL")


def main():
    if not CAMERA_URL:
        print("No se ha definido CAMERA_URL.")
        print("Ejemplo:")
        print('$env:CAMERA_URL="http://192.168.1.12:4747/video"')
        return

    cap = cv2.VideoCapture(CAMERA_URL)

    if not cap.isOpened():
        print("No se pudo acceder al flujo de video.")
        return

    print("Cámara iniciada correctamente.")
    print("Presiona Q para salir.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("No se pudo obtener un frame.")
            break

        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        cv2.imshow("Aula Mobile Alert - Camera Test", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()