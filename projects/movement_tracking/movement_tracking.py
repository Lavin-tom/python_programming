import cv2

# create a background subtractor object
bs = cv2.createBackgroundSubtractorMOG2()

# open the camera and read the first frame
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# loop over the frames
while ret:
    # apply background subtraction to the frame
    fgmask = bs.apply(frame)

    # apply thresholding to the foreground mask to obtain a binary image
    thresh = cv2.threshold(fgmask, 25, 255, cv2.THRESH_BINARY)[1]

    # find contours in the binary image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # loop over the contours and draw bounding boxes around the moving objects
    for c in contours:
        # get the bounding box for the contour
        (x, y, w, h) = cv2.boundingRect(c)

        # draw the bounding box on the frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # display the frame with bounding boxes
    cv2.imshow('frame', frame)

    # read the next frame
    ret, frame = cap.read()

    # exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the camera and close all windows
cap.release()
cv2.destroyAllWindows()