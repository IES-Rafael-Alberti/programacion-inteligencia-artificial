
# Ejemplo: Detección de rostros y landmarks con dlib + OpenCV
import cv2
import dlib

# Cargar detector de rostros y predicción de puntos faciales de dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # descargar previamente

# Cargar imagen con OpenCV
img = cv2.imread("ejemplo.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detectar rostros
faces = detector(img_rgb)

# Dibujar resultados
for face in faces:
    landmarks = predictor(img_rgb, face)
    for n in range(68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
    cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 2)

# Mostrar resultado
cv2.imshow("Detección facial con landmarks", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
