import cv2
import mediapipe
import pyautogui

x1 = y1 = x2 = y2 = 0
capture_hands  = mediapipe.solutions.hands.Hands()
drawing_option = mediapipe.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
camera = cv2.VideoCapture(0)
while True:
    _,image = camera.read()
    image_height,image_width,_ = image.shape    #don't want depth
    image = cv2.flip(image,1)       #flip vertical axis
    rgb_img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)     #convert img into rgb mode
    output_hands = capture_hands.process(rgb_img)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(image,hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * image_width)
                y = int(lm.y * image_height)
                #print(x,y)
                if id == 8:
                    mouse_x = int(screen_width/image_width * x)
                    mouse_y = int(screen_height/image_height * y)
                    cv2.circle(image,(x,y),10,(0,255,255))
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x1 = x
                    y1 = y
                if id == 12:
                    cv2.circle(image,(x,y),10,(0,255,255))
                    pyautogui.moveTo(mouse_x,mouse_y)
                    x2 = x
                    y2 = y
        dist = y1 - y2
        if dist < 5:
            pyautogui.click()
        print(dist)
    cv2.imshow("Hand movement capture",image)
    key = cv2.waitKey(100)
    # if esc press close the window
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()