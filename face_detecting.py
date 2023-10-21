import cv2


# load some pre-trained data from haar cascade opencv algorithm
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

"""

#choose an image to try with
img = cv2.imread('bpANDld.jpg')


#open the img
# cv2.imshow('img window', img)
# cv2.waitKey()

#convert to black and white
grayScaledImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # cv2.imshow('img window', grayScaledImg)
        # cv2.waitKey()

#detect the face
faceCoordinates = trained_face_data.detectMultiScale(grayScaledImg)
print(faceCoordinates)

#Draw a rectengle around the face
for x in faceCoordinates:
    (x, y, w, h) = x
    cv2.rectangle(img,(x ,y),(x+w, y+h) ,(0,255,0) ,2)

cv2.imshow('img window', img)
cv2.waitKey()


"""


#From the webcam ( or a video file : just paste the video's path instead of the 0)
webcam = cv2.VideoCapture(0)

#do a loop so the webcam can run infinitly
n = 1
while True:
    # read the current frame
    seccessful_reading, frameRead = webcam.read()
    grayScaledImg = cv2.cvtColor(frameRead, cv2.COLOR_BGR2GRAY)
    faceCoordinates = trained_face_data.detectMultiScale(grayScaledImg)
    for x in faceCoordinates:
        (x, y, w, h) = x
        cv2.rectangle(frameRead,(x ,y),(x+w, y+h) ,(0,255,0) ,2)
    cv2.imshow('img window', frameRead)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
webcam.release()

print("code completed")