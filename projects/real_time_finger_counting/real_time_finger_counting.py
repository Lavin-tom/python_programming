import cv2
import mediapipe

thumb_x1= thumb_y1= thumb_x2= thumb_y2 =0
index_x1=index_x2=index_y1= index_y2 = 0
ring_x1=ringx2=ring_y1=ring_y2=0
middle_x1 = middle_x2 = middle_y1=middle_y2=0
little_x1=little_x2=little_y1=little_y2=0
count = 0
capture_hands = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
camera = cv2.VideoCapture(0)
while True:
    _, image = camera.read()
    image_height, image_width, _ = image.shape
    image = cv2.flip(image, 1)
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_hands = capture_hands.process(rgb_img)
    all_hands = output_hands.multi_hand_landmarks
    count = 0
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image, hand)

        one_hand_landmarks = hand.landmark
        for id, lm in enumerate(one_hand_landmarks):
            x = int (lm.x * image_width)
            y = int (lm.y * image_height)
            #print(x,y)
            # thumb finger
            if id == 4:
                thumb_x1 =  x
                thumb_y1 = y
            if id == 3:
                thumb_x2 =  x
                thumb_y2 = y
            # index finger
            if id == 8:
                index_x1 =  x
                index_y1 = y
            if id == 7:
                index_x2 = x
                index_y2 = y
            # middle 
            if id == 12:
                middle_x1 = x
                middle_y1 = y
            if id == 11:
                middle_x2 = x
                middle_y2 = y
            #  ring finger
            if id == 16:
                ring_x1 =  x
                ring_y1 = y
            if id == 15:
                ring_x2 = x
                ring_y2 = y
            # little finger
            if id == 20:
                little_x1 = x
                little_y1 = y
            if id == 19:
                little_x2 = x
                little_y2 = y

    #print (x1,y1,x2, y2)
    thump_dist = thumb_y1 - thumb_y2
    index_dist = index_y1 - index_y2
    middle_dist = middle_y1 - middle_y2
    ring_dist = ring_y1 - ring_y2
    little_dist = little_y1 - little_y2    

    if thump_dist<0:
        count += 1
    if index_dist<0:
        count += 1
    if middle_dist<0:
        count += 1
    if ring_dist<0:
        count += 1
    if little_dist<0:
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    fps_text = "finger count: {}".format(count)
    cv2.putText(image, fps_text, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    #print(count)
    cv2.imshow("Testing of real_time_finger_counting",image)
    key = cv2.waitKey(100)
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()