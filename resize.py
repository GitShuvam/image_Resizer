import cv2

img = cv2.imread("exmpl.jpg", cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", img)

# percent by which the image is resiged
scale_percent = 50

# Calculate the 50 percent of original dimenshion
new_width = int(img.shape[1] * scale_percent / 100)
new_height = int(img.shape[0] * scale_percent / 100)

# desize
# desize = (width, height)

# resize image
output = cv2.resize(img, (new_width, new_height))

cv2.imwrite('new_img.png', output)
cv2.waitKey(0)
