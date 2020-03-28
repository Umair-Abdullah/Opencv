import cv2


def sketch(image):
    img_g = cv2.cvtColor(image, 0)
    img_g_b =cv2.GaussianBlur(img_g, (7, 7), 0)
    canny_edge = cv2.Canny(img_g_b, 10, 70)

    ret, mask = cv2.threshold(canny_edge, 70, 255, cv2.THRESH_BINARY)
    return mask


# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     cv2.imshow('my sketch', sketch(frame))
#     if cv2.waitKey(1) == 27:
#         break
#     else:
#         cap.release()
#         cv2.destroyAllWindows()



cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1366, 768))
    # frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', sketch(frame))

    c = cv2.waitKey(1)
    if c == 13:
        break

cap.release()
cv2.destroyAllWindows()
