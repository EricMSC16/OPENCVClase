import cv2

image = cv2.imread(r"FindPalmLines_EliLopez\b.jpg")

cv2.imshow("palm",image) #to view the palm in python
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,40,55,apertureSize = 3)
edges = cv2.bitwise_not(edges)
cv2.imshow("edges in palm",edges)
cv2.waitKey(0)

cv2.imwrite("FindPalmLines_EliLopez\palmlines.jpg", edges)
palmlines = cv2.imread(r"FindPalmLines_EliLopez\palmlines.jpg")
img = cv2.addWeighted(palmlines, 0.4, image, 1, 0)
cv2.imwrite("FindPalmLines_EliLopez\2.jpg", img)
cv2.imshow("edges in palm", img)
cv2.waitKey(0)