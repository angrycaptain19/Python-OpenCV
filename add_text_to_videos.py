import cv2
import  datetime

cap = cv2.VideoCapture(0)   # load default camera
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(3, 1208)    # set width frame
#cap.set(4, 720)     # set height frame
#print(cap.get(3))
#print(cap.get(4))
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret != True:
        break

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Width: '+ str(cap.get(3)) + ' Height: ' + str(cap.get(4))
    date = str(datetime.datetime.now())
    frame = cv2.putText(frame, date, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()