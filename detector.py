import cv2
import random as rand
from Blur import *
img = cv2.imread("testImg.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur = cv2.GaussianBlur(gray, (23, 23), 0)

Blur_Object = Blur(img, 1)

blur = Blur_Object.BoxBlur()

cv2.imshow("Custom Blur", blur)

cv2.waitKey(0)

cv2.destroyAllWindows()


color = (rand.randint(0,256), rand.randint(0,256), rand.randint(0,256))

canny = cv2.Canny(blur, 30, 30)
contours, _ = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(f'Number of Contours: {len(contours)}')
shape = img.copy()
cv2.drawContours(shape, contours, -1, color, 2)
cv2.imwrite('{}.png'.format('edges'), shape)
cv2.imshow("Edges Detected Image", shape)
cv2.waitKey(0)

cv2.destroyAllWindows()