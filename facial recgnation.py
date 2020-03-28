import cv2
import numpy

# user = input('Enter your name : ')
face_detector = cv2.CascadeClassifier(
    'C:/Users/CSC17/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def data(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return None
    for (x, y, h, w) in faces:
        cropped = img[y:y + h, x:x + w]
        return cropped


cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if data(frame) is not None:
        face = cv2.resize(data(frame), (400, 400))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        count += 1

        file_name = 'C:/Users/CSC17/PycharmProjects/opencv/faces/user' + str(count) + '.jpg'
        cv2.imwrite(file_name, face)

        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)
        cv2.imshow("DATA COLLECTION", face)
    else:
        print("Face Not Found")
        pass
    if cv2.waitKey(1) == 13 or count == 100:
        break
cap.release()
cv2.destroyAllWindows()
print("data collection is completed!!")
