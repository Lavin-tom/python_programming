import cv2
import matplotlib.pyplot as plt
import numpy as np

# read the image
img = cv2.imread('projects\prominent_color_from_image\image.jpg')

# check if the image is grayscale
if len(img.shape) < 3:
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# convert the image to the HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# calculate the histogram of the image
hist = cv2.calcHist([hsv_img], [0], None, [180], [0, 180])
# plot the histogram
plt.hist(hsv_img[:,:,0].ravel(), 180, [0, 180])
plt.show()

# find the bin with the highest value in the histogram
dominant_hue = np.argmax(hist)

# convert the bin index to the corresponding color value in the HSV color space
dominant_color_hsv = np.array([[[dominant_hue, 255, 255]]], dtype=np.uint8)
dominant_color_rgb = cv2.cvtColor(dominant_color_hsv, cv2.COLOR_HSV2BGR)[0][0]

# print the dominant color in RGB format
print('Dominant color:', dominant_color_rgb)
