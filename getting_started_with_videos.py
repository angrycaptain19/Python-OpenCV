import cv2

cap = cv2.VideoCapture(0);                                      # load default camera
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))    # output video 20 f/s and size 640x480

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)                                        # save frame as RGB color

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          # convert frame to grayscale
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):                   # press 'q' button to break the loop
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()