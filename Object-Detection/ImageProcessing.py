# Import Package
import cv2
# Creating Image Object
imgObj= cv2.imread("Puppy.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Text", imgObj)
cv2.waitKey(0)
cv2.destroyAllWindows()