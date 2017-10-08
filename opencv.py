import cv2
 
def detect(path):
    img = cv2.imread(path)
    # Pasamos la ruta del XML
    cascade = cv2.CascadeClassifier("C:\Users\Admin\Desktop\haarcascade_frontalface_alt.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20,20))
 
    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img
 
def box(rects, img):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    # Ruta donde guardaremos la imagen con la deteccion de rostros
    cv2.imwrite('C:\Users\Admin\Desktop\prueba.jpg', img);
 
# Pasamos la imagen que quremos detectar
rects, img = detect("C:\Users\Admin\Desktop\Imagen.jpg")
box(rects, img)